import os
from mikeplus import DataTableAccess
from mikeplus.tableWrapper.MsmNode import MsmNode, MsmNodeFields
from mikeplus.tableWrapper.FieldNameBase import FieldNameBase

file_name = os.path.join("tests", "testdata", "Db", "Sirius", "Sirius.sqlite")
data_access = DataTableAccess(file_name)
data_access.open_database()
node = MsmNode()
node.values[FieldNameBase.MUID] = "node_obj_test"
node.values[MsmNodeFields.Diameter] = 3.0
node.values[MsmNodeFields.InvertLevel] = 2.0
data_access.insertObj(node)
muids = data_access.get_muid_where("msm_Node", "MUID='node_obj_test'")
assert len(muids) == 1
fields = [MsmNodeFields.Diameter, MsmNodeFields.InvertLevel]
values_get = data_access.get_field_values(node.tableName, node.values[FieldNameBase.MUID], fields)
assert values_get[0] == 3.0
assert values_get[1] == 2.0
node.values[MsmNodeFields.LossCoeffKm] = 4.5
data_access.setObjValues(node)
fields = [MsmNodeFields.LossCoeffKm]
values_get = data_access.get_field_values(node.tableName, node.values[FieldNameBase.MUID], fields)
assert values_get[0] == 4.5
data_access.deleteObj(node)
muids = data_access.get_muid_where("msm_Link", "MUID='link_test'")
assert len(muids) == 0
data_access.close_database()