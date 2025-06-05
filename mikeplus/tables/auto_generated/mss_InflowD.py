from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class mss_InflowDTableColumns(BaseColumns):
    """Column names for mss_InflowD (Pollutants inflows)."""
    MUID = "MUID"
    """MUID"""
    InflowID = "InflowID"
    """InflowID"""
    PollutantID = "PollutantID"
    """Pollutant ID"""
    FormatNo = "FormatNo"
    """Format"""
    UseTimeSeries = "UseTimeSeries"
    """Use time series"""
    PollutSeriesID = "PollutSeriesID"
    """Time series ID"""
    ScalePollutValue = "ScalePollutValue"
    """Scale factor [()]"""
    BasePollutValue = "BasePollutValue"
    """Base value"""
    UsePattern = "UsePattern"
    """Use pattern"""
    BasePatternID = "BasePatternID"
    """Base pattern"""
    ConvFactor = "ConvFactor"
    """Unit factor [()]"""

class mss_InflowDTable(BaseTable):
    """Table for mss_InflowD (Pollutants inflows)."""
    
    @property
    def columns(self) -> mss_InflowDTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mss_InflowDTableColumns(self)
        return self._columns