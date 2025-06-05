from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class mss_DWFDTableColumns(BaseColumns):
    """Column names for mss_DWFD (Pollutant data)."""
    MUID = "MUID"
    """ID"""
    DwfID = "DwfID"
    """Dwf ID"""
    PollutantID = "PollutantID"
    """Pollutant ID"""
    BValue = "BValue"
    """Base value"""
    UseMonthlyPtn = "UseMonthlyPtn"
    """Use monthly pattern"""
    PatternMonthID = "PatternMonthID"
    """Monthly pattern"""
    UseDailyPtn = "UseDailyPtn"
    """Use daily pattern"""
    PatternWeekID = "PatternWeekID"
    """Daily pattern"""
    UseHourlyPtn = "UseHourlyPtn"
    """Use hourly pattern"""
    PatternWeekHourlyID = "PatternWeekHourlyID"
    """Hourly pattern"""
    UseWeekendPtn = "UseWeekendPtn"
    """Use weekend pattern"""
    PatternWeekendHourlyID = "PatternWeekendHourlyID"
    """Weekend pattern"""

class mss_DWFDTable(BaseTable):
    """Table for mss_DWFD (Pollutant data)."""
    
    @property
    def columns(self) -> mss_DWFDTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mss_DWFDTableColumns(self)
        return self._columns