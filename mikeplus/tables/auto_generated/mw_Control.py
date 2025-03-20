from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class mw_ControlTableColumns(BaseColumns):
    """Column names for mw_Control (Simple controls)."""
    MUID = "MUID"
    Sqn = "Sqn"
    LinkID = "LinkID"
    LinkTypeNo = "LinkTypeNo"
    SettingNo = "SettingNo"
    SetValue = "SetValue"
    ConditionNo = "ConditionNo"
    ControlJunctionID = "ControlJunctionID"
    CLevel = "CLevel"
    TValue = "TValue"
    TimeUnitsNo = "TimeUnitsNo"
    ClockTimeHrs = "ClockTimeHrs"
    ClockTimeMin = "ClockTimeMin"
    ClockTimeUnitsNo = "ClockTimeUnitsNo"
    Desription = "Desription"

class mw_ControlTable(BaseTable):
    """Table for mw_Control (Simple controls)."""
    
    @property
    def columns(self) -> mw_ControlTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mw_ControlTableColumns(self)
        return self._columns