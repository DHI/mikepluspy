from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class mw_PPatternDTableColumns(BaseColumns):
    """Column names for mw_PPatternD (Pattern data)."""
    MUID = "MUID"
    PatternID = "PatternID"
    Sqn = "Sqn"
    AbsDateTime = "AbsDateTime"
    RelativeTime = "RelativeTime"
    Multiplier = "Multiplier"

class mw_PPatternDTable(BaseTable):
    """Table for mw_PPatternD (Pattern data)."""
    
    @property
    def columns(self) -> mw_PPatternDTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mw_PPatternDTableColumns(self)
        return self._columns