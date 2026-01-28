from mikeplus.tables.base_geometry_table import BaseGeometryTable
from mikeplus.tables.base_geometry_table import BaseColumns

class mrm_UserDefinedChainageTableColumns(BaseColumns):
    """Column names for mrm_UserDefinedChainage (User defined chainage)."""
    MUID = "MUID"
    """MUID"""
    BranchID = "BranchID"
    """BranchID"""
    VertexIndex = "VertexIndex"
    """VertexIndex"""
    GeomX = "GeomX"
    """X [m]"""
    GeomY = "GeomY"
    """Y [m]"""
    Chainage = "Chainage"
    """Chainage [m]"""

class mrm_UserDefinedChainageTable(BaseGeometryTable):
    """Table for mrm_UserDefinedChainage (User defined chainage)."""
    
    @property
    def columns(self) -> mrm_UserDefinedChainageTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mrm_UserDefinedChainageTableColumns(self)
        return self._columns