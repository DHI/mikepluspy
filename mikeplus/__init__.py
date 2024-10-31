import clr

__version__ = "2025.0.0"

clr.AddReference("DHI.Mike.Install, Version=1.0.0.0, Culture=neutral, PublicKeyToken=c513450b5d0bf0bf")
from DHI.Mike.Install import MikeImport, MikeProducts
MikeImport.Setup(23, MikeProducts.MikePlus)

clr.AddReference("System")
clr.AddReference("System.Runtime")
clr.AddReference("System.Runtime.InteropServices")
clr.AddReference("System.Data")
clr.AddReference("DHI.Amelia.DataModule")
clr.AddReference("DHI.Amelia.DataModule.Interface")
clr.AddReference("DHI.Amelia.Infrastructure.Interface")
clr.AddReference("DHI.Amelia.GlobalUtility")

from .datatableaccess import DataTableAccess
import sys
import warnings

mike1dio = sys.modules.get("mikeio1d")
if mike1dio is not None:
    raise RuntimeError('mikeio1d module has been loaded. mikeio1d only can be loaded after mikeplus module.')

mikeio = sys.modules.get("mikeio")
if mikeio is not None:
    raise RuntimeError('mikeplus cannot currently be used with mikeio in the same script.')