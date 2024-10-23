import pytest

import os
from mikeplus import DataTableAccess


def test_opendatabase():
    file_name = os.path.join("tests", "testdata", "Db", "Sirius", "Sirius.sqlite")
    data_access = DataTableAccess(file_name)
    data_access.open_database()
    assert data_access.is_database_open() is True
    data_access.close_database()

# parameterize this test for different table name, MUIDs, fields, and expected values
@pytest.mark.parametrize("table_name, muid, fields, expected_values", [
    ("msm_Link", "Link_30", "Length", [4.06]),
    ('msm_Link', 'Link_30', ['Length', 'Diameter'], [4.06, 1.0]),
    ])
def test_get_field_values(table_name, muid, fields, expected_values):
    file_name = os.path.join("tests", "testdata", "Db", "Sirius", "Sirius.sqlite")
    data_access = DataTableAccess(file_name)
    data_access.open_database()
    values = data_access.get_field_values(table_name, muid, fields)
    assert values == expected_values
    data_access.close_database()


def test_manipulate_data():
    file_name = os.path.join("tests", "testdata", "Db", "Sirius", "Sirius.sqlite")
    data_access = DataTableAccess(file_name)
    data_access.open_database()
    muids = data_access.get_muid_where("msm_Link", "MUID='link_test'")
    if len(muids) == 1:
        data_access.delete("msm_Link", "link_test")
    field_values = {'Diameter': 2.5, 'Description': 'setvalues'}
    data_access.insert("msm_Link", "link_test", field_values)
    muids = data_access.get_muid_where("msm_Link", "MUID='link_test'")
    assert len(muids) == 1
    fields = ["Diameter", "Description"]
    values_get = data_access.get_field_values("msm_Link", "link_test", fields)
    assert values_get[0] == 2.5
    assert values_get[1] == 'setvalues'
    field_values = {'Diameter': 1.0, 'Description': 'Desc'}
    data_access.set_values("msm_Link", "link_test", field_values)
    values_get = data_access.get_field_values("msm_Link", "link_test", fields)
    assert values_get[0] == 1.0
    assert values_get[1] == 'Desc'
    data_access.delete("msm_Link", "link_test")
    muids = data_access.get_muid_where("msm_Link", "MUID='link_test'")
    assert len(muids) == 0
    data_access.close_database()
