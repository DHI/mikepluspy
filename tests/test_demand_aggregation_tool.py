from __future__ import annotations

import pytest

from mikeplus import Database, DatabaseError
from mikeplus.tools import DemandAggregationTool

from conftest import (
    EPANET_DEMO_DB,
    copy_database_folder,
    create_test_specific_db_copy,
)

pytestmark = pytest.mark.license_required

ALLOCATED = 3  # mw_MDemand.GenerateTypeNo for rows written by the tool
MANUAL = 1

# MUID: (junction, pipe, demand, category, pattern)
ALLOCATIONS = {
    "A1": ("Junction_1", "Pipe_2", 1.0, "Dom", "PPattern_1"),
    "A2": ("Junction_1", "Pipe_2", 2.0, "Dom", "PPattern_1"),
    "A3": ("Junction_1", "Pipe_3", 4.0, "Ind", None),
    "A4": ("Junction_2", "Pipe_3", 8.0, "Dom", "PPattern_1"),
    "A5": (None, "Pipe_4", 16.0, "Dom", None),
}


@pytest.fixture(scope="module")
def prepared_db(tmp_path_factory):
    """Epanet_Demo with the allocations added, opened once.

    The first open of a copied test database is slow, a reopen is fast, so
    each test copies this one.
    """
    path = copy_database_folder(
        EPANET_DEMO_DB, tmp_path_factory.mktemp("demand_aggregation") / "db"
    )
    with Database(path) as db:
        for muid, (junction, pipe, demand, category, pattern) in ALLOCATIONS.items():
            db.tables.mw_DemAlloc.insert(
                {
                    "MUID": muid,
                    "JunctionID": junction,
                    "PipeID": pipe,
                    "Demand": demand,
                    "Dem_category": category,
                    "Pattern": pattern,
                }
            )
    return path


@pytest.fixture
def db(prepared_db, tmp_path):
    db = Database(create_test_specific_db_copy(prepared_db, tmp_path, "demand"))
    yield db
    if db.is_open:
        db.close()


def demands(db, generate_type=ALLOCATED):
    """Return the junction demands of one origin as sorted tuples."""
    df = db.tables.mw_MDemand.select(
        ["JunctionID", "Demand", "Category", "PatternID", "GenerateTypeNo"]
    ).to_pandas()
    df = df[df["GenerateTypeNo"] == generate_type]
    return sorted(
        (row.JunctionID, row.Demand, row.Category, row.PatternID)
        for row in df.itertuples()
    )


def test_aggregate_to_node_demands_keeps_categories(db):
    manual = demands(db, MANUAL)
    assert len(manual) == 7

    DemandAggregationTool(db).aggregate_to_node_demands()

    assert demands(db) == [
        ("Junction_1", 3.0, "Dom", "PPattern_1"),
        ("Junction_1", 4.0, "Ind", None),
        ("Junction_2", 8.0, "Dom", "PPattern_1"),
    ]
    assert demands(db, MANUAL) == manual


def test_aggregate_to_node_demands_with_one_category(db):
    DemandAggregationTool(db).aggregate_to_node_demands(
        ["A1", "A3", "A5"], keep_categories=False, category="Total", pattern="P"
    )

    assert demands(db) == [("Junction_1", 5.0, "Total", "P")]


def test_reset_existing_replaces_only_aggregated_demands(db):
    manual = demands(db, MANUAL)
    tool = DemandAggregationTool(db)
    tool.aggregate_to_node_demands(["A4"])

    tool.aggregate_to_node_demands(["A1"])
    assert len(demands(db)) == 2

    tool.aggregate_to_node_demands(["A1"], reset_existing=True)
    assert demands(db) == [("Junction_1", 1.0, "Dom", "PPattern_1")]
    assert demands(db, MANUAL) == manual


def test_category_without_keep_categories_false_raises(db):
    with pytest.raises(ValueError, match="keep_categories"):
        DemandAggregationTool(db).aggregate_to_node_demands(category="Total")


def test_assign_to_multiple_demands(db):
    DemandAggregationTool(db).assign_to_multiple_demands()

    assert demands(db) == [
        ("Junction_1", 1.0, "Dom", "PPattern_1"),
        ("Junction_1", 2.0, "Dom", "PPattern_1"),
        ("Junction_1", 4.0, "Ind", None),
        ("Junction_2", 8.0, "Dom", "PPattern_1"),
    ]


