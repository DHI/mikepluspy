from mikeplus.tables.base_geometry_table import BaseGeometryTable
from mikeplus.tables.base_geometry_table import BaseColumns

class m2d_InitialConditionAreaTableColumns(BaseColumns):
    """Column names for m2d_InitialConditionArea (2D initial conditions)."""
    Sqn = "Sqn"
    """Priority"""
    ApplyNo = "ApplyNo"
    """Apply"""
    MUID = "MUID"
    """Polygon ID"""
    WaterLevel = "WaterLevel"
    """Water level [m]"""
    Description = "Description"
    """Description"""

class m2d_InitialConditionAreaTable(BaseGeometryTable):
    """Table for m2d_InitialConditionArea (2D initial conditions)."""
    
    @property
    def columns(self) -> m2d_InitialConditionAreaTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = m2d_InitialConditionAreaTableColumns(self)
        return self._columns