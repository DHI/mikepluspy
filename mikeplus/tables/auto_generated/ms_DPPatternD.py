from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class ms_DPPatternDTableColumns(BaseColumns):
    """Column names for ms_DPPatternD (Pattern data)."""
    MUID = "MUID"
    PatternID = "PatternID"
    Sqn = "Sqn"
    Time = "Time"
    ToTime = "ToTime"
    DPValue = "DPValue"

class ms_DPPatternDTable(BaseTable):
    """Table for ms_DPPatternD (Pattern data)."""
    
    @property
    def columns(self) -> ms_DPPatternDTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = ms_DPPatternDTableColumns(self)
        return self._columns