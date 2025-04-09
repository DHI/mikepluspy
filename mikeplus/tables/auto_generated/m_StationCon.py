from mikeplus.tables.base_geometry_table import BaseGeometryTable
from mikeplus.tables.base_geometry_table import BaseColumns

class m_StationConTableColumns(BaseColumns):
    """Column names for m_StationCon (Sensor connections)."""
    MUID = "MUID"
    StationID = "StationID"
    LocationID = "LocationID"
    LocationTypeNo = "LocationTypeNo"

class m_StationConTable(BaseGeometryTable):
    """Table for m_StationCon (Sensor connections)."""
    
    @property
    def columns(self) -> m_StationConTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = m_StationConTableColumns(self)
        return self._columns