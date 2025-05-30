"""Engine1D class for running MIKE 1D simulation."""

from pathlib import Path
import subprocess
from DHI.Mike.Install import MikeImport
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
        self._result_file = None

    def _get_data_tables(self, database):
        """Get proper DataTableContainer, working with deprecated DataTableAccess workflow."""
        if isinstance(database, Database):
            if not database.is_open:
                database.open()
            return database._data_table_container

        # if not Database object, assume user passed DataTableAccess.datatables per previous workflow
        return database
        
        
    def run(self, simMuid=None, verbose=False):
        """Run MIKE1D simulation.

        Parameters
        ----------
        simMuid : string, optional
            simulation muid, it will use the current active simulation muid if simMuid is None, by default None.
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
        if simMuid is None:
            muid = self._dataTables["msm_Project"].GetMuidsWhere("ActiveProject=1")
            if muid is None and muid.Count == 0:
                raise ValueError("Simulation id can't be none.")
            simMuid = muid[0]

        product_info = MikeImport.ActiveProduct()
        mike1d_exec = (
            Path(product_info.InstallRoot)
            / "bin"
            / "x64"
            / "DHI.Mike1D.Application.exe"
        )
        dbOrMuppFile = Path(self._dataTables.DataSource.BaseFullPath)
        dir = dbOrMuppFile.parent
        file_name = dbOrMuppFile.stem
        log_file = Path(dir) / f"{file_name}_{simMuid}.log"
        self._result_file = Path(dir) / f"{file_name}_{simMuid}.res1d"
        if verbose:
            print(f"Simulation is started. Simulation id is '{simMuid}'.")
        subprocess.run(
            [
                mike1d_exec,
                str(dbOrMuppFile),
                f"-simulationid={simMuid}",
                f"-logfilename={log_file}",
            ]
        )
        if verbose:
            if self._print_log(log_file) is False:
                print("Simulation is finished without logFile generated.")

    @property
    def result_file(self):
        """Get the current simulation result file path.

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
