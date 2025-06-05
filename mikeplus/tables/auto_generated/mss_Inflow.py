from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class mss_InflowTableColumns(BaseColumns):
    """Column names for mss_Inflow (Inflows)."""
    MUID = "MUID"
    """ID"""
    NodeID = "NodeID"
    """Inflow to"""
    Description = "Description"
    """Description"""
    FlowSeriesID = "FlowSeriesID"
    """Time series ID"""
    ScaleFlowFactor = "ScaleFlowFactor"
    """Scale factor"""
    BaseFlowValue = "BaseFlowValue"
    """Base flow [m^3/s]"""
    BaselinePatternID = "BaselinePatternID"
    """Pattern ID"""
    PollutNo = "PollutNo"
    """Pollutants"""

class mss_InflowTable(BaseTable):
    """Table for mss_Inflow (Inflows)."""
    
    @property
    def columns(self) -> mss_InflowTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mss_InflowTableColumns(self)
        return self._columns