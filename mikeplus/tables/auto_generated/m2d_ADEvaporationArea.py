from mikeplus.tables.base_geometry_table import BaseGeometryTable
from mikeplus.tables.base_geometry_table import BaseColumns

class m2d_ADEvaporationAreaTableColumns(BaseColumns):
    """Column names for m2d_ADEvaporationArea (2D AD evaporation)."""
    MUID = "MUID"

class m2d_ADEvaporationAreaTable(BaseGeometryTable):
    """Table for m2d_ADEvaporationArea (2D AD evaporation)."""
    
    @property
    def columns(self) -> m2d_ADEvaporationAreaTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = m2d_ADEvaporationAreaTableColumns(self)
        return self._columns