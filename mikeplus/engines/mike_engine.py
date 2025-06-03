"""MikeEngine class for unified engine operations across all MIKE+ simulation types."""

from __future__ import annotations

import time
from typing import List, Optional, Tuple, Any, Union
from pathlib import Path
from DHI.Amelia.Tools.EngineTool import EngineTool
from DHI.Amelia.GlobalUtility.DataType import MUSimulationOption
from System.Threading import CancellationTokenSource
from DHI.Amelia.DomainServices.Interface.SharedEntity import DhiEngineSimpleLauncher
from System import Object


from ..database import Database


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
    
    def run_cs(self, sim_muid: str | None = None) -> list[Path]:
        """Run simulations for 'Rivers, collection system and overland flows'.

        Parameters
        ----------
        sim_muid : str, optional
            Simulation MUID. If None, uses the active simulation MUID.

        Returns
        -------
        list[Path]
            List of result file paths as Path objects.
        """
        sim_muid = self._get_sim_muid(sim_muid)
        
        # CS is a special case that returns launcher directly
        success, launcher, messages = self._engine_tool.RunEngine_CS(None, None, sim_muid)
        
        self._handle_engine_launch(success, launcher, messages)
        self._wait_for_engine_completion(launcher)
        
        return self._get_result_files("msm_Project", sim_muid)
    
    def run_epanet(self, sim_muid: str | None = None) -> list[Path]:
        """Run EPANET simulation.

        Parameters
        ----------
        sim_muid : str, optional
            Simulation MUID. If None, uses the active simulation MUID.

        Returns
        -------
        list[Path]
            List of result file paths as Path objects.
        """
        sim_muid = self._get_sim_muid(sim_muid)
        
        launcher = DhiEngineSimpleLauncher()   
        success, messages = self._engine_tool.RunEngine_AllEpanet(
            MUSimulationOption.WD_EPANET,
            CancellationTokenSource().Token,
            launcher=launcher,
            simMuid=sim_muid,
        )
        
        self._handle_engine_launch(success, launcher, messages)
        self._wait_for_engine_completion(launcher)
        
        return self._get_result_files("mw_Project", sim_muid)
    
    def run_swmm(self, sim_muid: Optional[str] = None) -> List[Path]:
        """Run SWMM simulation.

        Parameters
        ----------
        sim_muid : str, optional
            Simulation MUID. If None, uses the active simulation MUID.

        Returns
        -------
        List[Path]
            List of result file paths as Path objects.
        """
        sim_muid = self._get_sim_muid(sim_muid)
        
        launcher = DhiEngineSimpleLauncher()
        success, messages = self._engine_tool.RunEngine_AllSWMM(
            CancellationTokenSource().Token, 
            launcher=launcher,
            simMuid=sim_muid,
        )

        self._handle_engine_launch(success, launcher, messages)
        self._wait_for_engine_completion(launcher)
        
        return self._get_result_files("mss_Project", sim_muid)
        
    def _get_sim_muid(self, sim_muid: Optional[str]) -> str:
        """Get the simulation MUID, defaulting to active simulation if None.
        
        Parameters
        ----------
        sim_muid : str, optional
            Simulation MUID. If None, uses the active simulation MUID.
            
        Returns
        -------
        str
            The simulation MUID to use.
        """
        if sim_muid is None:
            return self._database.active_simulation
        return sim_muid
    
    def _handle_engine_launch(self, success: bool, launcher: DhiEngineSimpleLauncher, 
                             messages: Union[List[str], Object]) -> None:
        """Handle the engine launch result.
        
        Parameters
        ----------
        success : bool
            Whether the engine launch was successful.
        launcher : DhiEngineSimpleLauncher
            The engine launcher.
        messages : List[str] or System.Object
            Error messages if the launch failed.
            
        Raises
        ------
        RuntimeError
            If the engine launch failed.
        """
        if not success or launcher is None:
            messages_list = list(messages) if messages else []
            messages_str = ". ".join(messages_list) if messages_list else "Unknown error"
            raise RuntimeError(f"Simulation failed to start: {messages_str}")
        
        launcher.Start()
    
    def _wait_for_engine_completion(self, launcher: DhiEngineSimpleLauncher) -> None:
        """Wait for the engine to complete.
        
        Parameters
        ----------
        launcher : DhiEngineSimpleLauncher
            The engine launcher.
        """
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
    
    def _get_result_files(self, project_table_name: str, sim_muid: str) -> List[Path]:
        """Get the result files from the project table.
        
        Parameters
        ----------
        project_table_name : str
            Name of the project table (e.g., "msm_Project").
        sim_muid : str
            Simulation MUID.
            
        Returns
        -------
        List[Path]
            List of result file paths as Path objects.
        """
        project_table = getattr(self._database.tables, project_table_name)._net_table
        result_files = list(project_table.GetResultFilePath(muid=sim_muid).Values)
        return [Path(f) for f in result_files]
