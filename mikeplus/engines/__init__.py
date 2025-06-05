"""
MIKE+ Engine classes.

.. deprecated:: 2025.1.0
   The 'mikeplus.engines' package is deprecated to simplify the codebase and provide a more simulation-oriented API.
   Please use 'mikeplus.simulation_runner.SimulationRunner' or 'Database.run()' for simulations.
   This package will be removed in version 2026.0.0.
"""

from .engine1d import Engine1D  # noqa: E402
from .epanet import EPANET  # noqa: E402
from .swmm import SWMM  # noqa: E402
from .flood_engine import FloodEngine  # noqa: E402

__all__ = [
    "Engine1D",
    "EPANET",
    "SWMM",
    "FloodEngine",
]
