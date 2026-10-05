from __future__ import annotations

import shutil

import pytest

from mikeplus import Database, DatabaseError
from mikeplus.tools import DemandConnectionTool

pytestmark = pytest.mark.license_required

# Epanet_Demo has no demand allocations, so each test places its own next to
# known features: Junction_1 is at (-4420, 1626.67), Pipe_3 runs from
# Junction_2 (-3260, 1693.33) to Junction_3 (-1713.33, 1573.33), and Pipe_5
# ends at Junction_5 (-820, 693.33). The demand allocation named "Pipe_5" is the
# only one "junction_by_pipe_id" can connect.
DEMANDS = {
    "NearJ1": "POINT (-4410 1626.666667)",
    "NearPipe3": "POINT (-2486.666667 1653.333333)",
    "Pipe_5": "POINT (-1000 700)",
    "Far": "POINT (20000 20000)",
}


@pytest.fixture(scope="module")
def prepared_db(module_epanet_demo_db):
    # Opening a fresh copy of Epanet_Demo takes about 20 s, and a copy of one
    # already opened about 1 s, so tests copy this one.
    db = Database(module_epanet_demo_db)
    for muid, point in DEMANDS.items():
        db.tables.mw_DemAlloc.insert({"MUID": muid, "geometry": point})
    db.close()
    return module_epanet_demo_db


def open_copy(prepared_db, target_dir):
    shutil.copytree(prepared_db.parent, target_dir)
    return Database(target_dir / prepared_db.name)


@pytest.fixture(scope="module")
def shared_db(prepared_db, tmp_path_factory):
    db = open_copy(prepared_db, tmp_path_factory.mktemp("shared") / "db")
    yield db
    db.close()


@pytest.fixture
def db(prepared_db, tmp_path):
    db = open_copy(prepared_db, tmp_path / "db")
    yield db
    db.close()


def connections(db) -> dict[str, tuple]:
    rows = db.tables.mw_DemAlloc.select(
        ["ConnectionTypeNo", "JunctionID", "PipeID"]
    ).execute()
    return {
        muid: (int(type_no), junction or None, pipe or None)
        for muid, (type_no, junction, pipe) in rows.items()
    }


def connection_lines(db) -> dict[str, str]:
    rows = db.tables.mw_DemAllocConn.select(["DemAllocID", "LocationID"]).execute()
    return {demand: location for demand, location in rows.values()}


def test_nearest_junction(db):
    DemandConnectionTool(db).run("nearest_junction")

    result = connections(db)
    assert result["NearJ1"] == (1, "Junction_1", None)
    assert result["NearPipe3"] == (1, "Junction_7", None)
    assert result["Pipe_5"] == (1, "Junction_5", None)
    assert result["Far"][1] == "Junction_6"
    assert connection_lines(db) == {
        "NearJ1": "Junction_1",
        "NearPipe3": "Junction_7",
        "Pipe_5": "Junction_5",
        "Far": "Junction_6",
    }


def test_nearest_pipe(db):
    DemandConnectionTool(db).run("nearest_pipe", max_distance=100.0)

    result = connections(db)
    assert result["NearJ1"] == (2, None, "Pipe_2")
    assert result["NearPipe3"] == (2, None, "Pipe_3")
    assert result["Pipe_5"] == (2, None, "Pipe_5")
    assert result["Far"] == (1, None, None)
    assert connection_lines(db) == {
        "NearJ1": "Pipe_2",
        "NearPipe3": "Pipe_3",
        "Pipe_5": "Pipe_5",
    }


def test_junction_by_nearest_pipe(db):
    DemandConnectionTool(db).run("junction_by_nearest_pipe", demand_ids=["NearPipe3"])

    # Junction_7 is nearer, but the nearest pipe is Pipe_3.
    assert connections(db)["NearPipe3"] == (1, "Junction_2", None)
    assert connection_lines(db) == {"NearPipe3": "Junction_2"}


def test_junction_by_pipe_id(db):
    DemandConnectionTool(db).run("junction_by_pipe_id")

    assert connection_lines(db) == {"Pipe_5": "Junction_5"}


def test_junction_by_pipe_id_where_formats_pipe_muid(db):
    tool = DemandConnectionTool(db)
    tool.run("junction_by_pipe_id", where="MUID <> '{0}'")
    assert connection_lines(db) == {}

    tool.run("junction_by_pipe_id", where="MUID = '{0}'")
    assert connection_lines(db) == {"Pipe_5": "Junction_5"}


