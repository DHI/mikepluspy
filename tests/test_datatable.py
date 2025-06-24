from __future__ import annotations

import pytest

from mikeplus import DataTableDemoAccess
from datetime import datetime
from shapely import wkt
from shapely.geometry import LineString


def test_open_database(sirius_db):
    """Test opening and closing a database."""
    data_access = DataTableDemoAccess(sirius_db)
    data_access.open_database()
    assert data_access.is_database_open() is True
    data_access.close_database()
    assert data_access.is_database_open() is False


# Helper function to setup and teardown database access
@pytest.fixture
def data_access(sirius_db):
    """Fixture to provide an open database connection for tests."""
    access = DataTableDemoAccess(sirius_db)
    access.open_database()
    yield access
    access.close_database()


@pytest.mark.parametrize(
    "table_name, muid, fields, expected_values",
    [
        # Test getting float values
        ("msm_Link", "Link_30", "Length", [4.06]),
        # Test getting multiple fields (float and float)
        ("msm_Link", "Link_30", ["Length", "Diameter"], [4.06, 1.0]),
        # Test getting string values
        ("msm_Link", "Link_29", ["fromnodeid", "tonodeid"], ["Node_36", "Node_27"]),
        # Test getting integer values (Enabled is typically an integer field)
        ("msm_Link", "Link_30", "Enabled", [1]),
        # Test getting geometry as WKT string
        (
            "msm_Link",
            "Link_30",
            "geometry",
            [
                "LINESTRING (102067.80047607422 109100.27648925781, 102405.85711669922 108873.84887695313)"
            ],
        ),
    ],
)
def test_get_field_values(
    data_access: DataTableDemoAccess, table_name, muid, fields, expected_values
):
    """Test retrieving field values from a database table."""
    values = data_access.get_field_values(table_name, muid, fields)
    if fields == "geometry":
        assert "LINESTRING" in values[0]
        assert "102067.8" in values[0]
        assert "109100.2" in values[0]
        assert "102405.8" in values[0]
        assert "108873.8" in values[0]
    else:
        assert values == expected_values


@pytest.mark.parametrize(
    "table_name, where_clause, expected_count, expected_muids",
    [
        ("msm_Link", "MUID='Link_30'", 1, ["Link_30"]),
        (
            "msm_Link",
            "Diameter=1.0",
            8,
            [
                "Link_29",
                "Link_30",
                "Link_34",
                "Link_35",
                "Link_36",
                "Link_37",
                "Link_33",
                "Link_2",
            ],
        ),
        ("msm_Link", "fromnodeid='Node_36' AND tonodeid='Node_27'", 1, ["Link_29"]),
        ("msm_Link", "MUID='NonExistentLink'", 0, None),
    ],
)
def test_get_muid_where(
    data_access, table_name, where_clause, expected_count, expected_muids
):
    """Test retrieving MUIDs based on a WHERE condition."""
    muids = data_access.get_muid_where(table_name, where_clause)

    # Verify correct number of results
    assert len(muids) == expected_count

    # If we expect a specific MUID, verify it's in the results
    if expected_muids is not None:
        assert expected_muids == muids


@pytest.mark.parametrize(
    "table_name, test_muid, field_values, verify_fields",
    [
        # Test case 1: Link with float value
        (
            "msm_Link",
            "link_test_float",
            {
                "Diameter": 2.5,  # float
                "Description": "insert_float_test",
                "geometry": "LINESTRING (3 4, 10 50, 20 25)",
            },
            ["Diameter", "Description", "geometry"],
        ),
        # Test case 2: Link with integer value
        (
            "msm_Link",
            "link_test_int",
            {
                "Diameter": 3.0,
                "Description": "insert_int_test",
                "Enabled": 1,  # integer
            },
            ["Diameter", "Description", "Enabled"],
        ),
        # Test case 3: Link with string value
        (
            "msm_Link",
            "link_test_string",
            {
                "Diameter": 1.8,
                "Description": "This is a test string with special chars: !@#$%",  # complex string
            },
            ["Diameter", "Description"],
        ),
        # Test case 4: Link with WKT geometry as string
        (
            "msm_Link",
            "link_test_wkt",
            {
                "Diameter": 1.5,
                "Description": "wkt_geometry_test",
                "geometry": "LINESTRING (0 0, 5 5, 10 10)",  # WKT string
            },
            ["Diameter", "Description", "geometry"],
        ),
        # Test case 5: Link with Shapely LineString geometry
        (
            "msm_Link",
            "link_test_shapely",
            {
                "Diameter": 1.2,
                "Description": "shapely_geometry_test",
                "geometry": LineString(
                    [(0, 0), (10, 10), (20, 5)]
                ),  # Shapely LineString
            },
            ["Diameter", "Description", "geometry"],
        ),
        # Test case 6: Project with datetime values
        (
            "msm_Project",
            "project_test_1",
            {
                "ComputationBegin": datetime(2023, 11, 1, 0, 0, 0, 0),
                "ComputationEnd": datetime(2023, 11, 1, 1, 0, 0, 0),
            },
            ["ComputationBegin", "ComputationEnd"],
        ),
    ],
)
def test_insert(
    data_access: DataTableDemoAccess, table_name, test_muid, field_values, verify_fields
):
    """Test inserting a new record into a table with various data types."""
    # First ensure test data doesn't exist
    muids = data_access.get_muid_where(table_name, f"MUID='{test_muid}'")
    if len(muids) == 1:
        data_access.delete(table_name, test_muid)

    # Insert test data
    data_access.insert(table_name, test_muid, field_values)

    # Verify insertion
    muids = data_access.get_muid_where(table_name, f"MUID='{test_muid}'")
    assert len(muids) == 1

    # Verify field values
    values = data_access.get_field_values(table_name, test_muid, verify_fields)

    # Check that each field value matches what we set
    for i, field in enumerate(verify_fields):
        expected = field_values[field]

        actual = values[i]

        if isinstance(expected, LineString):
            actual_geom = wkt.loads(actual)
            assert actual_geom.equals(expected), (
                f"Field {field} expected {expected} but got {actual}"
            )
        else:
            assert actual == expected, (
                f"Field {field} expected {expected} but got {actual}"
            )

    # Clean up
    data_access.delete(table_name, test_muid)


