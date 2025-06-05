from mikeplus.tables.base_geometry_table import BaseGeometryTable
from mikeplus.tables.base_geometry_table import BaseColumns

class m2d_ADInitalConditionAreaTableColumns(BaseColumns):
    """Column names for m2d_ADInitalConditionArea (2D AD initial conditions)."""
    MUID = "MUID"
    """Polygon ID"""

class m2d_ADInitalConditionAreaTable(BaseGeometryTable):
    """Table for m2d_ADInitalConditionArea (2D AD initial conditions)."""
    
    @property
    def columns(self) -> m2d_ADInitalConditionAreaTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = m2d_ADInitalConditionAreaTableColumns(self)
        return self._columns