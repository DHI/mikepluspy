"""MIKE+Py package."""

__version__ = "2025.2.0"

import clr
from .conflicts import check_conflicts
from .utils import setup_bin_path

check_conflicts()
setup_bin_path(
    major_assembly_version=23,
    fallback_mikeplus_install_root="C:/Program Files (x86)/DHI/MIKE+/2025",
    env_var_name_install_root="MIKEPLUSPY_INSTALL_ROOT",  # set this environment variable to use custom install path
    bin_path="bin/x64",
)

#  keep here for backward compatibility (mikeio1d uses) ... remove in 2026.0.0
try:
    from DHI.Mike.Install import MikeImport  # noqa: E402, F401
    from DHI.Mike.Install import MikeProducts  # noqa: E402, F401
except ImportError:
    pass

clr.AddReference("System")
clr.AddReference("System.Runtime")
clr.AddReference("System.Runtime.InteropServices")
clr.AddReference("System.Data")
clr.AddReference("NetTopologySuite")
clr.AddReference("DHI.Amelia.DataModule")
clr.AddReference("DHI.Amelia.DataModule.Interface")
clr.AddReference("DHI.Amelia.Infrastructure.Interface")
clr.AddReference("DHI.Amelia.GlobalUtility")
clr.AddReference("DHI.Amelia.Tools.EngineTool")

from .datatableaccess import DataTableAccess  # noqa: E402
from .datatableaccess import DataTableDemoAccess  # noqa: E402
from .database import Database  # noqa: E402
from .shortcuts import open, create  # noqa: E402
from .utils import to_sql  # noqa: E402

__all__ = [
    "Database",
    "DataTableAccess",
    "DataTableDemoAccess",
    "open",
    "create",
    "to_sql",
]
