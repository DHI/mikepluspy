from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class msm_HDAddPercentTableColumns(BaseColumns):
    """Column names for msm_HDAddPercent (Intervals)."""
    MUID = "MUID"
    """MUID"""
    Sqn = "Sqn"
    """Sqn"""
    ResultSpecID = "ResultSpecID"
    """ResultSpecID"""
    Percentage = "Percentage"
    """Percentage"""

class msm_HDAddPercentTable(BaseTable):
    """Table for msm_HDAddPercent (Intervals)."""
    
    @property
    def columns(self) -> msm_HDAddPercentTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = msm_HDAddPercentTableColumns(self)
        return self._columns