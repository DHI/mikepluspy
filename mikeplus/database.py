"""Entry point for MIKE+ model database operations.

This module provides the main Database class which serves as the primary interface 
for working with MIKE+ databases. It handles opening, creating, and manipulating 
MIKE+ model files, including access to tables and scenarios.
"""

from __future__ import annotations


from DHI.Amelia.DataModule.Services.DataSource import BaseDataSource
from DHI.Amelia.DataModule.Services.DataTables import DataTableContainer
from DHI.Amelia.DataModule.Services.DataTables import AmlUndoRedoManager
from DHI.Amelia.DataModule.Services.ImportExportPfsFile import ImportExportPfsFile
from DHI.Amelia.DataModule.Services.DataSource.ScenarioMangement import ScenarioManager

from plistlib import InvalidFileException
from pathlib import Path

from .conflicts import check_conflicts
from .tables.auto_generated import TableCollection


class Database:
    """Represents a MIKE+ model database."""

    def __init__(self, model_path: str | Path, *, auto_open: bool = True):
        """Initialize a new Database.

        Parameters
        ----------
        model_path : str or Path
            Path to the model database file (e.g. "model.sqlite" or "model.mupp")
        auto_open : bool
            If True, immediately open the database connection

        Raises
        ------
        FileNotFoundError
            If the database file doesn't exist
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
    def create(
        cls,
        model_path: str | Path,
        *,
        projection_string: str = "",
        srid: int = -1,
        auto_open: bool = True,
    ) -> Database:
        """Create a new MIKE+ model database.

        Parameters
        ----------
        model_path : str or Path
            Path where the new database will be created
        projection_string : str, optional
            The projection string for the database
        srid : int, optional
            The SRID for the database, e.g. 4326 for WGS84
        auto_open : bool, optional
            If True, immediately open the database connection

        Returns
        -------
        Database
            A Database object for the newly created database

        Raises
        ------
        FileExistsError
            If the database already exists
        """
        model_path = Path(model_path)
        if model_path.exists():
            raise FileExistsError(f"Model file '{model_path}' already exists.")

        db_sqlite = model_path.with_suffix(".sqlite")

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

        db = cls(model_path, auto_open=auto_open)
        return db

    def open(self):
        """Open the model database.

        Returns
        -------
        self
            For method chaining
        """
        check_conflicts()

        if self._is_open:
            return self

        try:
            self._data_source.OpenDatabase()
            self._data_table_container.SetActiveModel(self._data_source.ActiveModel)
            self._data_table_container.SetEumAppUnitSystem(
                self._data_source.UnitSystemOption
            )
            self._data_table_container.OnResetContainer(None, None)
            self._data_table_container.UndoRedoManager = AmlUndoRedoManager()
            self._data_table_container.ImportExportPfsFile = ImportExportPfsFile()
            self._scenario_manager = self._data_source.ScenarioManager
            self._is_open = True
        except Exception as e:
            raise Exception(
                f"Failed to open model database: {self._db_path}.\n{str(e)}"
            )

        return self

    def close(self):
        """Close the model database."""
        if not self._is_open:
            return True

        try:
            self._data_table_container.UndoRedoManager.ClearUndoRedoBuffer()
            self._data_table_container.DataSource.CloseDatabase()
            self._is_open = False
        except Exception as e:
            raise Exception(
                f"Failed to close model database: {self._db_path}.\n{str(e)}"
            )

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

        Returns
        -------
        Path
            Path to the database file
        """
        return self._db_path

    @property
    def mupp_path(self) -> Path | None:
        """Get the path to the MUPP file.

        Returns
        -------
        Path or None
            Path to the MUPP file, or None
        """
        return self._mupp_path

    @property
    def tables(self) -> TableCollection:
        """A collection of tables in the database.

        This property provides access to all tables in the database through a 
        fluent interface that allows for SQL-like operations on tables. It is 
        the primary entry point for working with tables.
        
        Returns
        -------
        TableCollection
            Collection of all tables in the database
        """
        return self._tables

    @property
    def is_open(self) -> bool:
        """Check if the database is open.

        Returns
        -------
        bool
            True if the database is open, False otherwise
        """
        return self._is_open

    @property
    def unit_system(self) -> str:
        """Get the unit system of the database in MIKE+ format.

        Returns
        -------
        str
            Unit system string (e.g. "MU_CS_SI")
        """
        return str(self._data_table_container.UnitSystemOption)

    @property
    def projection_string(self) -> str:
        """Get the projection string of the database.

        Returns
        -------
        str
            Projection string of the database
        """
        return str(self._data_source.ProjectionString)

    @property
    def srid(self) -> int:
        """Get the Spatial Reference ID (SRID) of the database.

        Returns
        -------
        int
            SRID value as an integer
        """
        return self._data_source.Srid

    @property
    def active_simulation(self) -> str:
        """
        Get the active simulation of the database.

        Returns
        -------
        str
            Active simulation name
        """
        return self._data_source.ActiveSimulation

    @property
    def version(self) -> str:
        """Get the version of the database.

        Returns
        -------
        str
            Version string
        """
        major_version = self._data_source.DbMajorVersion
        minor_version = self._data_source.DbMinorVersion

        return f"{major_version}.{minor_version}"

    @property
    def scenarios(self) -> list[str]:
        """Get the list of available scenarios.

        Returns
        -------
        list of str
            List of scenario names
        """
        if not self._scenario_manager:
            raise ValueError("Open the database with `open()` before accessing scenarios.")

        return list(self._scenario_manager.GetScenarios())
    @property
    def active_scenario(self) -> str:
        """Name of the active scenario

        Returns
        -------
        str
            Name of the active scenario

        Notes
        -----
        This can be set to a new scenario name to activate a different scenario.
        """
        if not self._scenario_manager:
            raise ValueError("Open the database with `open()` before accessing scenarios.")

        return self._scenario_manager.ActiveScenario.Name

    @active_scenario.setter
    def active_scenario(self, scenario_name: str):
        if not self._scenario_manager:
            raise ValueError("Open the database with `open()` before accessing scenarios.")

        if scenario_name not in self.scenarios:
            raise ValueError(
                f"Scenario '{scenario_name}' does not exist. Valid scenarios: {self.scenarios}"
            )

        scenario_id = self._scenario_manager.FindScenarioByName(scenario_name).Id
        self._scenario_manager.ActivateScenario(scenario_id, True)

    @property
    def active_model(self) -> str:
        """Get the name of the active model.

        Returns
        -------
        str
            Name of the active model
        """
        return str(self._data_source.ActiveModel)


__all__ = [
    "Database",
]
