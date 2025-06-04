from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class msm_RTCActionTableColumns(BaseColumns):
    """Column names for msm_RTCAction (Actions)."""
    MUID = "MUID"
    """ID"""
    StructureTypeNo = "StructureTypeNo"
    """Structure type"""
    ControlTypeNo = "ControlTypeNo"
    """Control type"""
    ActionTypeNo = "ActionTypeNo"
    """Action"""
    PIDInput = "PIDInput"
    """PID input"""
    PIDSetPoint = "PIDSetPoint"
    """PID set point"""
    PID = "PID"
    """PID parameters"""
    Value = "Value"
    """Value"""
    TSFileName = "TSFileName"
    """File name"""
    TSItemID = "TSItemID"
    """Item ID"""
    ScaleFactor = "ScaleFactor"
    """Scale factor"""
    TableInput = "TableInput"
    """Table's input"""
    TableInputY = "TableInputY"
    """Table's Y input"""
    TableID = "TableID"
    """Table ID"""
    TableTypeNo = "TableTypeNo"
    """TableTypeNo"""
    YearlyVarNo = "YearlyVarNo"
    """Values specified as yearly variation"""
    SetPointSourceTypeNo = "SetPointSourceTypeNo"
    """PID set point source"""
    SetPointFileName = "SetPointFileName"
    """PID set point"""
    SetPointFileID = "SetPointFileID"
    """Item ID"""
    SetPointTableID = "SetPointTableID"
    """PID set point"""
    SetPointTableInput = "SetPointTableInput"
    """Table's input"""

class msm_RTCActionTable(BaseTable):
    """Table for msm_RTCAction (Actions)."""
    
    @property
    def columns(self) -> msm_RTCActionTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = msm_RTCActionTableColumns(self)
        return self._columns