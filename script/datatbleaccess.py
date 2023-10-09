import os.path
from System import Object
from System import String
from System.Collections.Generic import Dictionary
from System.Collections.Generic import List
from System.Data import ConnectionState
from DHI.Amelia.DataModule.Services.DataSource import BaseDataSource
from DHI.Amelia.DataModule.Services.DataTables import DataTableContainer


class DataTableAccess:
    def __init__(self,
                 db_or_mupp_file):
        db_or_mupp_file = os.path.abspath(db_or_mupp_file)
        self._file_path = db_or_mupp_file
        self._data_source = BaseDataSource.Create(db_or_mupp_file)
        self._datatables = None

    def __repr__(self):
        out = ["<DataTableContainer>"]

        if self._file_path and self._data_source and self._data_source.IsDBOpen():
            out.append(f"Db major version: {str(self._data_source.DbMajorVersion)}")
            out.append(f"Db minor version: {str(self._data_source.DbMinorVersion)}")
            out.append(f"Active model: {str(self._data_source.ActiveModel)}")
            out.append(f"Unit system: {str(self._data_source.UnitSystemOption)}")
            out.append(f"Active simulation: {str(self._data_source.ActiveSimulation)}")
        return str.join("\n", out)

    def open_database(self):
        self._data_source.OpenDatabase()
        datatables = DataTableContainer(True)
        datatables.DataSource = self._data_source
        datatables.SetActiveModel(self._data_source.ActiveModel)
        datatables.SetEumAppUnitSystem(self._data_source.UnitSystemOption)
        datatables.OnResetContainer(None, None)
        self._datatables = datatables

    def close_database(self):
        self._data_source.CloseDatabase()
        self._datatables.Dispose()

    @property
    def datatables(self):
        """ DataTableContainer """
        return self._datatables

    def get_muid_where(self, table_name, where=None):
        muids = []
        muidGet = self._datatables[table_name].GetMuidsWhere(where)
        for muid in muidGet:
            muids.append(muid)
        return muids

    def get_field_values(self, table_name, muid, fields):
        fieldList = List[str]()
        for field in fields:
            fieldList.Add(field)
        values = self._datatables[table_name].GetFieldValues(muid, fieldList, False)
        pyValues = []
        i = 0
        if values is not None and len(values) > 0:
            while i < len(values):
                pyValues.append(values[i])
                i += 1
        return pyValues

    def get_muid_field_values(self, table_name, fields, where=None):
        fieldList = List[str]()
        for field in fields:
            fieldList.Add(field)
        fieldValueGet = self._datatables[table_name].GetMuidAndFieldsWhereOrder(fieldList, where)
        mydict = dict()
        for feildVal in fieldValueGet:
            mylist = list()
            for val in feildVal.Value:
                mylist.append(val)
            mydict[feildVal.Key] = mylist
        return mydict

    def set_value(self, table_name, muid, column, value):
        self._datatables[table_name].SetValueByCommand(muid, column, value)

    def set_values(self, table_name, muid, values):
        value_dict = Dictionary[String, Object]()
        for col in values:
            value_dict[col] = values[col]
        self._datatables[table_name].SetValuesByCommand(muid, value_dict)

    def insert(self, table_name, muid, values=None):
        value_dict = Dictionary[String, Object]()
        if values is not None:
            for col in values:
                value_dict[col] = values[col]
        result, new_muid = self._datatables[table_name].InsertByCommand(muid, None, value_dict, False, False)

    def delete(self, table_name, muid):
        self._datatables[table_name].DeleteByCommand(muid)

    def is_database_open(self):
        if self._datatables is None:
            return False
        is_open = self._datatables.DataSource is not None and self._datatables.DataSource.DbConnection is not None
        is_open = is_open and self._datatables.DataSource.DbConnection.State == ConnectionState.Open
        return is_open
