"""FloodEngine class for running 1D/2D/FLOOD simulation."""

import os.path
import time
from pathlib import Path
from DHI.Amelia.Tools.EngineTool import EngineTool
from DHI.Amelia.DataModule.Interface.Services import IMsmProjectTable
from DHI.Amelia.DomainServices.Interface.SharedEntity import DhiEngineSimpleLauncher
from DHI.Amelia.GlobalUtility.DataType import MUSimulationOption
from System.Collections.Generic import List


class FloodEngine:
    """FloodEngine class for running 1D/2D/FLOOD simulation."""

    def __init__(self, data_tables):
        """Initialize the FloodEngine class with the given DataTables.

        Parameters
        ----------
        data_tables : DataTables
            The DataTables object containing the data tables.

        Examples
        --------
        >>>engine = FloodEngine(data_access.datatables)
        
        """
        self._data_tables = data_tables
        self._result_files = None

    def run(self, sim_muid=None, verbose=False):
        """Run 1D/2D/Flood simulation.

        Parameters
        ----------
        sim_muid : string, optional
            simulation muid, it will use the current active simulation muid if simMuid is None, by default None.
        verbose : bool, optional
            print log file or not, by default False.

        Examples
        --------
        >>>data_access = DataTableAccess(muppOrSqlite)
        >>>data_access.open_database()
        >>>engine = FloodEngine(data_access.datatables)
        >>>engine.run()
        >>>data_access.close_database()

        """
        if sim_muid is None:
            sim_muid = self._get_active_muid()
            if sim_muid is None:
                raise ValueError("Simulation id can't be none.")
        if verbose:
            print("Simulation id is " + sim_muid)

        engine_tool = EngineTool()
        engine_tool.DataTables = self._data_tables
        msg = List[str]()
        launcher = DhiEngineSimpleLauncher()
        success, launcher, msg = engine_tool.RunEngine_CS(launcher, msg, sim_muid)
        if success and launcher is not None:
            launcher.Start()
        elif msg is not None and verbose:
            joined_msg = "\n".Join(msg)
            print(joined_msg)

        if self._result_files is None:
            self._result_files = self._get_result_files(sim_muid)

        engine_start = False
        while not launcher.IsEngineRunning:
            time.sleep(1)
        engine_start = True

        while engine_start and not launcher.IsEngineExit:
            time.sleep(1)

        if verbose:
            for log_file in self._get_log_files(sim_muid, launcher.SimulationOption):
                self._print_log(log_file)

    def _get_active_muid(self):
        muid = self._data_tables["msm_Project"].GetMuidsWhere("ActiveProject=1")
        if muid is None and muid.Count == 0:
            return None
        return muid[0]

    def _get_result_files(self, sim_muid):
        project = self._data_tables["msm_Project"]
        prj = IMsmProjectTable(project)
        res_files_dictionary = prj.GetResultFilePath(sim_muid)
        res_files = []
        for item in res_files_dictionary:
            res_files.append(os.path.abspath(item.Value))
        return res_files

    def _get_log_files(self, sim_muid, sim_option):
        db_mupp_file = Path(self._data_tables.DataSource.BaseFullPath)
        dir = db_mupp_file.parent
        file_name = db_mupp_file.stem
        prefix = Path(dir) / f"{file_name}_{sim_muid}"
        log_files = []
        if sim_option == MUSimulationOption.CS_MIKE_1D:
            log_files.append(f"{prefix}.log")
        elif sim_option == MUSimulationOption.CS_MIKE_21FM:
            log_files.append(f"{prefix}_m21fm.log")
        elif (
            sim_option == MUSimulationOption.CS_MIKE_COUPLING
            or sim_option == MUSimulationOption.CS_MIKE_COUPLING_21FMModelLink
        ):
            log_files.append(f"{prefix}_m1d.log")
            log_files.append(f"{prefix}_m21fm.log")
            log_files.append(f"{prefix}_mf.log")

        for file in log_files:
            if not os.path.exists(file):
                log_files.remove(file)
        return log_files

    def _print_log(self, log_file):
        if os.path.exists(log_file):
            with open(log_file) as f:
                lines = f.readlines()
                for line in lines:
                    print(line)
            return True
        else:
            return False

    @property
    def result_files(self):
        """Get the current simulation result files path.

        Returns
        -------
        string list
            The result files path of current simulation

        """
        if self._result_files is None:
            sim_muid = self._get_active_muid()
            self._result_files = self._get_result_files(sim_muid)
        return self._result_files
