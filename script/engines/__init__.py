import clr
from .engine1d import Egnine1D
from .epanet import EPANET
from .swmm import SWMM

clr.AddReference("System")
clr.AddReference("System.Runtime")
clr.AddReference("System.Threading")
clr.AddReference("System.Runtime.InteropServices")
clr.AddReference("DHI.Amelia.DataModule")
clr.AddReference("DHI.Amelia.DataModule.Interface")
clr.AddReference("DHI.Amelia.Infrastructure.Interface")
clr.AddReference("DHI.Amelia.GlobalUtility")
clr.AddReference("DHI.Amelia.DomainServices")
clr.AddReference("DHI.Amelia.DomainServices.Interface")
