from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class m2d_InfRoadTableColumns(BaseColumns):
    """Column names for m2d_InfRoad (Road)."""
    MUID = "MUID"
    CodeValue = "CodeValue"
    UniformOffset = "UniformOffset"

class m2d_InfRoadTable(BaseTable):
    """Table for m2d_InfRoad (Road)."""
    
    @property
    def columns(self) -> m2d_InfRoadTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = m2d_InfRoadTableColumns(self)
        return self._columns