@pytest.mark.parametrize(
    "table_name, test_muid, initial_values, updated_values, verify_fields",
    [
        # Test case 1: Update Link with float values
        (
            "msm_Link",
            "set_values_test_float",
            {
                "Diameter": 2.5,
                "Description": "initial_data",
                "geometry": "LINESTRING (3 4, 10 50, 20 25)",
            },
            {
                "Diameter": 3.75,  # float
                "Description": "updated_data",
                "geometry": "LINESTRING (4 5, 20 60, 30 35)",
            },
            ["Diameter", "Description", "geometry"],
        ),
        # Test case 2: Update Link with integer values
        (
            "msm_Link",
            "set_values_test_int",
            {
                "Diameter": 2.0,
                "Enabled": 0,  # integer
            },
            {
                "Diameter": 2.5,
                "Enabled": 1,  # integer
            },
            ["Diameter", "Enabled"],
        ),
        # Test case 3: Update Link with string values
        (
            "msm_Link",
            "set_values_test_string",
            {
                "Description": "original description",
                "fromnodeid": "Node_1",  # string
                "tonodeid": "Node_2",  # string
            },
            {
                "Description": "Complex string with special chars: !@#$%^",
                "fromnodeid": "Updated_Node_1",  # string
                "tonodeid": "Updated_Node_2",  # string
            },
            ["Description", "fromnodeid", "tonodeid"],
        ),
        # Test case 4: Update Link with shapely LineString geometry
        (
            "msm_Link",
            "set_values_test_shapely",
            {
                "Diameter": 1.0,
                "Description": "initial geometry",
                "geometry": "LINESTRING (0 0, 10 10)",
            },
            {
                "Diameter": 1.5,
                "Description": "updated geometry",
                "geometry": LineString(
                    [(5, 5), (15, 15), (25, 5)]
                ),  # Shapely LineString
            },
            ["Diameter", "Description", "geometry"],
        ),
        # Test case 5: Update Project with datetime values
        (
            "msm_Project",
            "set_values_test_datetime",
            {
                "ComputationBegin": datetime(2023, 11, 1, 0, 0, 0, 0),
                "ComputationEnd": datetime(2023, 11, 1, 1, 0, 0, 0),
            },
            {
                "ComputationBegin": datetime(2023, 11, 1, 1, 0, 0, 0),
                "ComputationEnd": datetime(2023, 11, 1, 2, 0, 0, 0),
            },
            ["ComputationBegin", "ComputationEnd"],
        ),
    ],
)
def test_set_values(
    data_access: DataTableDemoAccess,
    table_name,
    test_muid,
    initial_values,
    updated_values,
    verify_fields,
):
    """Test updating multiple field values at once."""
    # First ensure test data doesn't exist
    muids = data_access.get_muid_where(table_name, f"MUID='{test_muid}'")
    if len(muids) == 1:
        data_access.delete(table_name, test_muid)

    # Insert initial data
    data_access.insert(table_name, test_muid, initial_values)

    # Update values
    data_access.set_values(table_name, test_muid, updated_values)

    # Verify updates
    values = data_access.get_field_values(table_name, test_muid, verify_fields)

    # Check that each field value matches what we updated
    for i, field in enumerate(verify_fields):
        expected = updated_values[field]
        actual = values[i]

        if isinstance(expected, LineString):
            actual_geom = wkt.loads(actual)
            assert actual_geom.equals(expected), (
                f"Field {field} expected {expected} but got {actual}"
            )
        else:
            assert actual == expected, (
                f"Field {field} expected {expected} but got {actual}"
            )

    # Clean up
    data_access.delete(table_name, test_muid)


