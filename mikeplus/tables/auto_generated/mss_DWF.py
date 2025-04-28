from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class mss_DWFTableColumns(BaseColumns):
    """Column names for mss_DWF (Dry weather flow)."""
    MUID = "MUID"
    NodeID = "NodeID"
    Description = "Description"
    PollutNo = "PollutNo"
    FlowValue = "FlowValue"
    PatternMonthID = "PatternMonthID"
    PatternWeekID = "PatternWeekID"
    PatternWeekHourlyID = "PatternWeekHourlyID"
    PatternWeekendHourlyID = "PatternWeekendHourlyID"

class mss_DWFTable(BaseTable):
    """Table for mss_DWF (Dry weather flow)."""
    
    @property
    def columns(self) -> mss_DWFTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mss_DWFTableColumns(self)
        return self._columns