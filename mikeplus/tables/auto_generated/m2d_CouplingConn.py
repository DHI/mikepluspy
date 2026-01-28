from mikeplus.tables.base_geometry_table import BaseGeometryTable
from mikeplus.tables.base_geometry_table import BaseColumns

class m2d_CouplingConnTableColumns(BaseColumns):
    """Column names for m2d_CouplingConn (Couple Connection)."""
    MUID = "MUID"
    """ID"""
    CouplingID = "CouplingID"
    """Coupling ID"""
    LocationID = "LocationID"
    """Location ID"""
    LocationTypeNo = "LocationTypeNo"
    """Location Type"""

class m2d_CouplingConnTable(BaseGeometryTable):
    """Table for m2d_CouplingConn (Couple Connection)."""
    
    @property
    def columns(self) -> m2d_CouplingConnTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = m2d_CouplingConnTableColumns(self)
        return self._columns