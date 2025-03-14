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
            
        self._data_table_container: DataTableContainer | None = None
        self._scenario_manager: ScenarioManager | None = None
        self._tables: TableCollection | None = None
        self._is_open = False
        
        if auto_open:
            self.open()
            
    @classmethod
    def create(cls, model_path: str | Path) -> ModelDatabase:
        """Create a new MIKE+ model database.
        
        Args:
            model_path: Path where the new database will be created
            
        Returns:
            A ModelDatabase object for the newly created database
            
        Raises:
            FileExistsError: If the database already exists
        """
        # Implementation here would create the database
        
        # Return an opened database
        return cls(model_path, auto_open=True)

    def open(self):
        """Open the model database.
        
        Returns:
            self: For method chaining
        """
        check_conflicts()
        
        if self._is_open:
            return self

        try:
            data_source = BaseDataSource.Create(str(self._db_path))
            data_source.OpenDatabase()
            data_table_container = DataTableContainer(True)
            data_table_container.DataSource = data_source
            data_table_container.SetActiveModel(data_source.ActiveModel)
            data_table_container.SetEumAppUnitSystem(data_source.UnitSystemOption)
            data_table_container.OnResetContainer(None, None)
            data_table_container.UndoRedoManager = AmlUndoRedoManager()
            data_table_container.ImportExportPfsFile = ImportExportPfsFile()
            self._data_table_container = data_table_container
            self._scenario_manager = data_source.ScenarioManager
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
        pass
    
    @property
    def is_open(self) -> bool:
        """Check if the database is open.
        
        Returns:
            True if the database is open, False otherwise
        """
        return self._is_open
    
    @property
    def unit_system(self) -> str:
        """Get the unit system of the database.
        
        Returns:
            Unit system string
        """
        pass
    
    @property
    def version(self) -> str:
        """Get the version of the database.
        
        Returns:
            Version string
        """
        pass
    
    @property
    def active_scenario(self) -> str:
        """Get the name of the active scenario.
        
        Returns:
            Name of the active scenario
        """
        pass
    
    @property
    def active_simulation(self) -> str:
        """Get the name of the active simulation.
        
        Returns:
            Name of the active simulation
        """
        pass
    
    @property
    def activate_model(self) -> str:
        """Get the name of the active model.
        
        Returns:
            Name of the active model
        """
        pass
        
    def set_active_scenario(self, scenario_name: str):
        """Set the active scenario.
        
        Args:
            scenario_name: Name of the scenario to activate
        """
        pass
    
    def set_active_simulation(self, simulation_name: str):
        """Set the active simulation.
        
        Args:
            simulation_name: Name of the simulation to activate
        """
        pass
    
    def create_scenario(self, name: str, base_scenario: str):
        """Create a new scenario based on an existing one.
        
        Args:
            name: Name of the new scenario
            base_scenario: Name of the scenario to base the new one on
        """
        pass

__all__ = [
    "ModelDatabase",
]
