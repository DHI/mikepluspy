import clr
import sys
import os
from platform import architecture

__version__ = "0.3.0"

clr.AddReference("DHI.Mike.Install, Version=1.0.0.0, Culture=neutral, PublicKeyToken=c513450b5d0bf0bf")
from DHI.Mike.Install import MikeImport, MikeProducts
MikeImport.Setup(22, MikeProducts.MikePlus)
'''MikeImport.SetupInstallDir("D:\\Work\\10081016 - MIKE+ WD features 2024\\Products\\Source\\Amelia\\Core\\Source", True)'''

clr.AddReference("System")
clr.AddReference("System.Runtime")
clr.AddReference("System.Runtime.InteropServices")
clr.AddReference("System.Data")
clr.AddReference("DHI.Amelia.DataModule")
clr.AddReference("DHI.Amelia.DataModule.Interface")
clr.AddReference("DHI.Amelia.Infrastructure.Interface")
clr.AddReference("DHI.Amelia.GlobalUtility")

from .datatbleaccess import DataTableAccess