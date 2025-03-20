from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class msm_HDInitialConditionTableColumns(BaseColumns):
    """Column names for msm_HDInitialCondition (Initial conditions)."""
    MUID = "MUID"
    LevelDepthTypeNo = "LevelDepthTypeNo"
    LevelDepth = "LevelDepth"
    DischargeTypeNo = "DischargeTypeNo"
    Discharge = "Discharge"
    UseLocalNo = "UseLocalNo"
    UseHotstartNo = "UseHotstartNo"
    Description = "Description"

class msm_HDInitialConditionTable(BaseTable):
    """Table for msm_HDInitialCondition (Initial conditions)."""
    
    @property
    def columns(self) -> msm_HDInitialConditionTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = msm_HDInitialConditionTableColumns(self)
        return self._columns