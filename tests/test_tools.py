from __future__ import annotations

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

    assert os.path.exists(catch_slope_len_db), (
        f"Database file does not exist: {catch_slope_len_db}"
    )
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
