from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class msm_RRAddPercentTableColumns(BaseColumns):
    """Column names for msm_RRAddPercent (Intervals)."""
    MUID = "MUID"
    Sqn = "Sqn"
    ResultSpecID = "ResultSpecID"
    Percentage = "Percentage"

class msm_RRAddPercentTable(BaseTable):
    """Table for msm_RRAddPercent (Intervals)."""
    
    @property
    def columns(self) -> msm_RRAddPercentTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = msm_RRAddPercentTableColumns(self)
        return self._columns