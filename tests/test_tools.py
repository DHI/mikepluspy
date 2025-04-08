from __future__ import annotations

import pytest

import os
from mikeplus import DataTableDemoAccess
from mikeplus import DataTableAccess
from mikeplus.tools.topology_repair_tool import TopoRepairTool
from mikeplus.tools.interpolation_tool import InterpolationTool
from mikeplus.tools.connection_repair_tool import ConnectionRepairTool
from mikeplus.tools.catch_slope_length_process_tool import CathSlopeLengthProcess
from mikeplus.tools.import_tool import ImportTool


def test_topology_repair_tool(repair_tool_db):
    data_access = DataTableDemoAccess(repair_tool_db)
    data_access.open_database()
    repair_tool = TopoRepairTool(data_access.datatables)
    repair_tool.run()
    query = data_access.get_muid_where("msm_Link", "muid='LinkToDel'")
    assert len(query) == 0
    query = data_access.get_muid_where("msm_Node", "muid='NodeIsolate'")
    assert len(query) == 0
    query = data_access.get_muid_where("msm_Link", "muid='LinkToSplit'")
    assert len(query) == 0
    query = data_access.get_muid_where("msm_Link", "tonodeid='NodeToSplit'")
    assert len(query) == 2
    query = data_access.get_muid_where("msm_Link", "fromnodeid='NodeToSplit'")
    assert len(query) == 1
    query = data_access.get_muid_where("msm_Node", "muid='Node_8'")
    assert len(query) == 1
    data_access.close_database()


def test_interpolate_tool(interpolate_db):
    data_access = DataTableDemoAccess(interpolate_db)
    data_access.open_database()
    data_access.set_value("msm_Node", "Node_1", "Diameter", None)
    data_access.set_value("msm_Node", "Node_2", "Diameter", None)
    data_access.set_value("msm_Node", "Node_3", "Diameter", None)
    tool = InterpolationTool(data_access.datatables)
    tool.interpolate_from_nearest_feature(
        "msm_Node", "Diameter", "msm_Link", "Diameter"
    )
    fields = ["Diameter"]
    field_val_get = data_access.get_muid_field_values("msm_Node", fields)
    data_access.close_database()
    assert field_val_get["Node_1"][0] == 2.0
    assert field_val_get["Node_2"][0] == 2.0
    assert field_val_get["Node_3"][0] == 3.0


def test_connect_repair_tool(connection_repair_db):
    data_access = DataTableDemoAccess(connection_repair_db)
    data_access.open_database()
    muids = data_access.get_muid_where("m_StationCon")
    for muid in muids:
        data_access.delete("m_StationCon", muid)
    muids = data_access.get_muid_where("msm_LoadPointConnection")
    for muid in muids:
        data_access.delete("msm_LoadPointConnection", muid)
    conn_repair_tool = ConnectionRepairTool(data_access.datatables)
    conn_repair_tool.run()
    station_conn = data_access.get_muid_where("m_StationCon")
    assert len(station_conn) == 2
    load_point_conn = data_access.get_muid_where("msm_LoadPointConnection")
    assert len(load_point_conn) == 2
    data_access.close_database()


def test_catch_slope_len_tool(catch_slope_len_db):
    data_access = DataTableDemoAccess(catch_slope_len_db)
    data_access.open_database()
    field_values = {"ModelBSlope": 0.0, "ModelBLength": 0.0}
    fields = ["ModelBSlope", "ModelBLength"]
    muid = "imp3"
    data_access.set_values("msm_Catchment", muid, field_values)
    field_val_get = data_access.get_field_values("msm_Catchment", muid, fields)
    assert field_val_get[0] == 0.0
    assert field_val_get[1] == 0.0
    catch_ids = [muid]

    # Get the paths to the files in the temporary directory
    db_dir = os.path.dirname(catch_slope_len_db)
    shp_file = os.path.join(db_dir, "Catch_Slope.shp")
    dem_file = os.path.join(db_dir, "dem.dfs2")

    tool = CathSlopeLengthProcess(data_access.datatables)
    tool.run(
        catch_ids,
        shp_file,
        dem_file,
        0,
    )
    field_val_get = data_access.get_field_values("msm_Catchment", muid, fields)
    assert (field_val_get[0] - 0.102342) < 0.00001
    assert (field_val_get[1] - 172.571601) < 0.00001
    data_access.close_database()


@pytest.mark.license_required
def test_import_tool(import_db):
    data_access = DataTableAccess(import_db)
    data_access.open_database()
    muids = data_access.get_muid_where("msm_Link")
    for muid in muids:
        data_access.delete("msm_Link", muid)

    # Get the path to the config file in the temporary directory
    db_dir = os.path.dirname(import_db)
    config_file = os.path.join(db_dir, "config.xml")

    import_tool = ImportTool(config_file, data_access.datatables)
    import_tool.run()
    muids = data_access.get_muid_where("msm_Link")
    assert len(muids) == 575
    data_access.close_database()
