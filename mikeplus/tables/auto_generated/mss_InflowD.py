from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class mss_InflowDTableColumns(BaseColumns):
    """Column names for mss_InflowD (Pollutants inflows)."""
    MUID = "MUID"
    InflowID = "InflowID"
    PollutantID = "PollutantID"
    FormatNo = "FormatNo"
    UseTimeSeries = "UseTimeSeries"
    PollutSeriesID = "PollutSeriesID"
    ScalePollutValue = "ScalePollutValue"
    BasePollutValue = "BasePollutValue"
    UsePattern = "UsePattern"
    BasePatternID = "BasePatternID"
    ConvFactor = "ConvFactor"

class mss_InflowDTable(BaseTable):
    """Table for mss_InflowD (Pollutants inflows)."""
    
    @property
    def columns(self) -> mss_InflowDTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mss_InflowDTableColumns(self)
        return self._columns