"""Provides useful warnings about conflicts related to usage alongside mikeio and mikeio1d."""

import sys
import os
import warnings

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

    MIKEIO_IMPORTED = "mikeio" in sys.modules

    if MIKEIO_IMPORTED:
        if not hasattr(check_conflicts, "warned"):
            check_conflicts.warned = True
            warnings.warn(
                "mikeio and mikeplus are both imported in the same process. There could be some conflicts. See docs for more info.",
                category=UserWarning,
                stacklevel=2,
            )
