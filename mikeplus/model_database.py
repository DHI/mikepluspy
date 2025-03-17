"""
Entry point for MIKE+ model database operations.
"""
from __future__ import annotations

import System
import sys

from DHI.Amelia.DataModule.Services.DataSource import BaseDataSource
from DHI.Amelia.DataModule.Services.DataTables import DataTableContainer
from DHI.Amelia.Infrastructure.Interface.UtilityHelper import GeoAPIHelper
from DHI.Amelia.DataModule.Interface.Services import IMuGeomTable
from DHI.Amelia.DataModule.Services.DataTables import AmlUndoRedoManager
from DHI.Amelia.DataModule.Services.ImportExportPfsFile import ImportExportPfsFile
from DHI.Amelia.GlobalUtility.DataType import UserDefinedColumnType

from plistlib import InvalidFileException
from pathlib import Path

from .conflicts import check_conflicts
from .tables.auto_generated import TableCollection


class ModelDatabase:
    """Represents a MIKE+ model database."""
    
    def __init__(self, model_path: str | Path, *, auto_open: bool = True):
        """Initialize a new ModelDatabase.
        
        Args:
            model_path: Path to the model database file (e.g. "model.sqlite" or "model.mupp")
            auto_open: If True, immediately open the database connection
            
        Raises:
            FileNotFoundError: If the database file doesn't exist
        """
        model_path = Path(model_path)
        
        if not model_path.exists():
            raise FileNotFoundError(f"Model file '{model_path}' does not exist.")

        self._db_path = model_path
        self._mupp_path = None

        mupp_file = model_path.with_suffix(".mupp")
        if mupp_file.exists():
            self._mupp_path = mupp_file

        db_file = model_path.with_suffix(".sqlite")
        if db_file.exists():
            self._db_path = db_file

        if not (self._db_path or self._mupp_path):
            raise InvalidFileException(f"Model file '{model_path}' is invalid.")
        
        self._data_source: BaseDataSource = BaseDataSource.Create(str(self._db_path))
        self._data_table_container: DataTableContainer = DataTableContainer(True)
        self._data_table_container.DataSource = self._data_source
        self._tables: TableCollection = TableCollection(self._data_table_container)
        self._scenario_manager: ScenarioManager | None = None
        self._is_open = False
        
        if auto_open:
            self.open()
            
    @classmethod
    def create(cls, model_path: str | Path, *, projection_string: str = "", srid: int = -1, auto_open: bool = True) -> ModelDatabase:
        """Create a new MIKE+ model database.
        
        Args:
            model_path: Path where the new database will be created
            projection_string: The projection string for the database
            srid: The SRID for the database, e.g. 4326 for WGS84
            auto_open: If True, immediately open the database connection
            
        Returns:
            A ModelDatabase object for the newly created database
            
        Raises:
            FileExistsError: If the database already exists
        """
        model_path = Path(model_path)
        if model_path.exists():
            raise FileExistsError(f"Model file '{model_path}' already exists.")

        db_sqlite= model_path.with_suffix(".sqlite")

        if projection_string and srid != -1:
            raise ValueError("Projection string and SRID cannot be specified together.")

        try:
            data_source = BaseDataSource.Create(str(db_sqlite))
            data_source.CreateDatabase()
            data_source.OpenDatabase()
            data_source.CreateModelTables(srid, projection_string)
            data_source.CloseDatabase()
        except Exception as e:
            raise Exception(f"Failed to create model database: {str(e)}")

        mdb = cls(model_path, auto_open=auto_open)
        return mdb

    def open(self):
        """Open the model database.
        
        Returns:
            self: For method chaining
        """
        check_conflicts()
        
        if self._is_open:
            return self

        try:
            self._data_source.OpenDatabase()
            self._data_table_container.SetActiveModel(self._data_source.ActiveModel)
            self._data_table_container.SetEumAppUnitSystem(self._data_source.UnitSystemOption)
            self._data_table_container.OnResetContainer(None, None)
            self._data_table_container.UndoRedoManager = AmlUndoRedoManager()
            self._data_table_container.ImportExportPfsFile = ImportExportPfsFile()
            self._scenario_manager = self._data_source.ScenarioManager
            self._is_open = True
        except Exception as e:
            raise Exception(f"Failed to open model database: {self._db_path}.\n{str(e)}")
            
        return self

    
    def close(self):
        """Close the model database."""
        if not self._is_open:
            return True
        
        try:
            self._data_table_container.UndoRedoManager.ClearUndoRedoBuffer()
            self._data_table_container.DataSource.CloseDatabase()
            self._data_table_container.Dispose()
            self._data_table_container = None
            self._is_open = False
        except Exception as e:
            raise Exception(f"Failed to close model database: {self._db_path}.\n{str(e)}")
            
    def __enter__(self):
        """Context manager entry."""
        self.open()
        return self
        
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit."""
        self.close()

    @property
    def db_path(self) -> Path:
        """Get the path to the database file.
        
        Returns:
            Path to the database file
        """
        return self._db_path

    @property
    def mupp_path(self) -> Path | None:
        """Get the path to the MUPP file.
        
        Returns:
            Path to the MUPP file, or None
        """
        return self._mupp_path
    
    @property
    def tables(self) -> TableCollection:
        """A collection of tables in the database.

        This property provides access to all tables in the database, and is
        the primary entry point for working with tables.

        Returns:
            TableCollection object
        """
        return self._tables
    
    @property
    def is_open(self) -> bool:
        """Check if the database is open.
        
        Returns:
            True if the database is open, False otherwise
        """
        return self._is_open
    
    @property
    def unit_system(self) -> str:
        """Get the unit system of the database in MIKE+ format.
        
        Returns:
            Unit system string (e.g. "MU_CS_SI")
        """
        return str(self._data_table_container.UnitSystemOption)


    @property
    def version(self) -> str:
        """Get the version of the database.
        
        Returns:
            Version string
        """
        major_version = self._data_source.DbMajorVersion
        minor_version = self._data_source.DbMinorVersion

        return f"{major_version}.{minor_version}"

    @property
    def scenarios(self) -> list[str]:
        """Get the list of available scenarios.

        Returns:
            List of scenario names
        """
        return list(self._scenario_manager.GetScenarios())
    
    @property
    def active_scenario(self) -> str:
        """Name of the active scenario
        
        Returns:
            str: Name of the active scenario

        Notes:
            This can be set to a new scenario name to activate a different scenario.
        """
        return self._scenario_manager.ActiveScenario.Name

    @active_scenario.setter
    def active_scenario(self, scenario_name: str):
        if scenario_name not in self.scenarios:
            raise ValueError(f"Scenario '{scenario_name}' does not exist. Valid scenarios: {self.scenarios}")

        scenario_id = self._scenario_manager.FindScenarioByName(scenario_name).Id
        self._scenario_manager.ActivateScenario(scenario_id, True)
    
    @property
    def activate_model(self) -> str:
        """Get the name of the active model.
        
        Returns:
            Name of the active model
        """
        pass


__all__ = [
    "ModelDatabase",
]
