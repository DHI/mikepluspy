import os
from mikeplus import DataTableAccess
from mikeplus.fieldTableNames.tableNames import CSTabNames
from mikeplus.fieldTableNames.fieldNames import Fields



def test_opendatabase():
    file_name = os.path.join("tests", "testdata", "Db", "Sirius", "Sirius.sqlite")
    data_access = DataTableAccess(file_name)
    data_access.open_database()
    assert data_access.is_database_open() is True
    data_access.close_database()


def test_manipulate_data():
    file_name = os.path.join("tests", "testdata", "Db", "Sirius", "Sirius.sqlite")
    data_access = DataTableAccess(file_name)
    data_access.open_database()
    muids = data_access.get_muid_where(CSTabNames.LinkTable, "MUID='link_test'")
    if len(muids) == 1:
        data_access.delete(CSTabNames.LinkTable, "link_test")
    field_values = {Fields.LinkFields.Diameter: 2.5, Fields.DescriptionFieldBase.Description: 'setvalues'}
    data_access.insert(CSTabNames.LinkTable, "link_test", field_values)
    muids = data_access.get_muid_where(CSTabNames.LinkTable, "MUID='link_test'")
    assert len(muids) == 1
    fields = [Fields.LinkFields.Diameter, Fields.DescriptionFieldBase.Description]
    values_get = data_access.get_field_values(CSTabNames.LinkTable, "link_test", fields)
    assert values_get[0] == 2.5
    assert values_get[1] == 'setvalues'
    field_values = {Fields.LinkFields.Diameter: 1.0, Fields.DescriptionFieldBase.Description: 'Desc'}
    data_access.set_values(CSTabNames.LinkTable, "link_test", field_values)
    values_get = data_access.get_field_values(CSTabNames.LinkTable, "link_test", fields)
    assert values_get[0] == 1.0
    assert values_get[1] == 'Desc'
    data_access.delete(CSTabNames.LinkTable, "link_test")
    muids = data_access.get_muid_where(CSTabNames.LinkTable, "MUID='link_test'")
    assert len(muids) == 0
    data_access.close_database()
