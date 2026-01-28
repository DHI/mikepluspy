from mikeplus.tables.base_geometry_table import BaseGeometryTable
from mikeplus.tables.base_geometry_table import BaseColumns

class m2d_SurfaceRoughnessAreaTableColumns(BaseColumns):
    """Column names for m2d_SurfaceRoughnessArea (2D surface roughness)."""
    Sqn = "Sqn"
    """Priority"""
    ApplyNo = "ApplyNo"
    """Apply"""
    MUID = "MUID"
    """Polygon ID"""
    TypeNo = "TypeNo"
    """Value type"""
    Material = "Material"
    """Material"""
    Roughness = "Roughness"
    """Roughness"""
    Description = "Description"
    """Description"""

class m2d_SurfaceRoughnessAreaTable(BaseGeometryTable):
    """Table for m2d_SurfaceRoughnessArea (2D surface roughness)."""
    
    @property
    def columns(self) -> m2d_SurfaceRoughnessAreaTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = m2d_SurfaceRoughnessAreaTableColumns(self)
        return self._columns