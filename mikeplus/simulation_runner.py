"""SimulationRunner for executing MIKE+ simulations."""

from __future__ import annotations

import time
from pathlib import Path
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .database import Database

from System import Enum
from System import String
from System.Collections.Generic import List
from System.Threading import CancellationTokenSource
from DHI.Amelia.Tools.EngineTool import EngineTool
from DHI.Amelia.GlobalUtility.DataType import MUSimulationOption
from DHI.Amelia.GlobalUtility.DataType import MUModelOption
from DHI.Amelia.DomainServices.Interface.SharedEntity import DhiEngineSimpleLauncher
class SimulationRunner:
    """Runs MIKE+ simulations."""

    def __init__(self, database: Database):
        """Initializes SimulationRunner with a MIKE+ database.

        Parameters
        ----------
        database : Database
            MIKE+ model database.

        Examples
        --------
        >>> from mikeplus import Database
        >>> from mikeplus.engines import SimulationRunner
        >>> db = Database("path/to/model.sqlite")
        >>> runner = SimulationRunner(db)
        """          
        self._database = database
        self._engine_tool = EngineTool()
        self._engine_tool.DataTables = self._database._data_table_container

    def run(self, muid: str | None = None, model_option: str | None = None) -> list[Path]:
        """Runs a simulation.

        Parameters
        ----------
        muid : str, optional
            Simulation MUID. Defaults to the active simulation.
        model_option : str | MUModelOption, optional
            Model option. Defaults to None.

        Returns
        -------
        list[Path]
            Paths to the result files.
        """
        if model_option is None:
            model_option = self._database.active_model
        
        try:
            model_option = Enum.Parse(MUModelOption, model_option)
        except ValueError:
            possible_options = ", ".join(Enum.GetNames(MUModelOption))
            raise ValueError(f"Invalid model option: {model_option}. Valid options: {possible_options}")

        if model_option == MUModelOption.CS_MIKE1D:
            return self.run_cs(muid)
        elif model_option == MUModelOption.CS_SWMM:
            return self.run_swmm(muid)
        elif model_option == MUModelOption.WD_EPANET:
            return self.run_epanet(muid)
        else:
            raise ValueError(f"No simulation runner for model option: {model_option}")
    
    def run_cs(self, sim_muid: str | None = None) -> list[Path]:
        """Runs a Collection System (CS) simulation.

        Covers rivers, collection systems, and overland flows.

        Parameters
        ----------
        sim_muid : str, optional
            Simulation MUID. Defaults to the active simulation.

        Returns
        -------
        list[Path]
            Paths to the result files.
        """
        sim_muid = self._get_sim_muid(sim_muid)
        
        # CS is a special case that returns launcher directly
        launcher = DhiEngineSimpleLauncher()
        messages = List[String]()
        success, launcher, messages = self._engine_tool.RunEngine_CS(launcher, messages, sim_muid)
        
        self._handle_engine_launch(success, launcher, messages)
        self._wait_for_engine_completion(launcher)
        
        return self._get_result_files("msm_Project", sim_muid)
    
    def run_epanet(self, sim_muid: str | None = None) -> list[Path]:
        """Runs an EPANET water distribution simulation.

        Parameters
        ----------
        sim_muid : str, optional
            Simulation MUID. Defaults to the active simulation.

        Returns
        -------
        list[Path]
            Paths to the result files.
        """
        sim_muid = self._get_sim_muid(sim_muid)
        
        launcher = DhiEngineSimpleLauncher()
        messages = List[String]()
        success, messages = self._engine_tool.RunEngine_AllEpanet(
            MUSimulationOption.WD_EPANET,
            CancellationTokenSource().Token,
            messages,
            launcher=launcher,
            simMuid=sim_muid,
        )
        
        self._handle_engine_launch(success, launcher, messages)
        self._wait_for_engine_completion(launcher)
        
        return self._get_result_files("mw_Project", sim_muid)
    
    def run_swmm(self, sim_muid: Optional[str] = None) -> List[Path]:
        """Runs an SWMM urban drainage simulation.

        Parameters
        ----------
        sim_muid : str, optional
            Simulation MUID. Defaults to the active simulation.

        Returns
        -------
        list[Path]
            Paths to the result files.
        """
        sim_muid = self._get_sim_muid(sim_muid)
        
        launcher = DhiEngineSimpleLauncher()
        messages = List[String]()
        success, messages = self._engine_tool.RunEngine_AllSWMM(
            CancellationTokenSource().Token,
            messages,
            launcher=launcher,
            simMuid=sim_muid,
        )

        self._handle_engine_launch(success, launcher, messages)
        self._wait_for_engine_completion(launcher)
        
        return self._get_result_files("mss_Project", sim_muid)
        
    def _get_sim_muid(self, sim_muid: str | None) -> str:
        """Gets simulation MUID, or active simulation MUID if None."""
        if sim_muid is None:
            return self._database.active_simulation
        return sim_muid
    
    def _handle_engine_launch(self, success: bool, launcher: DhiEngineSimpleLauncher, 
                             messages: List[String]) -> None:
        """Handles engine launch: starts launcher or raises error."""
        if not success or launcher is None:
            messages_str = ". ".join(messages) if messages else "Unknown error"
            raise RuntimeError(f"Simulation failed to start: {messages_str}")
        
        launcher.Start()
    
    def _wait_for_engine_completion(self, launcher: DhiEngineSimpleLauncher) -> None:
        """Waits for the DHI engine simulation to complete."""
        start_time = time.time()
        timeout_start = 30.0
        time.sleep(0.5)
        while not launcher.IsEngineRunning:
            if time.time() - start_time > timeout_start:
                break
            time.sleep(0.1)

        while launcher.IsEngineRunning:
            time.sleep(0.1)
    
    def _get_result_files(self, project_table_name: str, sim_muid: str) -> List[Path]:
        """Gets result file paths for the completed simulation."""
        project_table = getattr(self._database.tables, project_table_name)._net_table
        result_files = list(project_table.GetResultFilePath(muid=sim_muid).Values)
        return [Path(f) for f in result_files]
