from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class msm_LTSRunSTableColumns(BaseColumns):
    """Column names for msm_LTSRunS (Run time stop criteria)."""
    MUID = "MUID"
    """ID"""
    ApplyNo = "ApplyNo"
    """Apply"""
    ConditionNo = "ConditionNo"
    """Type"""
    LocationNo = "LocationNo"
    """Location type"""
    LocationID = "LocationID"
    """Location"""
    StopValue = "StopValue"
    """Threshold"""
    StopTime = "StopTime"
    """Duration [min]"""

class msm_LTSRunSTable(BaseTable):
    """Table for msm_LTSRunS (Run time stop criteria)."""
    
    @property
    def columns(self) -> msm_LTSRunSTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = msm_LTSRunSTableColumns(self)
        return self._columns