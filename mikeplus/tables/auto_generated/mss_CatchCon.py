from mikeplus.tables.base_geometry_table import BaseGeometryTable
from mikeplus.tables.base_geometry_table import BaseColumns

class mss_CatchConTableColumns(BaseColumns):
    """Column names for mss_CatchCon (SWMM catchment connections)."""
    MUID = "MUID"
    """ID"""
    CatchID = "CatchID"
    """Catchment ID"""

class mss_CatchConTable(BaseGeometryTable):
    """Table for mss_CatchCon (SWMM catchment connections)."""
    
    @property
    def columns(self) -> mss_CatchConTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mss_CatchConTableColumns(self)
        return self._columns