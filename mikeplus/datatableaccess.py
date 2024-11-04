import os.path
import System
import sys
from System import Object
from System import String
from System.Collections.Generic import Dictionary
from System.Collections.Generic import List
from System.Data import ConnectionState
from DHI.Amelia.DataModule.Services.DataSource import BaseDataSource
from DHI.Amelia.DataModule.Services.DataTables import DataTableContainer

from .dotnet import as_dotnet_list


class DataTableAccess:
    """
    Class to manipulate data in MIKE+ database.

    Examples
    --------
    An example of insert a link into msm_Link table. Get field data from table and delete row from table
    ```python
    >>> data_access = DataTableAccess(muppOrSqlite)
    >>> data_access.open_database()
    >>> values = {'Diameter': 2.0, 'Description': 'insertValues'}
    >>> data_access.insert("msm_Link", "link_test", values)
    >>> fields = ["Diameter", "Description"]
    >>> values = data_access.get_field_values("msm_Link", "link_test", fields)
    >>> data_access.delete("msm_Link", "link_test")
    >>> data_access.close_database()
    ```
    """

    def __init__(self, db_or_mupp_file):
        db_or_mupp_file = os.path.abspath(db_or_mupp_file)
        self._file_path = db_or_mupp_file
        self._datatables = None

    def __repr__(self):
        out = ["<DataTableContainer>"]

        if self.is_database_open():
            out.append(
                f"Db major version: {str(self._datatables.DataSource.DbMajorVersion)}"
            )
            out.append(
                f"Db minor version: {str(self._datatables.DataSource.DbMinorVersion)}"
            )
            out.append(f"Active model: {str(self._datatables.DataSource.ActiveModel)}")
            out.append(
                f"Unit system: {str(self._datatables.DataSource.UnitSystemOption)}"
            )
            out.append(
                f"Active simulation: {str(self._datatables.DataSource.ActiveSimulation)}"
            )
        return str.join("\n", out)

    def open_database(self):
        """Open database"""
        self._check_conflict()
        if self.is_database_open():
            return
        data_source = BaseDataSource.Create(self._file_path)
        data_source.OpenDatabase()
        datatables = DataTableContainer(True)
        datatables.DataSource = data_source
        datatables.SetActiveModel(data_source.ActiveModel)
        datatables.SetEumAppUnitSystem(data_source.UnitSystemOption)
        datatables.OnResetContainer(None, None)
        self._datatables = datatables

    def close_database(self):
        """Close database"""
        self._datatables.DataSource.CloseDatabase()
        self._datatables.Dispose()
        self._datatables = None

    @property
    def datatables(self):
        """DataTableContainer"""
        return self._datatables

    def get_muid_where(self, table_name, where=None):
        """If where is none, get all the muids of the specified table. Otherwise get the muids in table which meet the condition.

        Parameters
        ----------
        table_name : string
            table name
        where : string, optional
            the condition string, by default None

        Returns
        -------
        array
            the muids array
        """
        muids = []
        muidGet = self._datatables[table_name].GetMuidsWhere(where)
        for muid in muidGet:
            muids.append(muid)
        return muids

    def get_field_values(self, table_name, muid, fields):
        """Get field values

        Parameters
        ----------
        table_name : str
            The name of the table to get values from.
        muid : str
            The MUID of the row to get values for.
        fields : str | List[str]
            The name of the field(s) to get values for.

        Returns
        -------
        List
            A list of the requested values in the same order as the fields argument.
        """
        if not isinstance(fields, list):
            fields = [fields]

        values = self._datatables[table_name].GetFieldValues(
            muid, as_dotnet_list(fields), False
        )
        pyValues = []
        i = 0
        if values is not None and len(values) > 0:
            while i < len(values):
                pyValues.append(values[i])
                i += 1
        return pyValues

    def get_muid_field_values(self, table_name, fields, where=None):
        """Get muid and field values dictionary

        Parameters
        ----------
        table_name : string
            table name
        fields : string array
            the fields want to get values
        where : string, optional
            the condition string, by default None

        Returns
        -------
        dicationary
            muid and field values dictionary
        """
        fieldList = List[str]()
        for field in fields:
            fieldList.Add(field)
        fieldValueGet = self._datatables[table_name].GetMuidAndFieldsWhereOrder(
            fieldList, where
        )
        mydict = dict()
        for feildVal in fieldValueGet:
            mylist = list()
            for val in feildVal.Value:
                mylist.append(val)
            mydict[feildVal.Key] = mylist
        return mydict

    def set_value(self, table_name, muid, column, value):
        """Set value of specified muid and column in table

        Parameters
        ----------
        table_name : string
            table name
        muid : string
            muid
        column : string
            column name
        value :
            the value want to set
        """
        self._datatables[table_name].SetValueByCommand(muid, column, value)

    def set_values(self, table_name, muid, values):
        """Set values of specified muid in table

        Parameters
        ----------
        table_name : string
            table name
        muid : string
            muid
        values : array
            field values want to set
        """
        value_dict = Dictionary[String, Object]()
        for col in values:
            value_dict[col] = values[col]
        self._datatables[table_name].SetValuesByCommand(muid, value_dict)

    def insert(self, table_name, muid, values=None):
        """Insert row into table with specified muid

        Parameters
        ----------
        table_name : string
            table name
        muid : string
            muid
        values : array, optional
            the values want to insert, by default None
        """
        value_dict = Dictionary[String, Object]()
        if values is not None:
            for col in values:
                if isinstance(values[col], int):
                    value_dict[col] = System.Nullable[int](values[col])
                else:
                    value_dict[col] = values[col]
        result, new_muid = self._datatables[table_name].InsertByCommand(
            muid, None, value_dict, False, False
        )

    def delete(self, table_name, muid):
        """Delete row with specified muid in table

        Parameters
        ----------
        table_name : string
            table name
        muid : string
            muid
        """
        self._datatables[table_name].DeleteByCommand(muid)

    def is_database_open(self):
        """Check if database if open

        Returns
        -------
        bool
            the status of the database
        """
        if self._datatables is None:
            return False
        is_open = (
            self._datatables.DataSource is not None
            and self._datatables.DataSource.DbConnection is not None
        )
        is_open = (
            is_open
            and self._datatables.DataSource.DbConnection.State == ConnectionState.Open
        )
        return is_open

    def _check_conflict(self):
        """Check if there are conflicts with mikeio and mikeioid"""

        mike1dio = sys.modules.get("mikeio1d")
        if mike1dio is not None:
            raise RuntimeError(
                "mikeio1d module has been loaded. mikeio1d only can be loaded after mikeplus module."
            )

        mikeio = sys.modules.get("mikeio")
        if mikeio is not None:
            raise RuntimeError(
                "mikeplus cannot currently be used with mikeio in the same script."
            )
