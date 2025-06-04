from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class msm_STRemovalWeirTableColumns(BaseColumns):
    """Column names for msm_STRemovalWeir (Sediment removal in weirs)."""
    MUID = "MUID"
    """ID"""
    MethodTypeNo = "MethodTypeNo"
    """Efficiency type"""
    WeirID = "WeirID"
    """Weir ID"""
    EfficiencyFunctionID = "EfficiencyFunctionID"
    """Efficiency function"""
    EfficiencyFac = "EfficiencyFac"
    """Efficiency factor [()]"""

class msm_STRemovalWeirTable(BaseTable):
    """Table for msm_STRemovalWeir (Sediment removal in weirs)."""
    
    @property
    def columns(self) -> msm_STRemovalWeirTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = msm_STRemovalWeirTableColumns(self)
        return self._columns