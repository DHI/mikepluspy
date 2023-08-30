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
clr.AddReference("System.Threading")
clr.AddReference("System.Runtime.InteropServices")
clr.AddReference("DHI.Generic.MikeZero.EUM")
clr.AddReference("DHI.Amelia.DataModule")
clr.AddReference("DHI.Amelia.DataModule.Interface")
clr.AddReference("DHI.Amelia.Infrastructure.Interface")
clr.AddReference("DHI.Amelia.GlobalUtility")
clr.AddReference("DHI.Amelia.DomainServices.Interface")
clr.AddReference("DHI.Amelia.Tools.ImportEngine")
clr.AddReference("DHI.Amelia.Tools.TopologyRepairTool")
clr.AddReference("DHI.Amelia.Tools.InterpolationEngine")
clr.AddReference("DHI.Amelia.Tools.ConnectionRepairEngine")
clr.AddReference("DHI.Amelia.Tools.CatchmentProcessing")

from .import_tool import ImportTool
from .topology_repair_tool import TopoRepairTool
from .interpolation_tool import InterpolationTool
from .connection_repair_tool import ConnectionRepairTool
from .catch_slope_length_process_tool import CathSlopeLengthProcess