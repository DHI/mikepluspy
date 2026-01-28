"""SimulationRunner for executing MIKE+ simulations."""

from __future__ import annotations

import time
from pathlib import Path
from typing import TYPE_CHECKING
from typing import Literal

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
        """Initialize SimulationRunner with a MIKE+ database.

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

    def run(
        self,
        muid: str | None = None,
        *,
        sim_option: Literal[
            "CS_MIKE_1D",
            "CS_SWMM",
            "WD_EPANET",
            "CS_MIKE_1D_JobList",
        ]
        | None = None,
    ) -> list[Path]:
        """Run a simulation.

        Parameters
        ----------
        muid : str, optional
            Simulation MUID. Defaults to the active simulation.
        sim_option : Literal[str], optional
            Simulation option. Defaults to None. Possible values are:

            - "CS_MIKE_1D": Rivers, collection systems, and overland flows.
            - "CS_SWMM": SWMM-based collection systems and overland flows.
            - "WD_EPANET": Water distribution systems.
            - "CS_MIKE_1D_JobList": Generate job list for LTS simulation (.MJL file).

        Returns
        -------
        list[Path]
            Paths to the result files.
        """
        VALID_OPTIONS = (
            "CS_MIKE_1D",
            "CS_SWMM",
            "WD_EPANET",
            "CS_MIKE_1D_JobList",
        )
        if sim_option is not None and sim_option not in VALID_OPTIONS:
            raise ValueError(
                f"Invalid simulation option: {sim_option}. Valid options: {', '.join(VALID_OPTIONS)}"
            )

        if sim_option is None:
            model_option = self._database.active_model
            model_option = Enum.Parse(MUModelOption, model_option)
            if model_option == MUModelOption.CS_MIKE1D:
                sim_option = MUSimulationOption.CS_MIKE_1D
            elif model_option == MUModelOption.CS_SWMM:
                sim_option = MUSimulationOption.CS_SWMM
            elif model_option == MUModelOption.WD_EPANET:
                sim_option = MUSimulationOption.WD_EPANET
            else:
                raise ValueError(
                    f"Could not use 'active_model' of {model_option} to determine "
                    f"simulation option. Manually specify the simulation option."
                )

        if isinstance(sim_option, str):
            sim_option = Enum.Parse(MUSimulationOption, sim_option)

        if sim_option == MUSimulationOption.CS_MIKE_1D:
            return self.run_cs(muid)
        elif sim_option == MUSimulationOption.CS_SWMM:
            return self.run_swmm(muid)
        elif sim_option == MUSimulationOption.WD_EPANET:
            return self.run_epanet(muid)
        elif sim_option == MUSimulationOption.CS_MIKE_1D_JobList:
            return self.run_lts_joblist(muid)
        else:
            raise ValueError(
                f"No simulation runner for simulation option: {sim_option}"
            )

    def run_cs(self, sim_muid: str | None = None) -> list[Path]:
        """Run a Collection System (CS) simulation.

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
        success, launcher, messages = self._engine_tool.RunEngine_CS(
            launcher, messages, sim_muid
        )

        self._handle_engine_launch(success, launcher, messages)
        self._wait_for_engine_completion(launcher)

        return self._get_result_files("msm_Project", sim_muid)

    def run_lts_joblist(self, sim_muid: str | None = None) -> list[Path]:
        """Run a Long Term Simulation (LTS) job list generation.

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
        success, launcher, messages = self._engine_tool.RunEngine_LTS_JobList(
            launcher, messages, sim_muid
        )

        self._handle_engine_launch(success, launcher, messages)
        self._wait_for_engine_completion(launcher)

        return self._get_result_files("msm_Project", sim_muid, is_lts_joblist=True)

    def run_epanet(self, sim_muid: str | None = None) -> list[Path]:
        """Run an EPANET water distribution simulation.

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

    def run_swmm(self, sim_muid: str | None = None) -> List[Path]:
        """Run an SWMM urban drainage simulation.

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
        """Get simulation MUID, or active simulation MUID if None."""
        if sim_muid is None:
            return self._database.active_simulation
        return sim_muid

    def _handle_engine_launch(
        self, success: bool, launcher: DhiEngineSimpleLauncher, messages: List[String]
    ) -> None:
        """Handle engine launch: starts launcher or raises error."""
        if not success or launcher is None:
            messages_str = ". ".join(messages) if messages else "Unknown error"
            raise RuntimeError(f"Simulation failed to start: {messages_str}")

        launcher.Start()

    def _wait_for_engine_completion(self, launcher: DhiEngineSimpleLauncher) -> None:
        """Wait for the DHI engine simulation to complete."""
        start_time = time.time()
        timeout_start = 30.0
        time.sleep(0.5)
        while not launcher.IsEngineRunning:
            if time.time() - start_time > timeout_start:
                break
            time.sleep(0.1)

        while launcher.IsEngineRunning:
            time.sleep(0.1)

    def _get_result_files(
        self, project_table_name: str, sim_muid: str, is_lts_joblist: bool = False
    ) -> List[Path]:
        """Get result file paths for the completed simulation."""
        if is_lts_joblist:
            return self._get_result_file_lts_job_list(sim_muid)

        project_table = getattr(self._database.tables, project_table_name)
        result_files = list(
            project_table._net_table.GetResultFilePath(muid=sim_muid).Values
        )
        return [Path(f) for f in result_files]

    def _get_result_file_lts_job_list(self, sim_muid: str) -> list[Path]:
        project_table = self._database.tables.msm_Project
        scenario = (
            project_table.select([project_table.columns.ScenarioName])
            .by_muid(sim_muid)
            .execute()
        )
        try:
            scenario = scenario[sim_muid][0]
        except Exception as e:
            raise ValueError(f"Scenario not found for simulation MUID: {sim_muid}. {e}")

        result_file_name = f"{sim_muid}{scenario}.MJL"
        return [Path(self._database.db_path.parent / result_file_name)]
