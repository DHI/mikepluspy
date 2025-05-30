from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class m2d_StructureWeirDTableColumns(BaseColumns):
    """Column names for m2d_StructureWeirD (2D weir geometry)."""
    MUID = "MUID"
    WeirID = "WeirID"
    Sqn = "Sqn"
    Level = "Level"
    Width = "Width"

class m2d_StructureWeirDTable(BaseTable):
    """Table for m2d_StructureWeirD (2D weir geometry)."""
    
    @property
    def columns(self) -> m2d_StructureWeirDTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = m2d_StructureWeirDTableColumns(self)
        return self._columns