from mikeplus.tables.base_geometry_table import BaseGeometryTable
from mikeplus.tables.base_geometry_table import BaseColumns

class msm_RSTableColumns(BaseColumns):
    """Column names for msm_RS (Result files)."""
    MUID = "MUID"
    """ID"""
    ModelTypeNo = "ModelTypeNo"
    """Model type"""
    ContentTypeNo = "ContentTypeNo"
    """Content type"""
    FormatNo = "FormatNo"
    """Format"""
    DefaultNo = "DefaultNo"
    """DefaultNo"""
    SubmeshResultNo = "SubmeshResultNo"
    """Submesh"""
    SubmeshLowerLeftX = "SubmeshLowerLeftX"
    """Lower left coordinate (X) [m]"""
    SubmeshLowerLeftY = "SubmeshLowerLeftY"
    """Lower left coordinate (Y) [m]"""
    SubmeshCellSizeX = "SubmeshCellSizeX"
    """Cell size (X) [m]"""
    SubmeshCellSizeY = "SubmeshCellSizeY"
    """Cell size (Y) [m]"""
    SubmeshNoCellsX = "SubmeshNoCellsX"
    """Number of cells (X)"""
    SubmeshNoCellsY = "SubmeshNoCellsY"
    """Number of cells (Y)"""

class msm_RSTable(BaseGeometryTable):
    """Table for msm_RS (Result files)."""
    
    @property
    def columns(self) -> msm_RSTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = msm_RSTableColumns(self)
        return self._columns