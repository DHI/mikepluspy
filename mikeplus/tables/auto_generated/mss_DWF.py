from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class mss_DWFTableColumns(BaseColumns):
    """Column names for mss_DWF (Dry weather flow)."""
    MUID = "MUID"
    """ID"""
    NodeID = "NodeID"
    """Load to"""
    Description = "Description"
    """Description"""
    PollutNo = "PollutNo"
    """Pollutant attached"""
    FlowValue = "FlowValue"
    """Average flow [m^3/s]"""
    PatternMonthID = "PatternMonthID"
    """Monthly"""
    PatternWeekID = "PatternWeekID"
    """Daily"""
    PatternWeekHourlyID = "PatternWeekHourlyID"
    """Week hourly"""
    PatternWeekendHourlyID = "PatternWeekendHourlyID"
    """Weekend hourly"""

class mss_DWFTable(BaseTable):
    """Table for mss_DWF (Dry weather flow)."""
    
    @property
    def columns(self) -> mss_DWFTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mss_DWFTableColumns(self)
        return self._columns