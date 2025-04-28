from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class m2d_StructureCulvertDTableColumns(BaseColumns):
    """Column names for m2d_StructureCulvertD (2D culvert geometry)."""
    MUID = "MUID"
    CulvertID = "CulvertID"
    Sqn = "Sqn"
    Level = "Level"
    Width = "Width"

class m2d_StructureCulvertDTable(BaseTable):
    """Table for m2d_StructureCulvertD (2D culvert geometry)."""
    
    @property
    def columns(self) -> m2d_StructureCulvertDTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = m2d_StructureCulvertDTableColumns(self)
        return self._columns