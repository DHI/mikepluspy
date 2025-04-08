from __future__ import annotations

import os.path

import System
import sys
from System import Object
from System import String
from System import DateTime
from System.Collections.Generic import Dictionary
from System.Collections.Generic import List
from System.Data import ConnectionState
from System.Data import DbType

from DHI.Amelia.DataModule.Services.DataSource import BaseDataSource
from DHI.Amelia.DataModule.Services.DataTables import DataTableContainer
from DHI.Amelia.Infrastructure.Interface.UtilityHelper import GeoAPIHelper
from DHI.Amelia.DataModule.Interface.Services import IMuGeomTable
from DHI.Amelia.DataModule.Services.DataTables import AmlUndoRedoManager
from DHI.Amelia.DataModule.Services.ImportExportPfsFile import ImportExportPfsFile
from DHI.Amelia.GlobalUtility.DataType import UserDefinedColumnType


from .dotnet import as_dotnet_list
from .dotnet import from_dotnet_datetime
from .dotnet import to_dotnet_datetime
from .conflicts import check_conflicts
from datetime import datetime
from warnings import warn


class DataTableAccess:
    """Class to manipulate data in MIKE+ database.

    This class provides direct access to tables in a MIKE+ database,
    allowing for operations like inserting, updating, and deleting data.
    
    Parameters
    ----------
    db_or_mupp_file : str
        Path to the .sqlite or .mupp database file
    
    Examples
    --------
    Insert a link into msm_Link table, get field data, and delete the row:
    
    >>> data_access = DataTableAccess(muppOrSqlite)
    >>> data_access.open_database()
    >>> values = {'Diameter': 2.0, 'Description': 'insertValues', "geometry": "LINESTRING (3 4, 10 50, 20 25)"}
    >>> data_access.insert("msm_Link", "link_test", values)
    >>> fields = ["Diameter", "Description", "geometry"]
    >>> query = data_access.get_field_values("msm_Link", "link_test", fields)
    >>> values = {'Diameter': 1.0, 'Description': 'updateValues', "geometry": "LINESTRING (4 5, 20 60, 30 35)"}
    >>> data_access.set_values("msm_Link", "link_test", values)
    >>> data_access.delete("msm_Link", "link_test")
    >>> data_access.close_database()
    """

    def __init__(self, db_or_mupp_file):
        db_or_mupp_file = os.path.abspath(db_or_mupp_file)
        self._file_path = db_or_mupp_file
        self._datatables = None
        self._scenario_manager = None

    def __repr__(self):
        out = ["<DataTableContainer>"]

        if self.is_database_open():
            data_source = self._datatables.DataSource
            out.append(f"Db major version: {str(data_source.DbMajorVersion)}")
            out.append(f"Db minor version: {str(data_source.DbMinorVersion)}")
            out.append(f"Active model: {str(data_source.ActiveModel)}")
            out.append(f"Unit system: {str(data_source.UnitSystemOption)}")
            out.append(f"Active scenario: {str(self.active_scenario)}")
            out.append(f"Active simulation: {str(data_source.ActiveSimulation)}")

        return str.join("\n", out)

    def open_database(self):
        """Open the database connection.
        
        Opens the database and initializes the DataTableContainer.
        
        Returns
        -------
        None
        """
        check_conflicts()
        if self.is_database_open():
            return
        data_source = BaseDataSource.Create(self._file_path)
        data_source.OpenDatabase()
        datatables = self._create_datatables()
        datatables.DataSource = data_source
        datatables.SetActiveModel(data_source.ActiveModel)
        datatables.SetEumAppUnitSystem(data_source.UnitSystemOption)
        datatables.OnResetContainer(None, None)
        datatables.UndoRedoManager = AmlUndoRedoManager()
        datatables.ImportExportPfsFile = ImportExportPfsFile()
        self._datatables = datatables
        self._scenario_manager = data_source.ScenarioManager

    def close_database(self):
        """Close the database connection.
        
        Clears the undo/redo buffer and closes the database connection.
        
        Returns
        -------
        None
        """
        self._datatables.UndoRedoManager.ClearUndoRedoBuffer()
        self._datatables.DataSource.CloseDatabase()
        self._datatables.Dispose()
        self._datatables = None

    @property
    def datatables(self):
        """Get the DataTableContainer object.
        
        Returns
        -------
        DataTableContainer
            The underlying .NET DataTableContainer object
        """
        return self._datatables

    @property
    def table_names(self) -> list[str]:
        """Get a list of all table names in the database.
        
        Returns
        -------
        list of str
            Names of all tables in the database
        """
        return [table.TableName for table in self._datatables.AllTables]

    def _get_table_with_validation(self, table_name: str):
        """Get a table object with validation.
        
        Parameters
        ----------
        table_name : str
            Name of the table to retrieve
            
        Returns
        -------
        object
            The .NET table object
            
        Raises
        ------
        ValueError
            If the table does not exist in the database
        """
        table = self._datatables.GetTable(table_name)
        if table is None:
            raise ValueError(f"Table '{table_name}' does not exist in the database.")
        return table

    def get_column_names(self, table_name: str) -> list[str]:
        """Get column names of the specified table.

        Parameters
        ----------
        table_name : str
            The name of the table to get fields from.

        Returns
        -------
        list[str]
            A list of field names.
        """
        table = self._get_table_with_validation(table_name)
        return [column.Field for column in table.Columns]

    def get_muid_where(self, table_name, where=None):
        """Get MUIDs from a table that match a condition.

        Parameters
        ----------
        table_name : str
            Name of the table to query
        where : str, optional
            SQL-like condition string, by default None (returns all MUIDs)

        Returns
        -------
        list of str
            List of MUIDs that match the condition
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
            WTK (well-know-text) will be returned for geometry field.

        Returns
        -------
        List
            A list of the requested values in the same order as the fields argument.
            WTK (well-know-text) will be returned for geometry field
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
                if fields[i].lower() == "geometry":
                    wkt = None
                    if values[i] is not None:
                        wkt = GeoAPIHelper.GetWKTIGeometry(values[i])
                    pyValues.append(wkt)
                elif isinstance(values[i], System.DateTime):
                    pyValues.append(from_dotnet_datetime(values[i]))
                else:
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
            WTK (well-know-text) will be returned for geometry field.
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
            i = 0
            for val in feildVal.Value:
                if (fields[i]).lower() == "geometry":
                    wkt = None
                    if val is not None:
                        wkt = GeoAPIHelper.GetWKTIGeometry(val)
                    mylist.append(wkt)
                elif isinstance(val, System.DateTime):
                    mylist.append(from_dotnet_datetime(val))
                else:
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
            Geometry can be set for the 'geometry' field of geometry based tables. e.g. Node and Link
            Two types of data format are supported. One is wkt which is string format, another is shapely geometry object.
                - WTK (well-know-text) is accept for geometry field. It uses ISO 19162:2019 standard.
                Multiple geometry is not supported.
                WTK example for point, line and polygon
                    - POINT (30 10)
                    - LINESTRING (30 10, 10 30, 40 40)
                    - POLYGON ((30 10, 40 40, 20 40, 10 20, 30 10))
                - shapely object is accept for geometry field. Please install shapely package first.
                The supported geometry types are Point, LineString and Polygon
        """
        if column.lower() == "geometry":
            wkt = None
            if isinstance(value, str):
                wkt = value
            else:
                shapely = self._get_shapely()
                wkt = shapely.to_wkt(value)
            geom = GeoAPIHelper.GetIGeometryFromWKT(wkt)
            geomTable = IMuGeomTable(self._datatables[table_name])
            geomTable.UpdateGeomByCommand(muid, geom)
        else:
            if isinstance(value, int):
                value = System.Nullable[int](value)
            elif isinstance(value, datetime):
                value = to_dotnet_datetime(value)
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
            Geometry can be set for the 'geometry' field of geometry based tables. e.g. Node and Link
            Two types of data format are supported. One is wkt which is string format, another is shapely geometry object.
                - WTK (well-know-text) is accept for geometry field. It uses ISO 19162:2019 standard.
                Multiple geometry is not supported.
                WTK example for point, line and polygon
                    - POINT (30 10)
                    - LINESTRING (30 10, 10 30, 40 40)
                    - POLYGON ((30 10, 40 40, 20 40, 10 20, 30 10))
                - shapely object is accept for geometry field. Please install shapely package first.
                The supported geometry types are Point, LineString and Polygon
        """
        value_dict = Dictionary[String, Object]()
        for col in values:
            if col.lower() == "geometry":
                geom_val = values[col]
                wkt = None
                if isinstance(geom_val, str):
                    wkt = geom_val
                else:
                    shapely = self._get_shapely()
                    wkt = shapely.to_wkt(geom_val)
                geom = GeoAPIHelper.GetIGeometryFromWKT(wkt)
                geomTable = IMuGeomTable(self._datatables[table_name])
                geomTable.UpdateGeomByCommand(muid, geom)
            elif isinstance(values[col], int):
                value_dict[col] = System.Nullable[int](values[col])
            elif isinstance(values[col], datetime):
                value_dict[col] = to_dotnet_datetime(values[col])
            else:
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
            Geometry can be set for the 'geometry' field of geometry based tables. e.g. Node and Link
            Two types of data format are supported. One is wkt which is string format, another is shapely geometry object.
                - WTK (well-know-text) is accept for geometry field. It uses ISO 19162:2019 standard.
                Multiple geometry is not supported.
                WTK example for point, line and polygon
                    - POINT (30 10)
                    - LINESTRING (30 10, 10 30, 40 40)
                    - POLYGON ((30 10, 40 40, 20 40, 10 20, 30 10))
                - shapely object is accept for geometry field. Please install shapely package first.
                The supported geometry types are Point, LineString and Polygon
        """
        value_dict = Dictionary[String, Object]()
        geom = None
        if values is not None:
            for col in values:
                if col.lower() == "geometry":
                    wkt = None
                    geom_obj = values[col]
                    if isinstance(geom_obj, str):
                        wkt = values[col]
                    else:
                        shapely = self._get_shapely()
                        wkt = shapely.to_wkt(geom_obj)
                    geom = GeoAPIHelper.GetIGeometryFromWKT(wkt)
                if isinstance(values[col], int):
                    value_dict[col] = System.Nullable[int](values[col])
                elif isinstance(values[col], datetime):
                    value_dict[col] = to_dotnet_datetime(values[col])
                else:
                    value_dict[col] = values[col]
        result, new_muid = self._datatables[table_name].InsertByCommand(
            muid, geom, value_dict, False, False
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
        """Check if database if open.

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

    def _create_datatables(self):
        datatables = DataTableContainer(True)
        return datatables

    def _get_shapely(self):
        shapely = sys.modules.get("shapely")
        if shapely is None:
            message = "This functionality requires installing the optional dependency shapely."
            raise ImportError(message)
        return shapely

    @property
    def scenarios(self) -> list[str]:
        """A list of model scenarios in the database."""
        if not self.is_database_open():
            warn("Cannot retrieve a list of scenarios. The database is closed.")
            return []

        return list(self._scenario_manager.GetScenarios())

    @property
    def active_scenario(self) -> str:
        """Current active scenarion name."""
        if not self.is_database_open():
            warn("Cannot retrieve active scenario name. The database is closed.")
            return ""

        return self._scenario_manager.ActiveScenario.Name

    def activate_scenario(self, scenario_name: str):
        """
        Activates a scenario from a given scenario name.

        Parameters
        ----------
        scenario_name : str
            Name of a scenario to activate.
        """
        if not self.is_database_open():
            warn(f"Cannot activate scenario {scenario_name}. The database is closed.")
            return

        scenario_id = self._scenario_manager.FindScenarioByName(scenario_name).Id
        self._scenario_manager.ActivateScenario(scenario_id, True)

    def add_user_defined_column(
        self,
        table_name: str,
        column_name: str,
        column_data_type: str,
        column_header: str | None = None,
    ):
        """
        Add a user defined column to a table.

        Parameters
        ----------
        table_name : str
            Name of the table to add the column to.
        column_name : str
            Name of the column in the database.
        column_data_type : str
            Data type of the column. Must be one of 'integer', 'double', 'string', 'datetime'.
        column_header : str | None
            Name of the column as displayed in the MIKE+ GUI. None uses the column_name.
        """
        table = self._get_table_with_validation(table_name)

        column_data_type = column_data_type.lower()
        if column_data_type == "integer":
            column_data_type = DbType.Int32
        elif column_data_type == "double":
            column_data_type = DbType.Double
        elif column_data_type == "string":
            column_data_type = DbType.String
        elif column_data_type == "datetime":
            column_data_type = DbType.DateTime
        else:
            raise ValueError(
                f"Invalid column_data_type: {column_data_type}. Must be one of 'integer', 'double', 'string', 'datetime'."
            )

        if column_header is None:
            column_header = column_name

        ret = table.AddUserDefinedColumn(
            UserDefinedColumnType.NewDbField,  # Only NewDbField supported for now
            column_header,
            column_name,
            column_data_type,
            "",  # Expression columns not supported yet
            "",  # Result columns not supported yet
            "",  # Result columns not supported yet
            0,  # Result columns not supported yet
            DateTime.MinValue,  # Result columns not supported yet
            False,  # Reset from database
        )

        return ret



class DataTableDemoAccess(DataTableAccess):
    """Demo access to MIKE+ database with limited functionality.

    This class should only be used for demo models with very short license
    checking time, especially when license checks might fail.
    For full-size models, use DataTableAccess instead.

    Parameters
    ----------
    db_or_mupp_file : str
        Path to the .sqlite or .mupp database file
    """

    def _create_datatables(self):
        datatables = super()._create_datatables()
        datatables.LicenseTimeout = 1
        return datatables
