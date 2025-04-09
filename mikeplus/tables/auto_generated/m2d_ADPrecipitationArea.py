from mikeplus.tables.base_geometry_table import BaseGeometryTable
from mikeplus.tables.base_geometry_table import BaseColumns

class m2d_ADPrecipitationAreaTableColumns(BaseColumns):
    """Column names for m2d_ADPrecipitationArea (2D AD precipitation)."""
    MUID = "MUID"

class m2d_ADPrecipitationAreaTable(BaseGeometryTable):
    """Table for m2d_ADPrecipitationArea (2D AD precipitation)."""
    
    @property
    def columns(self) -> m2d_ADPrecipitationAreaTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = m2d_ADPrecipitationAreaTableColumns(self)
        return self._columns