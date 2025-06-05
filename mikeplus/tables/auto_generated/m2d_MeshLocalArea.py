from mikeplus.tables.base_geometry_table import BaseGeometryTable
from mikeplus.tables.base_geometry_table import BaseColumns

class m2d_MeshLocalAreaTableColumns(BaseColumns):
    """Column names for m2d_MeshLocalArea (Mesh polygon marker)."""
    MUID = "MUID"
    """Marker ID"""
    GeomX = "GeomX"
    """X coordinate [m]"""
    GeomY = "GeomY"
    """Y coordinate [m]"""
    UseLocalNo = "UseLocalNo"
    """Use local setting"""
    LocalOptionNo = "LocalOptionNo"
    """Polygon option"""
    LocalMaxArea = "LocalMaxArea"
    """Local maximum area [m^2]"""

class m2d_MeshLocalAreaTable(BaseGeometryTable):
    """Table for m2d_MeshLocalArea (Mesh polygon marker)."""
    
    @property
    def columns(self) -> m2d_MeshLocalAreaTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = m2d_MeshLocalAreaTableColumns(self)
        return self._columns