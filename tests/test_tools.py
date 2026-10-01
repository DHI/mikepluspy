from __future__ import annotations

import numpy as np
import pytest

import os
from mikeplus import Database
from mikeplus.tools.topology_repair_tool import TopoRepairTool
from mikeplus.tools.interpolation_tool import InterpolationTool
from mikeplus.tools.connection_repair_tool import ConnectionRepairTool
from mikeplus.tools.catch_slope_length_process_tool import CathSlopeLengthProcess
from mikeplus.tools.import_tool import ImportTool


def test_topology_repair_tool(repair_tool_db):
    db = Database(repair_tool_db)
    repair_tool = TopoRepairTool(db)
    repair_tool.run()
    query = db.tables.msm_Link.select(["MUID"]).where("muid='LinkToDel'")
    assert len(query.execute()) == 0

    query = db.tables.msm_Node.select(["MUID"]).where("muid='NodeIsolate'")
    assert len(query.execute()) == 0

    query = db.tables.msm_Link.select(["MUID"]).where("muid='LinkToSplit'")
    assert len(query.execute()) == 0

    query = db.tables.msm_Link.select(["MUID"]).where("tonodeid='NodeToSplit'")
    assert len(query.execute()) == 2

    query = db.tables.msm_Link.select(["MUID"]).where("fromnodeid='NodeToSplit'")
    assert len(query.execute()) == 1

    query = db.tables.msm_Node.select(["MUID"]).where("muid='Node_8'")
    assert len(query.execute()) == 1
    db.close()


def test_interpolate_tool(interpolate_db):
    """Test interpolating a field from a source layer."""
    db = Database(interpolate_db)
    db.tables.msm_Node.update({"Diameter": None}).where("MUID='Node_1'").execute()
    db.tables.msm_Node.update({"Diameter": None}).where("MUID='Node_2'").execute()
    db.tables.msm_Node.update({"Diameter": None}).where("MUID='Node_3'").execute()
    tool = InterpolationTool(db)
    tool.interpolate_from_nearest_feature(
        "msm_Node", "Diameter", "msm_Link", "Diameter"
    )
    field_val_get = db.tables.msm_Node.select(["Diameter"]).execute()
    db.close()
    assert field_val_get["Node_1"][0] == 2.0
    assert field_val_get["Node_2"][0] == 2.0
    assert field_val_get["Node_3"][0] == 3.0


def test_direct_assign_value_treats_value_as_missing(interpolate_db):
    db = Database(interpolate_db)
    db.tables.msm_Node.update({"Diameter": -999.0}).where("MUID='Node_1'").execute()
    db.tables.msm_Node.update({"Diameter": 1.5}).where("MUID='Node_2'").execute()
    InterpolationTool(db).direct_assign_value(
        "msm_Node", "Diameter", 5.0, assign_val_as_missing=True, value_as_missing=-999.0
    )
    field_val_get = db.tables.msm_Node.select(["Diameter"]).execute()
    db.close()
    assert field_val_get["Node_1"][0] == 5.0
    assert field_val_get["Node_2"][0] == 1.5


def test_interpolate_from_neighbour_along_path(interpolate_db):
    """`alongPath` reaches the engine: the two assignment methods give different values."""
    db = Database(interpolate_db)
    tool = InterpolationTool(db)
    diameters = {}
    for along_path in (False, True):
        db.tables.msm_Node.update({"Diameter": None}).where("MUID='Node_2'").execute()
        tool.interpolate_from_neighobour(
            "msm_Node", "Diameter", "msm_Node", "Diameter", alongPath=along_path
        )
        row = db.tables.msm_Node.select(["Diameter"]).by_muid("Node_2").execute()
        diameters[along_path] = row["Node_2"][0]
    db.close()
    assert diameters[False] == pytest.approx(2.0)
    assert diameters[True] is not None
    assert diameters[True] != pytest.approx(diameters[False])


def test_interpolate_from_dem_only_given_muids(catch_slope_len_db):
    db = Database(catch_slope_len_db)
    before = db.tables.msm_Node.select(["GroundLevel"]).execute()
    selected = ["OL_001", "OL_003"]
    InterpolationTool(db).interpolate_from_DEM(
        "msm_Node",
        "GroundLevel",
        str(catch_slope_len_db.parent / "dem.dfs2"),
        1,
        only_null_values=False,
        muids=selected,
    )
    after = db.tables.msm_Node.select(["GroundLevel"]).execute()
    db.close()
    assert after["OL_001"][0] == pytest.approx(6.58, abs=0.01)
    assert after["OL_003"][0] == pytest.approx(66.36, abs=0.01)
    unchanged = {muid: value for muid, value in after.items() if muid not in selected}
    assert unchanged == {muid: value for muid, value in before.items() if muid not in selected}


def test_direct_assign_value_only_given_muids(interpolate_db):
    db = Database(interpolate_db)
    before = db.tables.msm_Node.select(["Diameter"]).execute()
    InterpolationTool(db).direct_assign_value(
        "msm_Node", "Diameter", 7.0, only_null_values=False, muids=iter(["Node_2"])
    )
    after = db.tables.msm_Node.select(["Diameter"]).execute()
    db.close()
    assert after["Node_2"][0] == 7.0
    assert {k: v for k, v in after.items() if k != "Node_2"} == {
        k: v for k, v in before.items() if k != "Node_2"
    }


