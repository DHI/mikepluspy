"""Engine1D class for running MIKE 1D simulation."""

from pathlib import Path
import time
import os.path
from DHI.Amelia.Tools.EngineTool import EngineTool
from DHI.Amelia.DataModule.Interface.Services import IMsmProjectTable
from ..database import Database


class Engine1D:
    """Engine1D class for running MIKE 1D simulation."""

    def __init__(self, database):
        """Initialize the Engine1D class with the given Database.

        Parameters
        ----------
        database : Database or DataTables
            A Database object for the MIKE+ model, or for backward compatibility,
            a DataTables object from DataTableAccess.

        Examples
        --------
        >>>from mikeplus import Database
        >>>db = Database("path/to/model.sqlite")
        >>>engine = Engine1D(db)
        
        """
        self._dataTables = self._get_data_tables(database)
        self._result_files = None
        self._active_sim_muid = None

    def _get_data_tables(self, database):
        """Get proper DataTableContainer, working with deprecated DataTableAccess workflow."""
        if isinstance(database, Database):
            if not database.is_open:
                database.open()
            return database._data_table_container

        # if not Database object, assume user passed DataTableAccess.datatables per previous workflow
        return database
        
        
    def get_active_sim_muid(self):
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
        if self._active_sim_muid is None:
            muid = self._dataTables["msm_Project"].GetMuidsWhere("ActiveProject=1")
            if muid is None or muid.Count == 0:
                raise ValueError("No active simulation found in the database.")
            self._active_sim_muid = muid[0]
        return self._active_sim_muid
    
    def run(self, sim_muid=None, verbose=False):
        """Run MIKE1D simulation.

        Parameters
        ----------
        sim_muid : string, optional
            simulation muid, it will use the current active simulation muid if sim_muid is None, by default None.
        verbose : bool, optional
            print log file or not, by default False.

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

        if verbose:
            print(f"Simulation is started. Simulation id is '{sim_muid}'.")

        engine_tool = EngineTool()
        engine_tool.DataTables = self._dataTables
        
        # Run the engine - use None for out parameters
        # Pythonnet will return new instances for launcher and messages
        success, launcher, messages = engine_tool.RunEngine_CS(None, None, sim_muid)
        
        if success and launcher is not None:
            launcher.Start()
        elif messages is not None and verbose:
            joined_msg = "\n".join(messages)
            print(joined_msg)
            
        # Get result file paths from the database
        if self._result_files is None:
            self._result_files = self._get_result_files(sim_muid)
            
        # Get log file path
        db_file_path = Path(self._dataTables.DataSource.BaseFullPath)
        directory = db_file_path.parent
        file_name = db_file_path.stem
        log_file = directory / f"{file_name}_{sim_muid}.log"
        
        # Wait for engine to start with timeout
        start_time = time.time()
        timeout_start = 10.0  # 10 seconds timeout for starting
        
        # First wait a little to give the launcher thread time to initialize
        time.sleep(0.5)
        
        # Then check if it's running with a timeout
        while not launcher.IsEngineRunning:
            if time.time() - start_time > timeout_start:
                if verbose:
                    print(f"Warning: Engine did not start within {timeout_start} seconds")
                break
            time.sleep(0.1)
            
        # If engine is running, wait for it to complete
        if launcher.IsEngineRunning:
            while not launcher.IsEngineExit:
                time.sleep(0.1)
                # Check if the engine is still running to catch any errors
                if not launcher.IsEngineRunning and not launcher.IsEngineExit:
                    if verbose:
                        print("Warning: Engine stopped unexpectedly")
                    break
            
        if verbose:
            if self._print_log(log_file) is False:
                print("Simulation is finished without logFile generated.")

    def _get_result_files(self, sim_muid):
        """Get result files for the given simulation muid.

        Parameters
        ----------
        sim_muid : str
            Simulation muid.

        Returns
        -------
        list
            List of result file paths.
        """
        project = self._dataTables["msm_Project"]
        prj = IMsmProjectTable(project)
        res_files_dictionary = prj.GetResultFilePath(sim_muid)
        res_files = []
        for item in res_files_dictionary:
            res_files.append(os.path.abspath(item.Value))
        return res_files

    @property
    def result_files(self):
        """Get the current simulation result files path.

        Returns
        -------
        list
            The result files path of current simulation

        """
        if self._result_files is None:
            sim_muid = self.get_active_sim_muid()
            self._result_files = self._get_result_files(sim_muid)
        return self._result_files
        
    def get_result_files(self, sim_muid=None):
        """Get result files for a specific simulation MUID.
        
        Parameters
        ----------
        sim_muid : str, optional
            Simulation MUID. If None, uses the active simulation MUID.
            
        Returns
        -------
        list
            List of result file paths.
        """
        if sim_muid is None:
            sim_muid = self.get_active_sim_muid()
        return self._get_result_files(sim_muid)

    def _print_log(self, log_file):
        """Print the contents of a log file if it exists.
        
        Parameters
        ----------
        log_file : str or Path
            Path to the log file.
            
        Returns
        -------
        bool
            True if the log file exists and was printed, False otherwise.
        """
        if Path(log_file).exists():
            with open(log_file) as f:
                for line in f:
                    print(line, end="")
            return True
        return False
