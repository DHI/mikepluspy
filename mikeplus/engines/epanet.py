import os.path
from DHI.Amelia.DomainServices.Services import AmeliaEngineService
from DHI.Amelia.DomainServices.Services import AmeliaDataService
from DHI.Amelia.GlobalUtility.DataType import MUSimulationOption
from DHI.Amelia.DataModule.Interface.Services import IMwProjectTable
from System.Threading import CancellationTokenSource
from System.Collections.Generic import List


class EPANET:
    """The EPANET class can run EPANET simulation, get active simulation muid, print log file, and get the result file path.
    """
    def __init__(self,
                 dataTables):
        self._dataTables = dataTables
        self._result_file = None

    def run_engine_epanet(self,
                          simMuid=None):
        """Run EPANET simulation

        Parameters
        ----------
        simMuid : string, optional
            simulation muid, it will use the current active simulation muid if simMuid is None, by default None
        
        Examples
        --------
        >>>data_access = DataTableAccess(muppOrSqlite)
        >>>data_access.open_database()
        >>>engine = EPANET(data_access.datatables)
        >>>engine.run_engine_epanet()
        >>>data_access.close_database()        
        """
        if simMuid is None:
            simMuid = self._get_active_muid()
            if simMuid is None:
                print("Simulation id can't be none.")
                return
        print("Simulation id is " + simMuid)
        data_service = AmeliaDataService()
        data_service.DataTables = self._dataTables
        engine_service = AmeliaEngineService()
        engine_service.DataTables = self._dataTables
        engine_service.DataService = data_service
        cancel_source = CancellationTokenSource()
        msg = List[str]()
        success = engine_service.RunEngine_AllEpanet(MUSimulationOption.WD_EPANET, cancel_source.Token, msg, None, None, None, simMuid, None, None)
        if self._result_file is None:
            self._result_file = self._get_result_file(simMuid)
        dir = os.path.dirname(os.path.abspath(self._result_file))
        file_name = os.path.splitext(os.path.split(self._result_file)[1])[0]
        log_file = os.path.join(dir, file_name + '.log')
        if self._print_log(log_file) is False:
            if (success is False):
                print("Simulation failed.")
            else:
                print("Simulation is finished without logFile generated.")

    @property
    def result_file(self):
        """Get the current simulation result file path

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
        """Print log to specified path

        Parameters
        ----------
        log_file : string
            Log file path

        Returns
        -------
        bool
            Return true when print log successfully, otherwise false.
        """
        if os.path.exists(log_file):
            with open(log_file) as f:
                lines = f.readlines()
                for line in lines:
                    print(line)
            return True
        else:
            return False

    def _get_result_file(self, simMuid):
        """Get result file path of specified simulation 

        Parameters
        ----------
        simMuid : string
            simulation muid

        Returns
        -------
        string
            The result file path of the specified simulation
        """
        project = self._dataTables["mw_Project"]
        prj = IMwProjectTable(project)
        res_file = prj.GetEpanetResultFilePath(MUSimulationOption.WD_EPANET, None, simMuid)
        return os.path.abspath(res_file)

    def _get_active_muid(self):
        """Get the active simulation muid

        Returns
        -------
        string
            The active simulation muid
        """
        muid = self._dataTables["mw_Project"].GetMuidsWhere("ActiveProject=1")
        if muid is None and muid.Count == 0:
            return None
        return muid[0]
