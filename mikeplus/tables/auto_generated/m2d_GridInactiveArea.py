from mikeplus.tables.base_geometry_table import BaseGeometryTable
from mikeplus.tables.base_geometry_table import BaseColumns

class m2d_GridInactiveAreaTableColumns(BaseColumns):
    """Column names for m2d_GridInactiveArea (Grid inactive area)."""
    MUID = "MUID"
    """ID"""
    ApplyNo = "ApplyNo"
    """Apply"""

class m2d_GridInactiveAreaTable(BaseGeometryTable):
    """Table for m2d_GridInactiveArea (Grid inactive area)."""
    
    @property
    def columns(self) -> m2d_GridInactiveAreaTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = m2d_GridInactiveAreaTableColumns(self)
        return self._columns