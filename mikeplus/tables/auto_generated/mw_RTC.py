from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class mw_RTCTableColumns(BaseColumns):
    """Column names for mw_RTC (Real time control)."""
    MUID = "MUID"
    """ID"""
    Enabled = "Enabled"
    """Is active"""
    ControlElementTypeNo = "ControlElementTypeNo"
    """Control element type"""
    ControlElementID = "ControlElementID"
    """Control element ID"""
    ControlValueMin = "ControlValueMin"
    """Minimum value"""
    ControlValueMax = "ControlValueMax"
    """Maximum value"""
    ControlMaxIncRate = "ControlMaxIncRate"
    """Maximum increase rate"""
    ControlMaxDecRate = "ControlMaxDecRate"
    """Maximum decrease rate"""
    ControlTypeNo = "ControlTypeNo"
    """Control type"""
    Kp = "Kp"
    """Kp"""
    Ki = "Ki"
    """Ki"""
    Kd = "Kd"
    """Kd"""
    SetPointElementTypeNo = "SetPointElementTypeNo"
    """Set-point element type"""
    SetPointID = "SetPointID"
    """Set-point element ID"""
    SetPointVariableNo = "SetPointVariableNo"
    """Set-point variable"""
    SetPointTypeNo = "SetPointTypeNo"
    """Set-point type"""
    SetPointValue = "SetPointValue"
    """Set-point value"""
    SetPointValueCurveID = "SetPointValueCurveID"
    """Set-point curve"""
    SetPointAccuracy = "SetPointAccuracy"
    """Set-point accuracy [%]"""
    Description = "Description"
    """Description"""

class mw_RTCTable(BaseTable):
    """Table for mw_RTC (Real time control)."""
    
    @property
    def columns(self) -> mw_RTCTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mw_RTCTableColumns(self)
        return self._columns