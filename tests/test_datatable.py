import pytest

import os
from mikeplus import DataTableDemoAccess
from datetime import datetime


def test_opendatabase():
    file_name = os.path.join("tests", "testdata", "Db", "Sirius", "Sirius.sqlite")
    data_access = DataTableDemoAccess(file_name)
    data_access.open_database()
    assert data_access.is_database_open() is True
    data_access.close_database()


# parameterize this test for different table name, MUIDs, fields, and expected values
@pytest.mark.parametrize(
    "table_name, muid, fields, expected_values",
    [
        ("msm_Link", "Link_30", "Length", [4.06]),
        ("msm_Link", "Link_30", ["Length", "Diameter"], [4.06, 1.0]),
    ],
)
def test_get_field_values(table_name, muid, fields, expected_values):
    file_name = os.path.join("tests", "testdata", "Db", "Sirius", "Sirius.sqlite")
    data_access = DataTableDemoAccess(file_name)
    data_access.open_database()
    values = data_access.get_field_values(table_name, muid, fields)
    assert values == expected_values
    data_access.close_database()


def test_manipulate_data():
    file_name = os.path.join("tests", "testdata", "Db", "Sirius", "Sirius.sqlite")
    data_access = DataTableDemoAccess(file_name)
    data_access.open_database()
    muids = data_access.get_muid_where("msm_Link", "MUID='link_test'")
    if len(muids) == 1:
        data_access.delete("msm_Link", "link_test")
    field_values = {
        "Diameter": 2.5,
        "Description": "setvalues",
        "geometry": "LINESTRING (3 4, 10 50, 20 25)",
    }
    data_access.insert("msm_Link", "link_test", field_values)
    muids = data_access.get_muid_where("msm_Link", "MUID='link_test'")
    assert len(muids) == 1
    fields = ["Diameter", "Description", "geometry"]
    values_get = data_access.get_field_values("msm_Link", "link_test", fields)
    assert values_get[0] == 2.5
    assert values_get[1] == "setvalues"
    assert values_get[2] == "LINESTRING (3 4, 10 50, 20 25)"
    field_values = {
        "Diameter": 1.0,
        "Description": "Desc",
        "geometry": "LINESTRING (4 5, 20 60, 30 35)",
    }
    data_access.set_values("msm_Link", "link_test", field_values)
    values_get = data_access.get_field_values("msm_Link", "link_test", fields)
    assert values_get[0] == 1.0
    assert values_get[1] == "Desc"
    assert values_get[2] == "LINESTRING (4 5, 20 60, 30 35)"
    data_access.set_value(
        "msm_Link", "link_test", "geometry", "LINESTRING (5 6, 30 70, 40 45)"
    )
    fields = ["geometry"]
    values_get = data_access.get_field_values("msm_Link", "link_test", fields)
    assert values_get[0] == "LINESTRING (5 6, 30 70, 40 45)"
    data_access.delete("msm_Link", "link_test")
    muids = data_access.get_muid_where("msm_Link", "MUID='link_test'")
    assert len(muids) == 0
    field_values = {
        "ComputationBegin": datetime(2023, 11, 1, 0, 0, 0, 0),
        "ComputationEnd": datetime(2023, 11, 1, 1, 0, 0, 0),
    }
    data_access.insert("msm_Project", "sim_test", field_values)
    fields = ["ComputationBegin", "ComputationEnd"]
    values_get = data_access.get_field_values("msm_Project", "sim_test", fields)
    assert values_get[0] == datetime(2023, 11, 1, 0, 0, 0, 0)
    assert values_get[1] == datetime(2023, 11, 1, 1, 0, 0, 0)
    field_values = {
        "ComputationBegin": datetime(2023, 11, 1, 1, 0, 0, 0),
        "ComputationEnd": datetime(2023, 11, 1, 2, 0, 0, 0),
    }
    data_access.set_values("msm_Project", "sim_test", field_values)
    values_get = data_access.get_field_values("msm_Project", "sim_test", fields)
    assert values_get[0] == datetime(2023, 11, 1, 1, 0, 0, 0)
    assert values_get[1] == datetime(2023, 11, 1, 2, 0, 0, 0)
    data_access.delete("msm_Project", "sim_test")
    data_access.close_database()


def test_shapely_geometry():
    from shapely.geometry import LineString

    file_name = os.path.join("tests", "testdata", "Db", "Sirius", "Sirius.sqlite")
    data_access = DataTableDemoAccess(file_name)
    data_access.open_database()
    muids = data_access.get_muid_where("msm_Link", "MUID='link_test'")
    if len(muids) == 1:
        data_access.delete("msm_Link", "link_test")
    line = LineString([(0, 0), (10, 10)])
    values = {"geometry": line}
    data_access.insert("msm_Link", "link_shp_test", values)
    fields = ["geometry"]
    values = data_access.get_field_values("msm_Link", "link_shp_test", fields)
    assert values[0] == "LINESTRING (0 0, 10 10)"
    line = LineString([(10, 10), (20, 20)])
    data_access.set_value("msm_Link", "link_shp_test", "geometry", line)
    values = data_access.get_field_values("msm_Link", "link_shp_test", fields)
    assert values[0] == "LINESTRING (10 10, 20 20)"
    data_access.delete("msm_Link", "link_shp_test")
    data_access.close_database()
