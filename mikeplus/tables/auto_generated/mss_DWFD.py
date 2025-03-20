from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class mss_DWFDTableColumns(BaseColumns):
    """Column names for mss_DWFD (Pollutant data)."""
    MUID = "MUID"
    DwfID = "DwfID"
    PollutantID = "PollutantID"
    BValue = "BValue"
    UseMonthlyPtn = "UseMonthlyPtn"
    PatternMonthID = "PatternMonthID"
    UseDailyPtn = "UseDailyPtn"
    PatternWeekID = "PatternWeekID"
    UseHourlyPtn = "UseHourlyPtn"
    PatternWeekHourlyID = "PatternWeekHourlyID"
    UseWeekendPtn = "UseWeekendPtn"
    PatternWeekendHourlyID = "PatternWeekendHourlyID"

class mss_DWFDTable(BaseTable):
    """Table for mss_DWFD (Pollutant data)."""
    
    @property
    def columns(self) -> mss_DWFDTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mss_DWFDTableColumns(self)
        return self._columns