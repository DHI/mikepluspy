"""MikeEngine class for unified engine operations across all MIKE+ simulation types."""

from __future__ import annotations

import time
from typing import List, Optional
from pathlib import Path
from unittest import result

from DHI.Amelia.Tools.EngineTool import EngineTool
from System.Collections.Generic import List as DotNetList

from ..database import Database
from ..dotnet import get_implementation


class MikeEngine:
    """Unified engine class for running all types of MIKE+ simulations."""

    def __init__(self, database: Database):
        """Initialize the MikeEngine class with a Database object.

        Parameters
        ----------
        database : Database
            A Database object for the MIKE+ model.

        Examples
        --------
        >>> from mikeplus import Database
        >>> db = Database("path/to/model.sqlite")
        >>> engine = MikeEngine(db)
        """          
        self._database = database
        self._engine_tool = EngineTool()
        self._engine_tool.DataTables = self._database._data_table_container
    
    def run_1d(self, sim_muid: str | None = None) -> list[Path]:
        """Run MIKE 1D simulation.

        Parameters
        ----------
        sim_muid : str, optional
            Simulation MUID. If None, uses the active simulation MUID.

        Returns
        -------
        list[Path]
            List of result file paths as Path objects.
        """
        if sim_muid is None:
            sim_muid = self._database.active_simulation

        success, launcher, messages = self._engine_tool.RunEngine_CS(None, None, sim_muid)

        if not success or launcher is None:
            messages_str = ". ".join(list(messages)) if messages else "Unknown error"
            raise RuntimeError(f"Simulation failed to start: {messages_str}")

        launcher.Start()

        # Wait for the engine to start
        start_time = time.time()
        timeout_start = 30.0
        time.sleep(0.5)
        while not launcher.IsEngineRunning:
            if time.time() - start_time > timeout_start:
                break
            time.sleep(0.1)

        # Wait for the engine to complete
        while launcher.IsEngineRunning:
            time.sleep(0.1)

        # Get result files
        project_table = self._database.tables.msm_Project._net_table
        result_files = list(project_table.GetResultFilePath(muid=sim_muid).Values)
        return [Path(f) for f in result_files]
    
    def run_epanet(self, sim_muid: Optional[str] = None, verbose: bool = False) -> List[Path]:
        """Run EPANET simulation.

        Parameters
        ----------
        sim_muid : str, optional
            Simulation MUID. If None, uses the active simulation MUID.
        verbose : bool, optional
            Print log file or not.

        Returns
        -------
        List[Path]
            List of result file paths as Path objects.
        """
        # Stub implementation
        return []
    
    def run_swmm(self, sim_muid: Optional[str] = None, verbose: bool = False) -> List[Path]:
        """Run SWMM simulation.

        Parameters
        ----------
        sim_muid : str, optional
            Simulation MUID. If None, uses the active simulation MUID.
        verbose : bool, optional
            Print log file or not.

        Returns
        -------
        List[Path]
            List of result file paths as Path objects.
        """
        # Stub implementation
        return []
    
    def run_flood(self, sim_muid: Optional[str] = None, verbose: bool = False) -> List[Path]:
        """Run 1D/2D/Flood simulation.

        Parameters
        ----------
        sim_muid : str, optional
            Simulation MUID. If None, uses the active simulation MUID.
        verbose : bool, optional
            Print log file or not.

        Returns
        -------
        List[Path]
            List of result file paths as Path objects.
        """
        # Stub implementation
        return []
