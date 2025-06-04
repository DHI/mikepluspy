from mikeplus.tables.base_geometry_table import BaseGeometryTable
from mikeplus.tables.base_geometry_table import BaseColumns

class mw_PumpStationTableColumns(BaseColumns):
    """Column names for mw_PumpStation (Pump stations)."""
    MUID = "MUID"
    """ID"""
    GeomCentroidX = "GeomCentroidX"
    """X coordinate [m]"""
    GeomCentroidY = "GeomCentroidY"
    """Y coordinate [m]"""
    GeomArea = "GeomArea"
    """Geom area [ha]"""
    Comment = "Comment"
    """Description"""
    Picture = "Picture"
    """Description"""
    Description = "Description"
    """Description"""
    Note = "Note"
    """Note"""

class mw_PumpStationTable(BaseGeometryTable):
    """Table for mw_PumpStation (Pump stations)."""
    
    @property
    def columns(self) -> mw_PumpStationTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mw_PumpStationTableColumns(self)
        return self._columns