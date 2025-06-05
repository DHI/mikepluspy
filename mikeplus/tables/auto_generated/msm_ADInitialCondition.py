from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class msm_ADInitialConditionTableColumns(BaseColumns):
    """Column names for msm_ADInitialCondition (AD initial conditions)."""
    MUID = "MUID"
    """ID"""
    Description = "Description"
    """Description"""
    UseLocalNo = "UseLocalNo"
    """Use local values"""
    UseHotstartNo = "UseHotstartNo"
    """Use hotstart files"""

class msm_ADInitialConditionTable(BaseTable):
    """Table for msm_ADInitialCondition (AD initial conditions)."""
    
    @property
    def columns(self) -> msm_ADInitialConditionTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = msm_ADInitialConditionTableColumns(self)
        return self._columns