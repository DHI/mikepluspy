from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class mw_FlushingTableColumns(BaseColumns):
    """Column names for mw_Flushing (Flushing analysis)."""
    MUID = "MUID"
    TypeNo = "TypeNo"
    Sqn = "Sqn"
    OutputPath = "OutputPath"
    PipeList = "PipeList"
    TargetTypeNo = "TargetTypeNo"
    TargetVelocity = "TargetVelocity"
    TargetShearStr = "TargetShearStr"
    MinResidualPre = "MinResidualPre"
    EmitterCoeff = "EmitterCoeff"
    FlushingDemand = "FlushingDemand"
    StartHour = "StartHour"
    IdleInterval = "IdleInterval"
    SaftyFactor = "SaftyFactor"
    MaxFlushTimeSpan = "MaxFlushTimeSpan"
    StartNodeNo = "StartNodeNo"
    StartNodeID = "StartNodeID"
    StartNodeList = "StartNodeList"
    HydrantLayer = "HydrantLayer"
    ValveLayer = "ValveLayer"
    IdentifyClosedPipeNo = "IdentifyClosedPipeNo"
    UseToleranceNo = "UseToleranceNo"
    Tolerance = "Tolerance"
    ClosedPipes = "ClosedPipes"
    Description = "Description"

class mw_FlushingTable(BaseTable):
    """Table for mw_Flushing (Flushing analysis)."""
    
    @property
    def columns(self) -> mw_FlushingTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mw_FlushingTableColumns(self)
        return self._columns