def _null_node_diameters(db):
    for muid in ("Node_1", "Node_2", "Node_3"):
        db.tables.msm_Node.update({"Diameter": None}).where(f"MUID='{muid}'").execute()


@pytest.mark.parametrize(
    "method", ["interpolate_from_nearest_feature", "interpolation_IDW"]
)
def test_interpolate_from_source_layer_only_given_muids(interpolate_db, method):
    db = Database(interpolate_db)
    _null_node_diameters(db)
    getattr(InterpolationTool(db), method)(
        "msm_Node", "Diameter", "msm_Link", "Diameter", muids=["Node_1"]
    )
    after = db.tables.msm_Node.select(["Diameter"]).execute()
    db.close()
    assert after["Node_1"][0] is not None
    assert after["Node_2"][0] is None
    assert after["Node_3"][0] is None


def test_interpolation_empty_muids_assigns_nothing(interpolate_db):
    db = Database(interpolate_db)
    before = db.tables.msm_Node.select(["Diameter"]).execute()
    InterpolationTool(db).direct_assign_value(
        "msm_Node", "Diameter", 7.0, only_null_values=False, muids=[]
    )
    after = db.tables.msm_Node.select(["Diameter"]).execute()
    db.close()
    assert after == before


def test_interpolation_accepts_numpy_muids(interpolate_db):
    db = Database(interpolate_db)
    _null_node_diameters(db)
    InterpolationTool(db).direct_assign_value(
        "msm_Node", "Diameter", 7.0, muids=np.array(["Node_1", "Node_3"])
    )
    after = db.tables.msm_Node.select(["Diameter"]).execute()
    db.close()
    assert after["Node_1"][0] == 7.0
    assert after["Node_2"][0] is None
    assert after["Node_3"][0] == 7.0


def test_interpolation_muids_rejects_single_string(module_interpolate_db):
    db = Database(module_interpolate_db)
    try:
        with pytest.raises(TypeError, match="muids"):
            InterpolationTool(db).direct_assign_value(
                "msm_Node", "Diameter", 7.0, muids="Node_2"
            )
    finally:
        db.close()


def test_connect_repair_tool(connection_repair_db):
    db = Database(connection_repair_db)

    db.tables.m_StationCon.delete().all().execute()
    db.tables.msm_LoadPointConnection.delete().all().execute()

    muids = db.tables.m_StationCon.get_muids()
    assert len(muids) == 0

    muids = db.tables.msm_LoadPointConnection.get_muids()
    assert len(muids) == 0

    conn_repair_tool = ConnectionRepairTool(db)
    conn_repair_tool.run()

    muids = db.tables.m_StationCon.get_muids()
    assert len(muids) == 2

    muids = db.tables.msm_LoadPointConnection.get_muids()
    assert len(muids) == 2
    db.close()


def test_catch_slope_len_tool(catch_slope_len_db):
    db = Database(catch_slope_len_db)

    field_values = {"ModelBSlope": 0.0, "ModelBLength": 0.0}
    fields = ["ModelBSlope", "ModelBLength"]
    muid = "imp3"

    db.tables.msm_Catchment.update(field_values).by_muid(muid).execute()

    field_val_get = db.tables.msm_Catchment.select(fields).by_muid(muid).execute()

    assert field_val_get[muid][0] == 0.0
    assert field_val_get[muid][1] == 0.0

    # Get the paths to the files in the temporary directory
    db_dir = os.path.dirname(catch_slope_len_db)
    shp_file = os.path.join(db_dir, "Catch_Slope.shp")
    dem_file = os.path.join(db_dir, "dem.dfs2")

    assert os.path.exists(
        catch_slope_len_db
    ), f"Database file does not exist: {catch_slope_len_db}"
    assert os.path.exists(shp_file), "Catch_Slope.shp does not exist"
    assert os.path.exists(dem_file), "dem.dfs2 does not exist"

    tool = CathSlopeLengthProcess(db)
    tool.run(
        [muid],
        shp_file,
        dem_file,
        0,
    )

    field_val_get = db.tables.msm_Catchment.select(fields).by_muid(muid).execute()

    assert field_val_get[muid][0] == pytest.approx(0.102342, abs=1e-6)
    assert field_val_get[muid][1] == pytest.approx(172.571601, abs=1e-6)

    db.close()


# TODO: Fix this - something not so great going on
@pytest.mark.license_required
@pytest.mark.xfail(reason="Passes locally on re-run, but not on full run or CI")
def test_import_tool(import_db):
    db = Database(import_db)

    db.tables.msm_Link.delete().all().execute()
    muids = db.tables.msm_Link.get_muids()
    assert len(muids) == 0

    # Get the path to the config file in the temporary directory
    db_dir = os.path.dirname(import_db)
    config_file = os.path.join(db_dir, "config.xml")

    import_tool = ImportTool(config_file, db)
    import_tool.run()
    muids = db.tables.msm_Link.get_muids()
    assert len(muids) == 575
    db.close()
