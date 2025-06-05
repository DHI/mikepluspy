from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class msm_STInitDepthFractLocalTableColumns(BaseColumns):
    """Column names for msm_STInitDepthFractLocal (msm_STInitDepthFractLocal)."""
    MUID = "MUID"
    """MUID"""
    STInitDepthID = "STInitDepthID"
    """ST initial depths ID"""
    FractionID = "FractionID"
    """Fraction"""
    FracPercentActive = "FracPercentActive"
    """Percentage active layer [%]"""
    FracPercentPassive = "FracPercentPassive"
    """Percentage passive layer [%]"""

class msm_STInitDepthFractLocalTable(BaseTable):
    """Table for msm_STInitDepthFractLocal (msm_STInitDepthFractLocal)."""
    
    @property
    def columns(self) -> msm_STInitDepthFractLocalTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = msm_STInitDepthFractLocalTableColumns(self)
        return self._columns