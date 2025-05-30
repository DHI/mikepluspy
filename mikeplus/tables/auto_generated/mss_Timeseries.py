from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class mss_TimeseriesTableColumns(BaseColumns):
    """Column names for mss_Timeseries (Time series)."""
    MUID = "MUID"
    TypeNo = "TypeNo"
    TimeseriesTypeNo = "TimeseriesTypeNo"
    UseRelativeTime = "UseRelativeTime"
    DeltaT = "DeltaT"
    ExternalTimeseriesFile = "ExternalTimeseriesFile"
    Description = "Description"

class mss_TimeseriesTable(BaseTable):
    """Table for mss_Timeseries (Time series)."""
    
    @property
    def columns(self) -> mss_TimeseriesTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mss_TimeseriesTableColumns(self)
        return self._columns