def test_assign_to_multiple_demands_selected(db):
    DemandAggregationTool(db).assign_to_multiple_demands(["A2", "A4"])

    assert demands(db) == [
        ("Junction_1", 2.0, "Dom", "PPattern_1"),
        ("Junction_2", 8.0, "Dom", "PPattern_1"),
    ]


def pipe_coefficients(db, field):
    df = db.tables.mw_Pipe.select([field]).to_pandas()
    return df[field].where(df[field].notna(), None).to_dict()


def test_aggregate_to_pipe_coefficients(db):
    DemandAggregationTool(db).aggregate_to_pipe_coefficients(coefficient=2)

    coefficients = pipe_coefficients(db, "Coeff2")
    assert coefficients["Pipe_2"] == pytest.approx(3.0)
    assert coefficients["Pipe_3"] == pytest.approx(12.0)
    assert coefficients["Pipe_4"] == pytest.approx(16.0)
    assert coefficients["Pipe_1"] is None
    assert all(value is None for value in pipe_coefficients(db, "Coeff1").values())


def test_aggregate_to_pipe_coefficients_reset_existing(db):
    db.tables.mw_Pipe.update({"Coeff1": 99.0}).all().execute()

    DemandAggregationTool(db).aggregate_to_pipe_coefficients(
        ["A3"], reset_existing=True
    )

    coefficients = pipe_coefficients(db, "Coeff1")
    assert coefficients["Pipe_3"] == pytest.approx(4.0)
    assert coefficients["Pipe_2"] == 0.0
    assert coefficients["Pipe_1"] == 0.0


@pytest.mark.parametrize("coefficient", [0, 5])
def test_aggregate_to_pipe_coefficients_rejects_unknown_coefficient(db, coefficient):
    with pytest.raises(ValueError, match="coefficient"):
        DemandAggregationTool(db).aggregate_to_pipe_coefficients(
            coefficient=coefficient
        )


def test_aggregate_null_demand_gives_null(db):
    db.tables.mw_DemAlloc.insert(
        {"MUID": "N", "JunctionID": "Junction_2", "PipeID": "Pipe_3", "Demand": None}
    )
    tool = DemandAggregationTool(db)

    tool.aggregate_to_node_demands(["A4", "N"], keep_categories=False)
    tool.aggregate_to_pipe_coefficients(["A4", "N"])

    assert demands(db) == [("Junction_2", None, None, None)]
    assert pipe_coefficients(db, "Coeff1")["Pipe_3"] is None


def test_empty_list_does_nothing(db):
    db.tables.mw_Pipe.update({"Coeff1": 99.0}).all().execute()
    tool = DemandAggregationTool(db)
    tool.aggregate_to_node_demands(["A1"])
    before = demands(db)

    tool.aggregate_to_node_demands([], reset_existing=True)
    tool.assign_to_multiple_demands([], reset_existing=True)
    tool.aggregate_to_pipe_coefficients([], reset_existing=True)

    assert demands(db) == before
    assert set(pipe_coefficients(db, "Coeff1").values()) == {99.0}


def test_empty_demand_allocation_table(db):
    db.tables.mw_DemAlloc.delete().all().execute()
    tool = DemandAggregationTool(db)

    tool.aggregate_to_node_demands(reset_existing=True)
    tool.assign_to_multiple_demands(reset_existing=True)
    tool.aggregate_to_pipe_coefficients(reset_existing=True)

    assert demands(db) == []


def test_str_demand_allocations_raises(db):
    with pytest.raises(TypeError, match="not a str"):
        DemandAggregationTool(db).aggregate_to_node_demands("A1")


def test_non_str_demand_allocation_raises(db):
    with pytest.raises(TypeError, match="str MUIDs"):
        DemandAggregationTool(db).aggregate_to_node_demands(["A1", 1])


def test_unknown_demand_allocation_raises(db):
    with pytest.raises(ValueError, match="'Nope'"):
        DemandAggregationTool(db).aggregate_to_pipe_coefficients(["A1", "Nope"])


# The rolled-back `None` result is not covered: no public input found makes
# MIKE+ return it (bad input gives an exception or a Skipped status).
def test_failure_raises_database_error(db):
    tool = DemandAggregationTool(db)
    db.close()

    with pytest.raises(DatabaseError, match="aggregate demands to junctions"):
        tool.aggregate_to_node_demands()
