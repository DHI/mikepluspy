from mikeplus.tables.base_geometry_table import BaseGeometryTable
from mikeplus.tables.base_geometry_table import BaseColumns

class mw_PumpStationConnTableColumns(BaseColumns):
    """Column names for mw_PumpStationConn (Pump stations connection)."""
    MUID = "MUID"
    """ID"""
    PumpStationID = "PumpStationID"
    """Description"""
    PumpID = "PumpID"
    """Description"""

class mw_PumpStationConnTable(BaseGeometryTable):
    """Table for mw_PumpStationConn (Pump stations connection)."""
    
    @property
    def columns(self) -> mw_PumpStationConnTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mw_PumpStationConnTableColumns(self)
        return self._columns