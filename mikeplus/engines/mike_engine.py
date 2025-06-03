"""MikeEngine class for unified engine operations across all MIKE+ simulation types."""

from __future__ import annotations

from typing import List, Optional
from pathlib import Path

from DHI.Amelia.Tools.EngineTool import EngineTool

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
        if not isinstance(database, Database):
            raise TypeError("MikeEngine only accepts Database objects. For backward compatibility "
                           "with DataTableContainer, use the original engine classes.")
            
        self._database = database
        if not database.is_open:
            database.open()
        self._data_tables = database._data_table_container
        self._engine_tool = EngineTool()
        self._engine_tool.DataTables = self._data_tables
    

    
    def run_1d(self, sim_muid: Optional[str] = None) -> List[Path]:
        """Run MIKE 1D simulation.

        Parameters
        ----------
        sim_muid : str, optional
            Simulation MUID. If None, uses the active simulation MUID.

        Returns
        -------
        List[Path]
            List of result file paths as Path objects.
        """
        # Stub implementation
        return []
    

    
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
