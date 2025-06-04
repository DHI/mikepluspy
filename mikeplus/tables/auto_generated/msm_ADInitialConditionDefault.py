from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class msm_ADInitialConditionDefaultTableColumns(BaseColumns):
    """Column names for msm_ADInitialConditionDefault (Default values)."""
    MUID = "MUID"
    """MUID"""
    ADInitCondID = "ADInitCondID"
    """ADInitCondID"""
    ComponentID = "ComponentID"
    """WQ component"""
    DefaultValue = "DefaultValue"
    """Default value"""
    Unit = "Unit"
    """Unit"""

class msm_ADInitialConditionDefaultTable(BaseTable):
    """Table for msm_ADInitialConditionDefault (Default values)."""
    
    @property
    def columns(self) -> msm_ADInitialConditionDefaultTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = msm_ADInitialConditionDefaultTableColumns(self)
        return self._columns