from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class ms_DPPatternDTableColumns(BaseColumns):
    """Column names for ms_DPPatternD (Pattern data)."""
    MUID = "MUID"
    """MUID"""
    PatternID = "PatternID"
    """PatternID"""
    Sqn = "Sqn"
    """Sqn"""
    Time = "Time"
    """From"""
    ToTime = "ToTime"
    """To"""
    DPValue = "DPValue"
    """Multiplier"""

class ms_DPPatternDTable(BaseTable):
    """Table for ms_DPPatternD (Pattern data)."""
    
    @property
    def columns(self) -> ms_DPPatternDTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = ms_DPPatternDTableColumns(self)
        return self._columns