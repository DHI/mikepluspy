from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class msm_STRemovalWeirTableColumns(BaseColumns):
    """Column names for msm_STRemovalWeir (Sediment removal in weirs)."""
    MUID = "MUID"
    MethodTypeNo = "MethodTypeNo"
    WeirID = "WeirID"
    EfficiencyFunctionID = "EfficiencyFunctionID"
    EfficiencyFac = "EfficiencyFac"

class msm_STRemovalWeirTable(BaseTable):
    """Table for msm_STRemovalWeir (Sediment removal in weirs)."""
    
    @property
    def columns(self) -> msm_STRemovalWeirTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = msm_STRemovalWeirTableColumns(self)
        return self._columns