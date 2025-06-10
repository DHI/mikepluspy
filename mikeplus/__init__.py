"""MIKE+Py package."""

__version__ = "2025.1.1"

import clr
from .conflicts import check_conflicts
from .utils import setup_bin_path

check_conflicts()
setup_bin_path()

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
