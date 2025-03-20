from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class mw_RTCTableColumns(BaseColumns):
    """Column names for mw_RTC (Real time control)."""
    MUID = "MUID"
    Enabled = "Enabled"
    ControlElementTypeNo = "ControlElementTypeNo"
    ControlElementID = "ControlElementID"
    ControlValueMin = "ControlValueMin"
    ControlValueMax = "ControlValueMax"
    ControlMaxIncRate = "ControlMaxIncRate"
    ControlMaxDecRate = "ControlMaxDecRate"
    ControlTypeNo = "ControlTypeNo"
    Kp = "Kp"
    Ki = "Ki"
    Kd = "Kd"
    SetPointElementTypeNo = "SetPointElementTypeNo"
    SetPointID = "SetPointID"
    SetPointVariableNo = "SetPointVariableNo"
    SetPointTypeNo = "SetPointTypeNo"
    SetPointValue = "SetPointValue"
    SetPointValueCurveID = "SetPointValueCurveID"
    SetPointAccuracy = "SetPointAccuracy"
    Description = "Description"

class mw_RTCTable(BaseTable):
    """Table for mw_RTC (Real time control)."""
    
    @property
    def columns(self) -> mw_RTCTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mw_RTCTableColumns(self)
        return self._columns