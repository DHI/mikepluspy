from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class msm_HDInitialConditionTableColumns(BaseColumns):
    """Column names for msm_HDInitialCondition (Initial conditions)."""
    MUID = "MUID"
    """ID"""
    LevelDepthTypeNo = "LevelDepthTypeNo"
    """Level type"""
    LevelDepth = "LevelDepth"
    """Level depth [m]"""
    DischargeTypeNo = "DischargeTypeNo"
    """Discharge type"""
    Discharge = "Discharge"
    """Discharge [m^3/s]"""
    UseLocalNo = "UseLocalNo"
    """Use local values"""
    UseHotstartNo = "UseHotstartNo"
    """Use hotstart files"""
    Description = "Description"
    """Description"""

class msm_HDInitialConditionTable(BaseTable):
    """Table for msm_HDInitialCondition (Initial conditions)."""
    
    @property
    def columns(self) -> msm_HDInitialConditionTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = msm_HDInitialConditionTableColumns(self)
        return self._columns