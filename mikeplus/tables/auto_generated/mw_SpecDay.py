from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class mw_SpecDayTableColumns(BaseColumns):
    """Column names for mw_SpecDay (mw_SpecDay)."""
    MUID = "MUID"
    PatternID = "PatternID"
    Description = "Description"
    StartDate = "StartDate"
    EndDate = "EndDate"
    Factor = "Factor"

class mw_SpecDayTable(BaseTable):
    """Table for mw_SpecDay (mw_SpecDay)."""
    
    @property
    def columns(self) -> mw_SpecDayTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mw_SpecDayTableColumns(self)
        return self._columns