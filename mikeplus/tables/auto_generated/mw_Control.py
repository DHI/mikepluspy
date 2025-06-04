from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class mw_ControlTableColumns(BaseColumns):
    """Column names for mw_Control (Simple controls)."""
    MUID = "MUID"
    """Control ID"""
    Sqn = "Sqn"
    """Sqn"""
    LinkID = "LinkID"
    """Link ID"""
    LinkTypeNo = "LinkTypeNo"
    """Link type"""
    SettingNo = "SettingNo"
    """Setting"""
    SetValue = "SetValue"
    """Setting value"""
    ConditionNo = "ConditionNo"
    """Condition"""
    ControlJunctionID = "ControlJunctionID"
    """Control node"""
    CLevel = "CLevel"
    """Control level [m]"""
    TValue = "TValue"
    """Time"""
    TimeUnitsNo = "TimeUnitsNo"
    """Time unit"""
    ClockTimeHrs = "ClockTimeHrs"
    """Clock time hours"""
    ClockTimeMin = "ClockTimeMin"
    """Clock time minutes"""
    ClockTimeUnitsNo = "ClockTimeUnitsNo"
    """Clock time unit"""
    Desription = "Desription"
    """Description"""

class mw_ControlTable(BaseTable):
    """Table for mw_Control (Simple controls)."""
    
    @property
    def columns(self) -> mw_ControlTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mw_ControlTableColumns(self)
        return self._columns