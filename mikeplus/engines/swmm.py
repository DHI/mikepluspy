import os.path
from DHI.Amelia.Tools.EngineTool import EngineTool
from DHI.Amelia.DataModule.Interface.Services import IMProjectTable
from System.Threading import CancellationTokenSource
from System.Collections.Generic import List


class SWMM:
    """The SWMM class can run SWMM simulation, get active simulation muid, print log file, and get the result file path."""

    def __init__(self, dataTables):
        self._dataTables = dataTables
        self._result_file = None

    def run(self, simMuid=None, verbose=False):
        """Run SWMM simulation.

        Parameters
        ----------
        simMuid : string, optional
            simulation muid, it will use the current active simulation muid if simMuid is None, by default None
        verbose : bool, optional
            print log file or not, by default False

        Examples
        --------
        >>>data_access = DataTableAccess(muppOrSqlite)
        >>>data_access.open_database()
        >>>engine = SWMM(data_access.datatables)
        >>>engine.run()
        >>>data_access.close_database()

        """
        if simMuid is None:
            simMuid = self._get_active_muid()
            if simMuid is None:
                raise ValueError("Simulation id can't be none.")

        if verbose:
            print("Simulation id is " + simMuid)
        engine_tool = EngineTool()
        engine_tool.DataTables = self._dataTables
        cancel_source = CancellationTokenSource()
        msg = List[str]()
        success = engine_tool.RunEngine_AllSWMM(
            cancel_source.Token, msg, None, None, None, simMuid, None, None
        )
        if self._result_file is None:
            self._result_file = self._get_result_file(simMuid)
        dir = os.path.dirname(os.path.abspath(self._result_file))
        file_name = os.path.splitext(os.path.split(self._result_file)[1])[0]
        log_file = os.path.join(dir, file_name + ".log")
        if verbose:
            if not success:
                print("Simulation failed.")

            log_file_made = self._print_log(log_file)
            if log_file_made is False:
                print("Simulation is finished without logFile generated.")

    @property
    def result_file(self):
        """Get the current simulation result file path.

        Returns
        -------
        string
            The result file path of current simulation

        """
        if self._result_file is None:
            simMuid = self._get_active_muid()
            self._result_file = self._get_result_file(simMuid)
        return self._result_file

    def _print_log(self, log_file):
        if os.path.exists(log_file):
            with open(log_file) as f:
                lines = f.readlines()
                for line in lines:
                    print(line)
            return True
        else:
            return False

    def _get_result_file(self, simMuid):
        project = self._dataTables["mss_Project"]
        prj = IMProjectTable(project)
        res_files = prj.GetResultFilePath(simMuid)
        res_file = None
        for item in res_files:
            res_file = item.Value
        return os.path.abspath(res_file)

    def _get_active_muid(self):
        muid = self._dataTables["mss_Project"].GetMuidsWhere("ActiveProject=1")
        if muid is None and muid.Count == 0:
            return None
        return muid[0]
