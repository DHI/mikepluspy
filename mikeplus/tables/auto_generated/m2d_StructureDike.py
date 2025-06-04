from mikeplus.tables.base_geometry_table import BaseGeometryTable
from mikeplus.tables.base_geometry_table import BaseColumns

class m2d_StructureDikeTableColumns(BaseColumns):
    """Column names for m2d_StructureDike (2D dikes)."""
    MUID = "MUID"
    """ID"""
    ApplyNo = "ApplyNo"
    """Apply"""
    DampDepth = "DampDepth"
    """Dampening delta depth [m]"""
    WeirCoef = "WeirCoef"
    """Weir coefficient"""
    ChangeType = "ChangeType"
    """Relative change type"""
    CorrDatum = "CorrDatum"
    """Datum [m]"""
    CorrFile = "CorrFile"
    """Change file"""
    CorrItem = "CorrItem"
    """Item"""
    CorrItemNo = "CorrItemNo"
    """CorrItemNo"""
    DataSource = "DataSource"
    """Data source"""
    Element_S = "Element_S"
    """Status"""
    Description = "Description"
    """Description"""

class m2d_StructureDikeTable(BaseGeometryTable):
    """Table for m2d_StructureDike (2D dikes)."""
    
    @property
    def columns(self) -> m2d_StructureDikeTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = m2d_StructureDikeTableColumns(self)
        return self._columns