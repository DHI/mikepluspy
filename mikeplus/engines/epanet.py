"""
EPANET class for running EPANET simulation.

.. deprecated:: 2025.1.0
   The 'mikeplus.engines.epanet' module is deprecated to simplify the codebase and provide a more simulation-oriented API.
   Please use 'mikeplus.simulation_runner.SimulationRunner' or 'Database.run()' for EPANET simulations.
   This module will be removed in version 2026.0.0.
"""
from __future__ import annotations

import os.path
import warnings

from DHI.Amelia.Tools.EngineTool import EngineTool
from DHI.Amelia.GlobalUtility.DataType import MUSimulationOption
from DHI.Amelia.DataModule.Interface.Services import IMwProjectTable
from System.Threading import CancellationTokenSource
from System.Collections.Generic import List

from ..database import Database

class EPANET:
    """EPANET class for running EPANET simulation."""

    def __init__(self, database):
        warnings.warn(
            "The 'EPANET' class is deprecated since version 2025.1.0 and will be removed in version 2026.0.0. "
            "It was deprecated to simplify the codebase and provide a more simulation-oriented API. "
            "Please use 'mikeplus.simulation_runner.SimulationRunner' or 'Database.run()' for EPANET simulations.",
            DeprecationWarning,
            stacklevel=2
        )
        """Initialize the EPANET class with the given Database.

        Parameters
        ----------
        database : Database or DataTables
            A Database object for the MIKE+ model, or for backward compatibility,
            a DataTables object from DataTableAccess.

        Examples
        --------
        >>>from mikeplus import Database
        >>>db = Database("path/to/model.sqlite")
        >>>engine = EPANET(db)

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

    def run_engine_epanet(self, simMuid=None, verbose=False):
        """Run EPANET simulation.

        Parameters
        ----------
        simMuid : string, optional
            simulation muid, it will use the current active simulation muid if simMuid is None, by default None
        verbose : bool, optional
            print log file or not, by default False

        Examples
        --------
        >>>from mikeplus import Database
        >>>db = Database("path/to/model.sqlite")
        >>>engine = EPANET(db)
        >>>engine.run_engine_epanet()
        >>>db.close()

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
        success = engine_tool.RunEngine_AllEpanet(
            MUSimulationOption.WD_EPANET,
            cancel_source.Token,
            msg,
            None,
            None,
            None,
            simMuid,
            None,
            None,
        )
        if self._result_file is None:
            self._result_file = self._get_result_file(simMuid)
        dir = os.path.dirname(os.path.abspath(self._result_file))
        file_name = os.path.splitext(os.path.split(self._result_file)[1])[0]
        log_file = os.path.join(dir, file_name + ".log")
        if verbose:
            log_file_made = self._print_log(log_file)

            if not success:
                print("Simulation failed.")

            if not log_file_made:
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
        project = self._dataTables["mw_Project"]
        prj = IMwProjectTable(project)
        res_file = prj.GetEpanetResultFilePath(
            MUSimulationOption.WD_EPANET, None, simMuid
        )
        return os.path.abspath(res_file)

    def _get_active_muid(self):
        muid = self._dataTables["mw_Project"].GetMuidsWhere("ActiveProject=1")
        if muid is None and muid.Count == 0:
            return None
        return muid[0]