@pytest.mark.parametrize(
    "table_name, test_muid, initial_values, field_to_update, new_value",
    [
        # Test case 1: Update a WKT geometry field (string format)
        (
            "msm_Link",
            "set_value_test_wkt",
            {
                "Diameter": 2.5,
                "Description": "initial_data",
                "geometry": "LINESTRING (3 4, 10 50, 20 25)",
            },
            "geometry",
            "LINESTRING (5 6, 30 70, 40 45)",  # WKT string
        ),
        # Test case 2: Update a string field
        (
            "msm_Link",
            "set_value_test_string",
            {
                "Diameter": 2.5,
                "Description": "initial_data",
            },
            "Description",
            "Complex string with special chars: !@#$%^",  # string
        ),
        # Test case 3: Update a float field
        (
            "msm_Link",
            "set_value_test_float",
            {
                "Diameter": 2.5,
                "Description": "initial_data",
            },
            "Diameter",
            3.75,  # float
        ),
        # Test case 4: Update a datetime field
        (
            "msm_Project",
            "set_value_test_datetime",
            {
                "ComputationBegin": datetime(2023, 11, 1, 0, 0, 0, 0),
                "ComputationEnd": datetime(2023, 11, 1, 1, 0, 0, 0),
            },
            "ComputationBegin",
            datetime(2023, 11, 1, 1, 0, 0, 0),
        ),
        # Test case 5: Update an integer field
        (
            "msm_Link",
            "set_value_test_int",
            {"Diameter": 2.5, "Description": "initial_data", "Enabled": 0},
            "Enabled",
            1,  # integer
        ),
        # Test case 6: Update geometry with Shapely LineString object
        (
            "msm_Link",
            "set_value_test_shapely",
            {
                "Diameter": 1.0,
                "Description": "shapely initial",
                "geometry": "LINESTRING (0 0, 10 10)",
            },
            "geometry",
            LineString([(10, 10), (20, 20), (30, 10)]),  # Shapely LineString
        ),
    ],
)
def test_set_value(
    data_access: DataTableDemoAccess,
    table_name,
    test_muid,
    initial_values,
    field_to_update,
    new_value,
):
    """Test updating a single field value."""
    # First ensure test data doesn't exist
    muids = data_access.get_muid_where(table_name, f"MUID='{test_muid}'")
    if len(muids) == 1:
        data_access.delete(table_name, test_muid)

    # Insert initial data
    data_access.insert(table_name, test_muid, initial_values)

    # Update a single value
    data_access.set_value(table_name, test_muid, field_to_update, new_value)

    # Verify update
    values = data_access.get_field_values(table_name, test_muid, [field_to_update])

    actual = values[0]

    if isinstance(new_value, LineString):
        actual_geom = wkt.loads(actual)
        assert actual_geom.equals(new_value), (
            f"Field {field_to_update} expected {new_value} but got {actual}"
        )
    else:
        assert actual == new_value, (
            f"Field {field_to_update} expected {new_value} but got {actual}"
        )

    # Clean up
    data_access.delete(table_name, test_muid)


def test_delete(data_access):
    """Test deleting a record from a table."""
    # First insert test data
    muids = data_access.get_muid_where("msm_Link", "MUID='link_test'")
    if len(muids) == 1:
        data_access.delete("msm_Link", "link_test")

    # Insert data to delete
    field_values = {
        "Diameter": 2.5,
        "Description": "to_be_deleted",
    }
    data_access.insert("msm_Link", "link_test", field_values)

    # Verify data exists
    muids = data_access.get_muid_where("msm_Link", "MUID='link_test'")
    assert len(muids) == 1

    # Delete the data
    data_access.delete("msm_Link", "link_test")

    # Verify deletion
    muids = data_access.get_muid_where("msm_Link", "MUID='link_test'")
    assert len(muids) == 0


def test_scenarios(data_access):
    """Test scenario management functionality."""
    # Test getting list of scenarios
    assert data_access.scenarios == ["Base", "sub_scenario"]

    # Test current active scenario
    assert data_access.active_scenario == "Base"
    assert data_access.get_field_values("msm_Link", "Link_2", "Length") == [20.0]

    # Test activating a different scenario
    data_access.activate_scenario("sub_scenario")
    assert data_access.active_scenario == "sub_scenario"
    assert data_access.get_field_values("msm_Link", "Link_2", "Length") == [24.0]

    # Test switching back to original scenario
    data_access.activate_scenario("Base")
    assert data_access.active_scenario == "Base"


def test_add_user_defined_column(data_access):
    data_access.add_user_defined_column("msm_Link", "test_column", "integer")

    # Should be None at first
    values = data_access.get_field_values("msm_Link", "Link_29", "test_column")
    assert values[0] is None

    # Set the value
    data_access.set_value("msm_Link", "Link_29", "test_column", 42)
    values = data_access.get_field_values("msm_Link", "Link_29", "test_column")
    assert values[0] == 42
