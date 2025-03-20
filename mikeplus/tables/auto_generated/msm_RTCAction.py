from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class msm_RTCActionTableColumns(BaseColumns):
    """Column names for msm_RTCAction (Actions)."""
    MUID = "MUID"
    StructureTypeNo = "StructureTypeNo"
    ControlTypeNo = "ControlTypeNo"
    ActionTypeNo = "ActionTypeNo"
    PIDInput = "PIDInput"
    PIDSetPoint = "PIDSetPoint"
    PID = "PID"
    Value = "Value"
    TSFileName = "TSFileName"
    TSItemID = "TSItemID"
    ScaleFactor = "ScaleFactor"
    TableInput = "TableInput"
    TableInputY = "TableInputY"
    TableID = "TableID"
    TableTypeNo = "TableTypeNo"
    YearlyVarNo = "YearlyVarNo"
    SetPointSourceTypeNo = "SetPointSourceTypeNo"
    SetPointFileName = "SetPointFileName"
    SetPointFileID = "SetPointFileID"
    SetPointTableID = "SetPointTableID"
    SetPointTableInput = "SetPointTableInput"

class msm_RTCActionTable(BaseTable):
    """Table for msm_RTCAction (Actions)."""
    
    @property
    def columns(self) -> msm_RTCActionTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = msm_RTCActionTableColumns(self)
        return self._columns