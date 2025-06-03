"""Engine1D class for running MIKE 1D simulation."""

from pathlib import Path
from typing import Any
import time

from DHI.Amelia.Tools.EngineTool import EngineTool

from ..dotnet import get_implementation
from ..database import Database

DataTableContainer = Any
class Engine1D:
    """Engine1D class for running MIKE 1D simulation."""

    def __init__(self, database: Database | DataTableContainer):
        """Initialize the Engine1D class with the given Database.

        Parameters
        ----------
        database : Database or DataTableContainer
            A Database object for the MIKE+ model, or for backward compatibility,
            a DataTables object from DataTableAccess.

        Examples
        --------
        >>>from mikeplus import Database
        >>>db = Database("path/to/model.sqlite")
        >>>engine = Engine1D(db)
        
        """
        self._data_tables = self._get_data_tables(database)

    def _get_data_tables(self, database: Database | DataTableContainer) -> DataTableContainer:
        """Get proper DataTableContainer, working with deprecated DataTableAccess workflow."""
        if isinstance(database, Database):
            if not database.is_open:
                database.open()
            return database._data_table_container

        # if not Database object, assume user passed DataTableAccess.datatables per previous workflow
        return database
    
    def run(self, sim_muid: str | None = None):
        """Run MIKE1D simulation.

        Parameters
        ----------
        sim_muid : string, optional
            simulation muid, it will use the current active simulation muid if sim_muid is None, by default None.

        Examples
        --------
        # Using Database object (preferred)
        >>>from mikeplus import Database
        >>>db = Database("path/to/model.sqlite")
        >>>engine = Engine1D(db)
        >>>engine.run()
        >>>db.close()

        """
        if sim_muid is None:
            sim_muid = self.get_active_sim_muid()

        engine_tool = EngineTool()
        engine_tool.DataTables = self._data_tables
        
        success, launcher, messages = engine_tool.RunEngine_CS(None, None, sim_muid)

        if not success or launcher is None:
            messages = ". ".join(list(messages))
            raise RuntimeError(f"Simulation failed to start: {messages}")
        
        launcher.Start()
            
        start_time = time.time()
        timeout_start = 30.0 
        time.sleep(0.5)
        while not launcher.IsEngineRunning:
            if time.time() - start_time > timeout_start:
                break
            time.sleep(0.1)
            
        while launcher.IsEngineRunning:
            time.sleep(0.1)

        result_files = self.get_result_files(sim_muid)
        return result_files

    def get_result_files(self, sim_muid: str | None = None) -> list[Path]:
        """Get result files for a simulation MUID.
        
        Parameters
        ----------
        sim_muid : str, optional
            Simulation MUID. If None, uses the active simulation MUID.
            
        Returns
        -------
        list
            List of result file paths as Path objects.
        """
        if sim_muid is None:
            sim_muid = self.get_active_sim_muid()
            
        project_table = self._data_tables["msm_Project"]
        project_table = get_implementation(project_table)
        res_files_dictionary = project_table.GetResultFilePath(sim_muid)
        res_files = []
        for item in res_files_dictionary:
            res_files.append(Path(item.Value).absolute())
        
        return res_files

    def get_active_sim_muid(self) -> str:
        """Get the active simulation MUID from the database.
        
        Returns
        -------
        str
            The active simulation MUID.
            
        Raises
        ------
        ValueError
            If no active simulation MUID is found.
        """
        muid = self._data_tables["msm_Project"].GetMuidsWhere("ActiveProject=1")
        if muid is None or muid.Count == 0:
            raise ValueError("No active simulation found in the database.")
        return muid[0]
