import sys
import clr

__version__ = "2024.1.0"

clr.AddReference(
    "DHI.Mike.Install, Version=1.0.0.0, Culture=neutral, PublicKeyToken=c513450b5d0bf0bf"
)
from DHI.Mike.Install import MikeImport, MikeProducts  # noqa: E402

MikeImport.Setup(22, MikeProducts.MikePlus)

clr.AddReference("System")
clr.AddReference("System.Runtime")
clr.AddReference("System.Runtime.InteropServices")
clr.AddReference("System.Data")
clr.AddReference("DHI.Amelia.DataModule")
clr.AddReference("DHI.Amelia.DataModule.Interface")
clr.AddReference("DHI.Amelia.Infrastructure.Interface")
clr.AddReference("DHI.Amelia.GlobalUtility")
clr.AddReference("NetTopologySuite")

from .datatableaccess import DataTableAccess  # noqa: E402


mike1dio = sys.modules.get("mikeio1d")
if mike1dio is not None:
    raise RuntimeError(
        "mikeio1d module has been loaded. mikeio1d only can be loaded after mikeplus module."
    )

__all__ = ["DataTableAccess"]
