from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class msm_ADComponentTableColumns(BaseColumns):
    """Column names for msm_ADComponent (WQ components)."""
    MUID = "MUID"
    DecayConst = "DecayConst"
    TypeNo = "TypeNo"
    Unit = "Unit"
    UnitNo = "UnitNo"
    Description = "Description"

class msm_ADComponentTable(BaseTable):
    """Table for msm_ADComponent (WQ components)."""
    
    @property
    def columns(self) -> msm_ADComponentTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = msm_ADComponentTableColumns(self)
        return self._columns