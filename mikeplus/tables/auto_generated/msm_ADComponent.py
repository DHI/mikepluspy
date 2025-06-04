from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class msm_ADComponentTableColumns(BaseColumns):
    """Column names for msm_ADComponent (WQ components)."""
    MUID = "MUID"
    """ID"""
    DecayConst = "DecayConst"
    """Decay [/h]"""
    TypeNo = "TypeNo"
    """Type"""
    Unit = "Unit"
    """Unit"""
    UnitNo = "UnitNo"
    """UnitNo"""
    Description = "Description"
    """Description"""

class msm_ADComponentTable(BaseTable):
    """Table for msm_ADComponent (WQ components)."""
    
    @property
    def columns(self) -> msm_ADComponentTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = msm_ADComponentTableColumns(self)
        return self._columns