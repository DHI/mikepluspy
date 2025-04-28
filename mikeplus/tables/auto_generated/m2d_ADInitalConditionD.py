from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class m2d_ADInitalConditionDTableColumns(BaseColumns):
    """Column names for m2d_ADInitalConditionD (AD initial conditions area in 2D domain)."""
    MUID = "MUID"
    InitCondID = "InitCondID"
    Sqn = "Sqn"
    ApplyNo = "ApplyNo"
    AreaID = "AreaID"
    LocalInitCond = "LocalInitCond"
    Unit = "Unit"
    Description = "Description"

class m2d_ADInitalConditionDTable(BaseTable):
    """Table for m2d_ADInitalConditionD (AD initial conditions area in 2D domain)."""
    
    @property
    def columns(self) -> m2d_ADInitalConditionDTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = m2d_ADInitalConditionDTableColumns(self)
        return self._columns