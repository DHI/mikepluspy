from __future__ import annotations

import pytest

from mikeplus import Database
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


@pytest.fixture
def db(epanet_demo_db):
    db = Database(epanet_demo_db)
    for muid, point in DEMANDS.items():
        db.tables.mw_DemAlloc.insert({"MUID": muid, "geometry": point})
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
    assert result["Far"][2] is None
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


def test_max_distance_limits_and_clears_connections(db):
    tool = DemandConnectionTool(db)
    tool.run("nearest_junction")
    tool.run("nearest_junction", max_distance=50.0)

    assert connection_lines(db) == {"NearJ1": "Junction_1"}
    assert connections(db)["NearPipe3"][1] is None


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


def test_empty_demand_ids_connects_none(db):
    DemandConnectionTool(db).run("nearest_junction", demand_ids=[])

    assert connection_lines(db) == {}


def test_invalid_arguments_raise_before_writing(db):
    tool = DemandConnectionTool(db)
    for kwargs in [
        {"method": "nearest_node"},
        {"max_distance": 0.0},
        {"max_diameter": -1.0},
        {"junction_ids": []},
        {"pipe_ids": []},
        {"demand_ids": ["NearJ1", "NoSuchDemand"]},
    ]:
        with pytest.raises(ValueError):
            tool.run(**kwargs)

    assert connection_lines(db) == {}
