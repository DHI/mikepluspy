"""Provides useful warnings about conflicts related to usage alongside mikeio and mikeio1d."""

import sys
import os

MIKEIO1D_IMPORTED_BEFORE_MIKEPLUS = "mikeio1d" in sys.modules
DISABLE_CONFLICT_CHECKS = (
    os.getenv("MIKEPLUSPY_DISABLE_CONFLICT_CHECKS", "false").lower() == "true"
)


def check_conflicts():
    """Check for conflicts with mikeio and mikeio1d.

    This function checks if mikeio1d was imported before mikeplus. If so, it raises an error
    that mikeio1d must be imported after mikeplus.

    It also checks if mikeio is imported. If so, it raises an error that mikeio cannot currently
    be used in same process as mikeplus.
    
    Raises
    ------
    ImportError
        If mikeio1d was imported before mikeplus or if mikeio is imported
    """

    if DISABLE_CONFLICT_CHECKS:
        return

    if MIKEIO1D_IMPORTED_BEFORE_MIKEPLUS:
        raise ImportError(
            "mikeio1d must be imported after mikeplus to avoid conflicts. See docs for more info."
        )

    if "mikeio" in sys.modules:
        raise ImportError(
            """mikeio cannot currently be used in same process as mikeplus. 
            Workarounds include splitting code into separate scripts or using 
            Python's multiprocessing library to import mikeio and mikeplus in 
            separate processes. See docs for more info."""
        )
