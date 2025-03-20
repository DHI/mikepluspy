from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class mss_InflowTableColumns(BaseColumns):
    """Column names for mss_Inflow (Inflows)."""
    MUID = "MUID"
    NodeID = "NodeID"
    Description = "Description"
    FlowSeriesID = "FlowSeriesID"
    ScaleFlowFactor = "ScaleFlowFactor"
    BaseFlowValue = "BaseFlowValue"
    BaselinePatternID = "BaselinePatternID"
    PollutNo = "PollutNo"

class mss_InflowTable(BaseTable):
    """Table for mss_Inflow (Inflows)."""
    
    @property
    def columns(self) -> mss_InflowTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mss_InflowTableColumns(self)
        return self._columns