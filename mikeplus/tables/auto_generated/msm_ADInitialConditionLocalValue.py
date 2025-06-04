from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class msm_ADInitialConditionLocalValueTableColumns(BaseColumns):
    """Column names for msm_ADInitialConditionLocalValue (Local values)."""
    MUID = "MUID"
    """MUID"""
    ADLocalID = "ADLocalID"
    """ADLocalID"""
    ComponentID = "ComponentID"
    """WQ component"""
    IncludeNo = "IncludeNo"
    """Include"""
    LocalValue = "LocalValue"
    """Local value"""
    Unit = "Unit"
    """Unit"""

class msm_ADInitialConditionLocalValueTable(BaseTable):
    """Table for msm_ADInitialConditionLocalValue (Local values)."""
    
    @property
    def columns(self) -> msm_ADInitialConditionLocalValueTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = msm_ADInitialConditionLocalValueTableColumns(self)
        return self._columns