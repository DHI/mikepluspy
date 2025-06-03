"""MIKE+Py package."""

__version__ = "2025.0.2"

from .conflicts import check_conflicts

check_conflicts()

import clr  # noqa: E402

clr.AddReference(
    "DHI.Mike.Install, Version=1.0.0.0, Culture=neutral, PublicKeyToken=c513450b5d0bf0bf"
)
from DHI.Mike.Install import MikeImport, MikeProducts  # noqa: E402

MikeImport.Setup(23, MikeProducts.MikePlus)

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

__all__ = ["Database", "DataTableAccess", "DataTableDemoAccess", "open", "create"]
