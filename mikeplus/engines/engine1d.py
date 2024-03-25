from pathlib import Path
import subprocess
from DHI.Mike.Install import MikeImport, MikeProducts


class Engine1D:
    """The Engine1D class can run MIKE1D simulation, print log file, and get the result file path.
    """
    def __init__(self,
                 dataTables):
        MikeImport.Setup(22, MikeProducts.MikePlus)
        self._dataTables = dataTables
        self._result_file = None

    def run(self,
            simMuid=None, verbose=False):
        """Run MIKE1D simulation

        Parameters
        ----------
        simMuid : string, optional
            simulation muid, it will use the current active simulation muid if simMuid is None, by default None.
        verbose : bool, optional
            print log file or not, by default False.

        Examples
        --------
        >>>data_access = DataTableAccess(muppOrSqlite)
        >>>data_access.open_database()
        >>>engine = Egnine1D(data_access.datatables)
        >>>engine.run()
        >>>data_access.close_database()
        """
        if simMuid is None:
            muid = self._dataTables["msm_Project"].GetMuidsWhere("ActiveProject=1")
            if muid is None and muid.Count == 0:
                raise ValueError("Simulation id can't be none.")
            simMuid = muid[0]

        product_info = MikeImport.ActiveProduct()
        mike1d_exec = Path(product_info.InstallRoot) / 'bin' / 'x64' / 'DHI.Mike1D.Application.exe'
        dbOrMuppFile = Path(self._dataTables.DataSource.BaseFullPath)
        dir = dbOrMuppFile.parent
        file_name = dbOrMuppFile.stem
        log_file = Path(dir) / f"{file_name}_{simMuid}.log"
        self._result_file = Path(dir) / f"{file_name}_{simMuid}.res1d"
        if verbose:
            print(f"Simulation is started. Simulation id is '{simMuid}'.")
        subprocess.run([mike1d_exec, str(dbOrMuppFile), f"-simulationid={simMuid}", f"-logfilename={log_file}"])
        if verbose:
            if self._print_log(log_file) is False:
                print("Simulation is finished without logFile generated.")
                
    @property
    def result_file(self):
        """Get the current simulation result file path

        Returns
        -------
        string
            The result file path of current simulation
        """
        return self._result_file

    def _print_log(self, logFile):
        if Path(logFile).exists():
            with open(logFile) as f:
                lines = f.readlines()
                for line in lines:
                    print(line)
            return True
        else:
            return False
