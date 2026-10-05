"""Entry point for MIKE+ model database operations.

This module provides the main Database class which serves as the primary interface
for working with MIKE+ databases. It handles opening, creating, and manipulating
MIKE+ model files, including access to tables and scenarios.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Literal, Self

if TYPE_CHECKING:
    from types import TracebackType

    from .scenarios.scenario import Scenario

import tempfile
from pathlib import Path

from DHI.Amelia.DataModule.Services.DataSource import BaseDataSource
from DHI.Amelia.DataModule.Services.DataSource.ScenarioMangement import (
    ScenarioManager as NetScenarioManager,
)
from DHI.Amelia.DataModule.Services.DataTables import (
    AmlUndoRedoManager,
    DataTableContainer,
)
from DHI.Amelia.DataModule.Services.ImportExportPfsFile import ImportExportPfsFile
from DHI.Amelia.EPANETBridge import INPBridge
from DHI.Amelia.GlobalUtility.DataType import DataBaseType
from DHI.Amelia.SWMMBridge import SWMMStorageBridge
from System.Threading import CancellationTokenSource

from .conflicts import check_conflicts
from .scenarios.alternative_group_collection import AlternativeGroupCollection
from .scenarios.scenario_collection import ScenarioCollection
from .simulation_runner import SimulationRunner
from .tables.auto_generated import TableCollection


class DatabaseError(Exception):
    """Raised when a MIKE+ database operation fails."""


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

        resolved = self._db_path.resolve()
        # PFS resolves the relative DBFilePath in a .mupp wrongly from a forward-slash path
        self._data_source: BaseDataSource = BaseDataSource.Create(
            str(resolved) if resolved.suffix.lower() == ".mupp" else resolved.as_posix()
        )
        self._data_table_container: DataTableContainer = DataTableContainer(True)
        self._data_table_container.DataSource = self._data_source
        self._tables: TableCollection = TableCollection(self._data_table_container)
        self._net_scenario_manager: NetScenarioManager | None = None
        self._scenarios: ScenarioCollection | None = None
        self._alternative_groups: AlternativeGroupCollection | None = None
        self._is_open = False

        if auto_open:
            self.open()

        self._runner = SimulationRunner(self)

    def __repr__(self) -> str:
        """Get nice string representation.

        Returns
        -------
        str
            The database file name.
        """
        return f"Database<'{self._db_path.name}'>"

    @classmethod
    def create(
        cls,
        model_path: str | Path,
        *,
        projection_string: str = "",
        srid: int = -1,
        auto_open: bool = True,
        overwrite: bool = False,
    ) -> Database:
        """Create a new MIKE+ model database.

        Writes the `.sqlite` database and a `.mupp` project file beside it, so
        the new model opens in MIKE+.

        Parameters
        ----------
        model_path : str or Path
            Path where the new database will be created, as `.sqlite` or `.mupp`
        projection_string : str, optional
            The projection string (WKT) for the database. The SRID is derived
            from it when MIKE+ recognises the projection.
        srid : int, optional
            The EPSG code of a projected coordinate system, e.g. ETRS89 / UTM
            zone 32N is 25832. Geographic systems such as 4326 are not supported;
            use a projected one such as 3857.
        auto_open : bool, optional
            If True, immediately open the database connection
        overwrite : bool, optional (default is False)
            If True, delete an existing database and project file first. Settings
            MIKE+ stores in the project file, such as map layers, are lost.

        Returns
        -------
        Database
            A Database object for the newly created database

        Raises
        ------
        FileExistsError
            If the database or project file already exists (except if overwrite
            is True)
        ValueError
            If both `projection_string` and `srid` are given, or `srid` is not
            a projected coordinate system MIKE+ knows
        DatabaseError
            If MIKE+ fails to create the database

        """
        model_path = Path(model_path)
        db_sqlite = model_path.with_suffix(".sqlite")
        db_mupp = model_path.with_suffix(".mupp")

        if projection_string and srid != -1:
            raise ValueError("Projection string and SRID cannot be specified together.")
        if srid != -1:
            projection_string = _projection_for_srid(srid)

        if overwrite:
            model_path.unlink(missing_ok=True)
            db_sqlite.unlink(missing_ok=True)
            db_mupp.unlink(missing_ok=True)

        if model_path.exists() or db_sqlite.exists() or db_mupp.exists():
            raise FileExistsError(f"Model file '{model_path}' already exists.")

        try:
            data_source = BaseDataSource.Create(str(db_sqlite))
            data_source.CreateDatabase()
            data_source.OpenDatabase()
            if projection_string and srid == -1:
                srid = data_source.GetSRIDFromProjStr(projection_string)
            data_source.CreateModelTables(srid, projection_string)
            if srid > 0:
                _save_srid(data_source, srid)
            _ensure_mupp_file(data_source)
            data_source.CloseDatabase()
        except Exception as e:
            raise DatabaseError(f"Failed to create model database: {e!s}")

        db = cls(model_path, auto_open=auto_open)
        return db

    def open(self) -> Self:
        """Open the model database.

        Returns
        -------
        Database
            self, for method chaining

        Raises
        ------
        DatabaseError
            If MIKE+ fails to open the database

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
            self._net_scenario_manager = self._data_source.ScenarioManager
            self._scenarios = ScenarioCollection(self._net_scenario_manager)
            self._alternative_groups = AlternativeGroupCollection(
                self._net_scenario_manager
            )
            self._is_open = True
        except Exception as e:
            raise DatabaseError(
                f"Failed to open model database: {self._db_path}.\n{e!s}"
            )

        return self

    def close(self) -> None:
        """Close the model database. Closing a closed database does nothing.

        Raises
        ------
        DatabaseError
            If MIKE+ fails to close the database
        """
        if not self._is_open:
            return

        try:
            self._data_table_container.UndoRedoManager.ClearUndoRedoBuffer()
            self._data_table_container.DataSource.CloseDatabase()
            self._is_open = False
        except Exception as e:
            raise DatabaseError(
                f"Failed to close model database: {self._db_path}.\n{e!s}"
            )

    def ensure_mupp(self) -> Path:
        """Get the model's project file (.mupp), writing one if it has none.

        A missing project file is written beside the database with the same
        name, as MIKE+ does when it opens a bare `.sqlite`. It records the
        database's model type and unit system and refers to the database by a
        path relative to itself. An existing project file is never changed.

        Returns
        -------
        Path
            Path to the project file.

        Raises
        ------
        ValueError
            If the database is not open.
        DatabaseError
            If MIKE+ fails to write the project file.

        Examples
        --------
        >>> with mp.open("path/to/model.sqlite") as db:
        ...     db.ensure_mupp()
        """
        if not self._is_open:
            raise ValueError("Database is not open")

        if self._mupp_path is None or not self._mupp_path.exists():
            self._mupp_path = _ensure_mupp_file(self._data_source)
        return self._mupp_path

    def begin_transaction(self) -> None:
        """Begin the data transaction.

        Using a BEGIN/END transaction significantly improves batch commit performance.

        Examples
        --------
        >>> from mikeplus import Database
        >>> db = Database("path/to/model.sqlite")
        >>> db.begin_transaction()
        >>> commit = True
        >>> try:
        >>>     db._tables.msm_Node.update({"Diameter": 0.35}).by_muid("Node_1").execute()
        >>>     db._tables.msm_Node.update({"Diameter": 0.40}).by_muid("Node_2").execute()
        >>>     ... [Update more data]
        >>> except RuntimeError as e:
        >>>     print(f"An error occurred: {e}")
        >>>     commit = False
        >>> finally:
        >>>     db.end_transaction(commit)

        Raises
        ------
        ValueError
            If the database is not open
        """
        if not self._is_open:
            raise ValueError("Database is not open")

        self._data_table_container.BeginTransaction()

    def end_transaction(self, commit: bool = True) -> None:
        """End the data transaction.

        Parameters
        ----------
        commit : bool
            true is to commit the data into database, false is to rollback the commit.

        Raises
        ------
        ValueError
            If the database is not open
        """
        if not self._is_open:
            raise ValueError("Database is not open")

        self._data_table_container.EndTransaction(commit)

    def __enter__(self) -> Self:
        """Context manager entry.

        Returns
        -------
        Database
            The opened database.
        """
        self.open()
        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> None:
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
        """Get the active simulation of the database.

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
    def scenarios(self) -> ScenarioCollection:
        """Access to MIKE+ scenario management.

        Returns
        -------
        ScenarioCollection
            Collection of all scenarios in the database

        Raises
        ------
        ValueError
            If the database is not open
        """
        if not self._is_open:
            raise ValueError("Database is not open")

        if not self._scenarios:
            self._scenarios = ScenarioCollection(self._net_scenario_manager)

        return self._scenarios

    @property
    def alternative_groups(self) -> AlternativeGroupCollection:
        """Access to MIKE+ alternative groups.

        Returns
        -------
        AlternativeGroupCollection
            Collection of all alternative groups in the database

        Raises
        ------
        ValueError
            If the database is not open
        """
        if not self._is_open:
            raise ValueError("Database is not open")

        if not self._alternative_groups:
            self._alternative_groups = AlternativeGroupCollection(
                self._net_scenario_manager
            )

        return self._alternative_groups

    @property
    def active_scenario(self) -> Scenario:
        """Active scenario.

        Returns
        -------
        Scenario
            The active scenario

        Notes
        -----
        This can be set to a `Scenario` (for example from `scenarios.by_name()`)
        to activate a different scenario.
        For more advanced scenario management, use the `scenarios` property.

        Raises
        ------
        ValueError
            If the database is not open or its scenarios are not initialized

        """
        if not self._is_open:
            raise ValueError("Database is not open")

        if not self._scenarios:
            raise ValueError("Scenarios are not initialized")

        return self._scenarios.active

    @active_scenario.setter
    def active_scenario(self, scenario: Scenario):
        if not self._is_open:
            raise ValueError("Database is not open")

        if not self._scenarios:
            raise ValueError("Scenarios are not initialized")

        if scenario is None:
            raise ValueError("Scenario cannot be None")

        if "Scenario" not in repr(scenario):
            raise ValueError(
                "Scenario must be an instance of Scenario. Use Database.scenarios.by_name() to get a scenario instance."
            )

        if scenario not in self._scenarios:
            valid_scenarios = [s.name for s in self._scenarios]
            raise ValueError(
                f"Scenario '{scenario.name}' does not exist. Valid scenarios: {valid_scenarios}"
            )

        scenario.activate()

    @property
    def active_model(self) -> str:
        """Get the name of the active model.

        Returns
        -------
        str
            Name of the active model

        """
        return str(self._data_source.ActiveModel)

    def run(
        self,
        simulation_muid: str | None = None,
        *,
        sim_option: Literal[
            "CS_MIKE_1D",
            "CS_SWMM",
            "WD_EPANET",
            "CS_MIKE_1D_JobList",
        ]
        | None = None,
    ) -> list[Path]:
        """Run a simulation.

        Parameters
        ----------
        simulation_muid : str, optional
            Simulation MUID. Defaults to the active simulation.
        sim_option : Literal[str], optional
            Simulation option. Defaults to None. Possible values are:

            - "CS_MIKE_1D": Rivers, collection systems, and overland flows.
            - "CS_SWMM": SWMM-based collection systems and overland flows.
            - "WD_EPANET": Water distribution systems.
            - "CS_MIKE_1D_JobList": Generate job list for LTS simulation (.MJL file).

        Examples
        --------
        >>> with mp.open("path/to/model.sqlite") as db:
        ...     results = db.run()

        >>> with mp.open("path/to/model.sqlite") as db:
        ...     results = db.run("My Simulation")

        >>> db = mp.open("path/to/model.sqlite")
        >>> results = db.run("My Simulation")
        >>> db.close()

        Returns
        -------
        list[Path]
            Paths to the result files the simulation wrote.

        Raises
        ------
        ValueError
            If `sim_option` is invalid, or not given and the active model does not
            determine one.
        RuntimeError
            If the simulation engine fails to start, exits with an error, or
            doesn't write its result files. The message names the engine's logs.
        """
        return self._runner.run(simulation_muid, sim_option=sim_option)

    def import_from_epanet(self, file_path: str | Path) -> None:
        """Import a model from an EPANET .inp file.

        Parameters
        ----------
        file_path : str or Path
            Path to the EPANET .inp file. If not provided, a file dialog will open.

        Examples
        --------
        >>> with mp.create("path/to/model.sqlite") as db:
        ...     db.import_from_epanet("path/to/model.inp")

        Raises
        ------
        FileNotFoundError
            If the file doesn't exist
        ValueError
            If the file is not an .inp file
        DatabaseError
            If the import fails

        """
        file_path = Path(file_path)
        if not file_path.exists():
            raise FileNotFoundError(f"EPANET file '{file_path}' does not exist.")

        if file_path.suffix.lower() != ".inp":
            raise ValueError("Provided file is not an EPANET .inp file.")

        inp_bridge = INPBridge(self._data_table_container, None)

        try:
            cancellation_token = CancellationTokenSource()
            result = inp_bridge.Import(file_path.as_posix(), cancellation_token.Token)
        except Exception as e:
            messages = "\n".join(inp_bridge.ErrorMsgs)
            raise DatabaseError(
                f"Error importing from EPANET file.\n{e!s}\n{messages}"
            ) from None
        if not result:
            messages = "\n".join(inp_bridge.ErrorMsgs)
            raise DatabaseError(f"Error importing from EPANET file.\n{messages}")

    def import_from_swmm(self, file_path: str | Path) -> None:
        """Import a model from a SWMM .inp file.

        Parameters
        ----------
        file_path : str or Path
            Path to the SWMM .inp file.

        Examples
        --------
        >>> with mp.create("path/to/model.sqlite") as db:
        ...     db.import_from_swmm("path/to/model.inp")

        Raises
        ------
        FileNotFoundError
            If the file doesn't exist
        ValueError
            If the file is not an .inp file
        DatabaseError
            If the import fails

        """
        file_path = Path(file_path)
        if not file_path.exists():
            raise FileNotFoundError(f"SWMM file '{file_path}' does not exist.")

        if file_path.suffix.lower() != ".inp":
            raise ValueError("Provided file is not a SWMM .inp file.")

        inp_bridge = SWMMStorageBridge(self._data_table_container, None)

        try:
            cancellation_token = CancellationTokenSource()
            result = inp_bridge.Import(file_path.as_posix(), cancellation_token.Token)
        except Exception as e:
            messages = "\n".join(inp_bridge.ErrorMsgs)
            raise DatabaseError(
                f"Error importing from SWMM file.\n{e!s}\n{messages}"
            ) from None
        if not result:
            messages = "\n".join(inp_bridge.ErrorMsgs)
            raise DatabaseError(f"Error importing from SWMM file.\n{messages}")


def _projection_for_srid(srid: int) -> str:
    """Look up the WKT MIKE+ has for a projected SRID.

    Uses a throwaway database, so it can run before any target file is touched.

    Returns
    -------
    str
        The projection as OGC WKT.

    Raises
    ------
    ValueError
        If MIKE+ doesn't know the SRID or it is a geographic system.
    """
    with tempfile.TemporaryDirectory(ignore_cleanup_errors=True) as tmp:
        data_source = BaseDataSource.Create(str(Path(tmp) / "srid.sqlite"))
        data_source.CreateDatabase()
        data_source.OpenDatabase()
        try:
            wkt = str(data_source.GetProjectionOGCWKT(srid) or "")
        finally:
            data_source.CloseDatabase()

    if not wkt.startswith(("PROJCS[", "GEOGCS[")):
        raise ValueError(f"SRID {srid} is not a coordinate system MIKE+ knows.")
    # MIKE+ would silently store Google Maps - Mercator instead.
    if wkt.startswith("GEOGCS["):
        raise ValueError(
            f"SRID {srid} is a geographic coordinate system, which MIKE+ models don't "
            "support. Use a projected one, e.g. 3857 or a UTM zone."
        )
    return wkt


def _save_srid(data_source: BaseDataSource, srid: int) -> None:
    """Store `srid` on a newly created database.

    `CreateModelTables` leaves the SRID at -1 whatever it is given, which also
    makes later geometry writes use -1.
    """
    srid = int(srid)
    data_source.ExecuteSqlNonQuery(
        f"UPDATE m_Configuration SET ValueInt = {srid} WHERE MUID = 'SRID'", None
    )
    data_source.ExecuteSqlNonQuery(f"UPDATE geometry_columns SET srid = {srid}", None)


def _ensure_mupp_file(data_source: BaseDataSource) -> Path:
    """Write a minimal .mupp beside an open data source's database if it has none.

    Returns
    -------
    Path
        Path to the project file.

    Raises
    ------
    DatabaseError
        If MIKE+ fails to write the project file.
    """
    sqlite_path = Path(str(data_source.DbFileName)).resolve()
    mupp_path = sqlite_path.with_suffix(".mupp")
    if mupp_path.exists():
        return mupp_path

    try:
        import clr

        clr.AddReference("DHI.Amelia.ProjectLoaderPFS.Interface")
        from DHI.Amelia.ProjectLoaderPFS.Interface.Services import ServicesFactory

        project_file = ServicesFactory.CreateProjectFileOper()
        module_data = project_file.ProjectRootNodeData.ModuleData
        module_data.DBType = DataBaseType.SpatiaLite
        module_data.DBName = mupp_path.stem
        # PFS garbles forward-slash Windows paths when it makes them relative
        module_data.DBFilePath = str(sqlite_path)
        module_data.ModelType = data_source.ActiveModel
        module_data.Ubg = data_source.UnitSystemOption
        module_data.CreateNewDB = False
        written = project_file.Write(str(mupp_path))
    except Exception as e:
        raise DatabaseError(
            f"Failed to create project file: {mupp_path}.\n{e!s}"
        ) from e
    # Write() reports success even when it writes nothing
    if not written or not mupp_path.exists():
        raise DatabaseError(f"Failed to create project file: {mupp_path}.")
    return mupp_path


__all__ = [
    "Database",
    "DatabaseError",
]
