from mikeplus.tables.base_geometry_table import BaseGeometryTable
from mikeplus.tables.base_geometry_table import BaseColumns

class m2d_MeshLocalAreaTableColumns(BaseColumns):
    """Column names for m2d_MeshLocalArea (Mesh polygon marker)."""
    MUID = "MUID"
    GeomX = "GeomX"
    GeomY = "GeomY"
    UseLocalNo = "UseLocalNo"
    LocalOptionNo = "LocalOptionNo"
    LocalMaxArea = "LocalMaxArea"

class m2d_MeshLocalAreaTable(BaseGeometryTable):
    """Table for m2d_MeshLocalArea (Mesh polygon marker)."""
    
    @property
    def columns(self) -> m2d_MeshLocalAreaTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = m2d_MeshLocalAreaTableColumns(self)
        return self._columns