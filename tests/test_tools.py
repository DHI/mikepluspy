import os
from mikeplus import DataTableAccess
from mikeplus.tools.topology_repair_tool import TopoRepairTool
from mikeplus.tools.interpolation_tool import InterpolationTool
from mikeplus.tools.connection_repair_tool import ConnectionRepairTool
from mikeplus.tools.catch_slope_length_process_tool import CathSlopeLengthProcess
from mikeplus.tools.import_tool import ImportTool


def test_topology_repair_tool():
    dbFile = os.path.join("tests", "testdata", "repairToolData", "RepairTestCase.sqlite")
    data_access = DataTableAccess(dbFile)
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


def test_interpolate_tool():
    dbFile = os.path.join("tests", "testdata", "interpolate", "inter.sqlite")
    data_access = DataTableAccess(dbFile)
    data_access.open_database()
    data_access.set_value("msm_Node", "Node_1", "Diameter", None)
    data_access.set_value("msm_Node", "Node_2", "Diameter", None)
    data_access.set_value("msm_Node", "Node_3", "Diameter", None)
    tool = InterpolationTool(data_access.datatables)
    tool.interpolate_from_nearest_feature("msm_Node", "Diameter", "msm_Link", "Diameter")
    fields = ["Diameter"]
    field_val_get = data_access.get_muid_field_values("msm_Node", fields)
    data_access.close_database()
    assert field_val_get['Node_1'][0] == 2.0
    assert field_val_get['Node_2'][0] == 2.0
    assert field_val_get['Node_3'][0] == 3.0


def test_connect_repair_tool():
    dbFile = os.path.join("tests", "testdata", "connectionRepair", "repair.sqlite")
    data_access = DataTableAccess(dbFile)
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


def test_catch_slope_len_tool():
    dbFile = os.path.join("tests", "testdata", "catchSlopeLen", "catch.sqlite")
    data_access = DataTableAccess(dbFile)
    data_access.open_database()
    field_values = {'ModelBSlope': 0.0, 'ModelBLength': 0.0}
    fields = ["ModelBSlope", "ModelBLength"]
    muid = "imp3"
    data_access.set_values("msm_Catchment", muid, field_values)
    field_val_get = data_access.get_field_values("msm_Catchment", muid, fields)
    assert field_val_get[0] == 0.0
    assert field_val_get[1] == 0.0
    catch_ids = [muid]
    tool = CathSlopeLengthProcess(data_access.datatables)
    tool.run(catch_ids, "tests/testdata/catchSlopeLen/Catch_Slope.shp", "tests/testdata/catchSlopeLen/dem.dfs2", 0)
    field_val_get = data_access.get_field_values("msm_Catchment", muid, fields)
    assert (field_val_get[0] - 0.102342) < 0.00001
    assert (field_val_get[1] - 172.571601) < 0.00001
    data_access.close_database()


def test_import_tool():
    dbFile = os.path.join("tests", "testdata", "import", "import.sqlite")
    data_access = DataTableAccess(dbFile)
    data_access.open_database()
    muids = data_access.get_muid_where("msm_Link")
    for muid in muids:
        data_access.delete("msm_Link", muid)
    import_tool = ImportTool("tests/testdata/import/config.xml", data_access.datatables)
    import_tool.run()
    muids = data_access.get_muid_where("msm_Link")
    assert len(muids) == 575
    data_access.close_database()
