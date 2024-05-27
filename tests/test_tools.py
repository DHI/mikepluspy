import os
from mikeplus import DataTableAccess
from mikeplus.tools.topology_repair_tool import TopoRepairTool
from mikeplus.tools.interpolation_tool import InterpolationTool
from mikeplus.tools.connection_repair_tool import ConnectionRepairTool
from mikeplus.tools.catch_slope_length_process_tool import CathSlopeLengthProcess
from mikeplus.tools.import_tool import ImportTool
from mikeplus.fieldTableNames.tableNames import CSTabNames, CommonTabNames
from mikeplus.fieldTableNames.fieldNames import Fields


def test_topology_repair_tool():
    dbFile = os.path.join("tests", "testdata", "repairToolData", "RepairTestCase.sqlite")
    data_access = DataTableAccess(dbFile)
    data_access.open_database()
    repair_tool = TopoRepairTool(data_access.datatables)
    repair_tool.run()
    query = data_access.get_muid_where(CSTabNames.LinkTable, Fields.FieldNameBase.MUID + "='LinkToDel'")
    assert len(query) == 0
    query = data_access.get_muid_where(CSTabNames.NodeTable, Fields.FieldNameBase.MUID + "='NodeIsolate'")
    assert len(query) == 0
    query = data_access.get_muid_where(CSTabNames.LinkTable, Fields.FieldNameBase.MUID + "='LinkToSplit'")
    assert len(query) == 0
    query = data_access.get_muid_where(CSTabNames.LinkTable, Fields.LinkBaseFields.ToNodeID + "='NodeToSplit'")
    assert len(query) == 2
    query = data_access.get_muid_where(CSTabNames.LinkTable, Fields.LinkBaseFields.FromNodeID + "='NodeToSplit'")
    assert len(query) == 1
    query = data_access.get_muid_where(CSTabNames.NodeTable, Fields.FieldNameBase.MUID + "='Node_8'")
    assert len(query) == 1
    data_access.close_database()


def test_interpolate_tool():
    dbFile = os.path.join("tests", "testdata", "interpolate", "inter.sqlite")
    data_access = DataTableAccess(dbFile)
    data_access.open_database()
    data_access.set_value(CSTabNames.NodeTable, "Node_1", Fields.NodeFields.Diameter, None)
    data_access.set_value(CSTabNames.NodeTable, "Node_2", Fields.NodeFields.Diameter, None)
    data_access.set_value(CSTabNames.NodeTable, "Node_3", Fields.NodeFields.Diameter, None)
    tool = InterpolationTool(data_access.datatables)
    tool.interpolate_from_nearest_feature(CSTabNames.NodeTable, Fields.NodeFields.Diameter, CSTabNames.LinkTable, Fields.LinkFields.Diameter)
    fields = [Fields.NodeFields.Diameter]
    field_val_get = data_access.get_muid_field_values(CSTabNames.NodeTable, fields)
    data_access.close_database()
    assert field_val_get['Node_1'][0] == 2.0
    assert field_val_get['Node_2'][0] == 2.0
    assert field_val_get['Node_3'][0] == 3.0


def test_connect_repair_tool():
    dbFile = os.path.join("tests", "testdata", "connectionRepair", "repair.sqlite")
    data_access = DataTableAccess(dbFile)
    data_access.open_database()
    muids = data_access.get_muid_where(CommonTabNames.StationConnTable)
    for muid in muids:
        data_access.delete(CommonTabNames.StationConnTable, muid)
    muids = data_access.get_muid_where(CSTabNames.LoadPointConnTable)
    for muid in muids:
        data_access.delete(CSTabNames.LoadPointConnTable, muid)
    conn_repair_tool = ConnectionRepairTool(data_access.datatables)
    conn_repair_tool.run()
    station_conn = data_access.get_muid_where(CommonTabNames.StationConnTable)
    assert len(station_conn) == 2
    load_point_conn = data_access.get_muid_where(CSTabNames.LoadPointConnTable)
    assert len(load_point_conn) == 2
    data_access.close_database()


def test_catch_slope_len_tool():
    dbFile = os.path.join("tests", "testdata", "catchSlopeLen", "catch.sqlite")
    data_access = DataTableAccess(dbFile)
    data_access.open_database()
    field_values = {Fields.CatchmentFields.ModelBSlope: 0.0, Fields.CatchmentFields.ModelBLength: 0.0}
    fields = [Fields.CatchmentFields.ModelBSlope, Fields.CatchmentFields.ModelBLength]
    muid = "imp3"
    data_access.set_values(CSTabNames.CatchmentTable, muid, field_values)
    field_val_get = data_access.get_field_values(CSTabNames.CatchmentTable, muid, fields)
    assert field_val_get[0] == 0.0
    assert field_val_get[1] == 0.0
    catch_ids = [muid]
    tool = CathSlopeLengthProcess(data_access.datatables)
    tool.run(catch_ids, "tests/testdata/catchSlopeLen/Catch_Slope.shp", "tests/testdata/catchSlopeLen/dem.dfs2", 0)
    field_val_get = data_access.get_field_values(CSTabNames.CatchmentTable, muid, fields)
    assert (field_val_get[0] - 0.102342) < 0.00001
    assert (field_val_get[1] - 172.571601) < 0.00001
    data_access.close_database()


def test_import_tool():
    dbFile = os.path.join("tests", "testdata", "import", "import.sqlite")
    data_access = DataTableAccess(dbFile)
    data_access.open_database()
    muids = data_access.get_muid_where(CSTabNames.LinkTable)
    for muid in muids:
        data_access.delete(CSTabNames.LinkTable, muid)
    import_tool = ImportTool("tests/testdata/import/config.xml", data_access.datatables)
    import_tool.run()
    muids = data_access.get_muid_where(CSTabNames.LinkTable)
    assert len(muids) == 575
    data_access.close_database()
