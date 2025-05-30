from mikeplus.tables.base_geometry_table import BaseGeometryTable
from mikeplus.tables.base_geometry_table import BaseColumns

class mw_DemAllocConnTableColumns(BaseColumns):
    """Column names for mw_DemAllocConn (Demand allocation connection)."""
    MUID = "MUID"
    LocationID = "LocationID"
    DemAllocID = "DemAllocID"
    LocationTypeNo = "LocationTypeNo"

class mw_DemAllocConnTable(BaseGeometryTable):
    """Table for mw_DemAllocConn (Demand allocation connection)."""
    
    @property
    def columns(self) -> mw_DemAllocConnTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mw_DemAllocConnTableColumns(self)
        return self._columns