from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class mss_TimeseriesDTableColumns(BaseColumns):
    """Column names for mss_TimeseriesD (Time Series data values)."""
    MUID = "MUID"
    TimeseriesID = "TimeseriesID"
    Sqn = "Sqn"
    TSDate = "TSDate"
    TSRelTime = "TSRelTime"
    TSValue = "TSValue"

class mss_TimeseriesDTable(BaseTable):
    """Table for mss_TimeseriesD (Time Series data values)."""
    
    @property
    def columns(self) -> mss_TimeseriesDTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mss_TimeseriesDTableColumns(self)
        return self._columns