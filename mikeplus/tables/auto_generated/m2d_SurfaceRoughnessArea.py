from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class m2d_SurfaceRoughnessAreaTableColumns(BaseColumns):
    """Column names for m2d_SurfaceRoughnessArea (2D surface roughness)."""
    Sqn = "Sqn"
    ApplyNo = "ApplyNo"
    MUID = "MUID"
    TypeNo = "TypeNo"
    Material = "Material"
    Roughness = "Roughness"
    Description = "Description"

class m2d_SurfaceRoughnessAreaTable(BaseTable):
    """Table for m2d_SurfaceRoughnessArea (2D surface roughness)."""
    
    @property
    def columns(self) -> m2d_SurfaceRoughnessAreaTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = m2d_SurfaceRoughnessAreaTableColumns(self)
        return self._columns