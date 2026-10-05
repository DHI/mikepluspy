"""Package containing access to various MIKE+ tools."""

import clr

clr.AddReference("System")
clr.AddReference("System.Runtime")
clr.AddReference("System.Threading")
clr.AddReference("System.Runtime.InteropServices")
clr.AddReference("DHI.Generic.MikeZero.EUM")
clr.AddReference("DHI.Amelia.DataModule")
clr.AddReference("DHI.Amelia.DataModule.Interface")
clr.AddReference("DHI.Amelia.Infrastructure.Interface")
clr.AddReference("DHI.Amelia.GlobalUtility")
clr.AddReference("DHI.Amelia.DomainServices")
clr.AddReference("DHI.Amelia.DomainServices.Interface")
clr.AddReference("DHI.Amelia.Tools.ImportEngine")
clr.AddReference("DHI.Amelia.Tools.TopologyRepairTool")
clr.AddReference("DHI.Amelia.Tools.InterpolationEngine")
clr.AddReference("DHI.Amelia.Tools.ConnectionRepairEngine")
clr.AddReference("DHI.Amelia.Tools.CatchmentProcessing")
clr.AddReference("DHI.Amelia.Tools.GeoCodeTool")

from .catch_slope_length_process_tool import CathSlopeLengthProcess
from .connection_repair_tool import ConnectionRepairTool
from .demand_aggregation_tool import DemandAggregationTool
from .demand_connection_tool import DemandConnectionTool
from .import_tool import ImportTool
from .interpolation_tool import InterpolationTool
from .topology_repair_tool import TopoRepairTool

__all__ = [
    "CathSlopeLengthProcess",
    "ConnectionRepairTool",
    "DemandAggregationTool",
    "DemandConnectionTool",
    "ImportTool",
    "InterpolationTool",
    "TopoRepairTool",
]
