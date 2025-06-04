from mikeplus.tables.base_geometry_table import BaseGeometryTable
from mikeplus.tables.base_geometry_table import BaseColumns

class m2d_ADInfiltrationAreaTableColumns(BaseColumns):
    """Column names for m2d_ADInfiltrationArea (2D AD infiltration)."""
    MUID = "MUID"
    """Polygon ID"""

class m2d_ADInfiltrationAreaTable(BaseGeometryTable):
    """Table for m2d_ADInfiltrationArea (2D AD infiltration)."""
    
    @property
    def columns(self) -> m2d_ADInfiltrationAreaTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = m2d_ADInfiltrationAreaTableColumns(self)
        return self._columns