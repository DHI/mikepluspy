import clr

clr.AddReference("System")
clr.AddReference("System.Runtime")
clr.AddReference("System.Threading")
clr.AddReference("System.Runtime.InteropServices")
clr.AddReference("DHI.Amelia.DataModule")
clr.AddReference("DHI.Amelia.DataModule.Interface")
clr.AddReference("DHI.Amelia.Infrastructure.Interface")
clr.AddReference("DHI.Amelia.GlobalUtility")
clr.AddReference("DHI.Amelia.Tools.EngineTool")

from .engine1d import Engine1D  # noqa: E402
from .epanet import EPANET  # noqa: E402
from .swmm import SWMM  # noqa: E402

__all__ = [
    "Engine1D",
    "EPANET",
    "SWMM",
]
