from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class ms_DPProfileDTableColumns(BaseColumns):
    """Column names for ms_DPProfileD (profile data)."""
    MUID = "MUID"
    """MUID"""
    ProfileID = "ProfileID"
    """ProfileID"""
    Sqn = "Sqn"
    """Sqn"""
    PatternID = "PatternID"
    """Diurnal pattern"""
    ScheduleID = "ScheduleID"
    """Calendar"""

class ms_DPProfileDTable(BaseTable):
    """Table for ms_DPProfileD (profile data)."""
    
    @property
    def columns(self) -> ms_DPProfileDTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = ms_DPProfileDTableColumns(self)
        return self._columns