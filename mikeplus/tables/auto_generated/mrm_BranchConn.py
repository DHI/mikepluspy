from mikeplus.tables.base_geometry_table import BaseGeometryTable
from mikeplus.tables.base_geometry_table import BaseColumns

class mrm_BranchConnTableColumns(BaseColumns):
    """Column names for mrm_BranchConn (River connection)."""
    MUID = "MUID"
    BranchID = "BranchID"
    TypeNo = "TypeNo"
    ToID = "ToID"
    ToTypeNo = "ToTypeNo"
    ToChainage = "ToChainage"

class mrm_BranchConnTable(BaseGeometryTable):
    """Table for mrm_BranchConn (River connection)."""
    
    @property
    def columns(self) -> mrm_BranchConnTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mrm_BranchConnTableColumns(self)
        return self._columns