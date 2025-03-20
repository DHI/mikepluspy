from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class mw_WH_BoundaryTableColumns(BaseColumns):
    """Column names for mw_WH_Boundary (Boundary conditions)."""
    MUID = "MUID"
    NodeTypeNo = "NodeTypeNo"
    NodeID = "NodeID"
    TypeNo = "TypeNo"
    CurveID = "CurveID"
    Description = "Description"

class mw_WH_BoundaryTable(BaseTable):
    """Table for mw_WH_Boundary (Boundary conditions)."""
    
    @property
    def columns(self) -> mw_WH_BoundaryTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mw_WH_BoundaryTableColumns(self)
        return self._columns