def test_max_distance_limits_and_clears_connections(db):
    tool = DemandConnectionTool(db)
    tool.run("nearest_junction")
    tool.run("nearest_junction", max_distance=50.0)

    assert connection_lines(db) == {"NearJ1": "Junction_1"}
    assert connections(db)["NearPipe3"] == (1, None, None)


def test_nearest_pipe_rerun_clears_pipes_out_of_reach(db):
    tool = DemandConnectionTool(db)
    tool.run("nearest_pipe")
    assert connections(db)["Far"][2] is not None

    tool.run("nearest_pipe", max_distance=100.0)

    assert connections(db)["Far"] == (1, None, None)
    assert "Far" not in connection_lines(db)


def test_switching_method_clears_the_other_field(db):
    tool = DemandConnectionTool(db)
    tool.run("nearest_pipe")
    tool.run("nearest_junction", demand_ids=["NearJ1", "NearPipe3"])

    result = connections(db)
    assert result["NearJ1"] == (1, "Junction_1", None)
    assert result["NearPipe3"] == (1, "Junction_7", None)
    assert result["Pipe_5"] == (2, None, "Pipe_5")

    tool.run("nearest_pipe", demand_ids=["NearJ1"])

    assert connections(db)["NearJ1"] == (2, None, "Pipe_2")


def test_junction_by_pipe_id_leaves_skipped_demands(db):
    tool = DemandConnectionTool(db)
    tool.run("nearest_pipe", max_distance=100.0)
    tool.run("junction_by_pipe_id")

    result = connections(db)
    assert result["Pipe_5"] == (1, "Junction_5", None)
    assert result["NearJ1"] == (2, None, "Pipe_2")


def test_max_diameter_excludes_larger_pipes(db):
    db.tables.mw_Pipe.update({"Diameter": 300.0}).by_muid("Pipe_3").execute()

    DemandConnectionTool(db).run(
        "nearest_pipe", demand_ids=["NearPipe3"], max_diameter=250.0
    )

    assert connection_lines(db) == {"NearPipe3": "Pipe_7"}


def test_target_restrictions(db):
    tool = DemandConnectionTool(db)
    tool.run("nearest_junction", demand_ids=["NearJ1"], junction_ids=["Junction_5"])
    assert connection_lines(db) == {"NearJ1": "Junction_5"}

    tool.run("nearest_junction", demand_ids=["NearJ1"], where="MUID <> 'Junction_1'")
    assert connection_lines(db) == {"NearJ1": "Junction_2"}


def test_empty_demand_ids_connects_none(shared_db):
    DemandConnectionTool(shared_db).run("nearest_junction", demand_ids=[])

    assert connection_lines(shared_db) == {}


@pytest.mark.parametrize(
    "kwargs",
    [
        {"method": "nearest_node"},
        {"max_distance": 0.0},
        {"max_distance": float("nan")},
        {"max_distance": float("inf")},
        {"max_diameter": -1.0},
        {"junction_ids": []},
        {"junction_ids": ["Junction_1", "NoSuchJunction"]},
        {"method": "nearest_pipe", "pipe_ids": []},
        {"method": "nearest_pipe", "pipe_ids": ["Pipe_1", "NoSuchPipe"]},
        {"demand_ids": ["NearJ1", "NoSuchDemand"]},
        {"method": "junction_by_pipe_id", "max_distance": 10.0},
        {"method": "nearest_junction", "max_diameter": 10.0},
        {"method": "nearest_junction", "pipe_ids": ["Pipe_1"]},
        {"method": "nearest_pipe", "junction_ids": ["Junction_1"]},
        {"method": "junction_by_pipe_id", "pipe_ids": ["Pipe_1"]},
    ],
)
def test_invalid_arguments_raise_before_writing(shared_db, kwargs):
    with pytest.raises(ValueError):
        DemandConnectionTool(shared_db).run(**kwargs)

    assert connection_lines(shared_db) == {}


@pytest.mark.parametrize(
    "kwargs",
    [
        {"demand_ids": "NearJ1"},
        {"junction_ids": "Junction_1"},
        {"method": "nearest_pipe", "pipe_ids": "Pipe_1"},
    ],
)
def test_string_ids_raise_type_error(shared_db, kwargs):
    with pytest.raises(TypeError):
        DemandConnectionTool(shared_db).run(**kwargs)

    assert connection_lines(shared_db) == {}


def test_engine_error_raises_database_error(shared_db):
    # MIKE+ formats `where` with the pipe MUID, so a lone brace is invalid.
    with pytest.raises(DatabaseError):
        DemandConnectionTool(shared_db).run("junction_by_pipe_id", where="MUID = '{'")
