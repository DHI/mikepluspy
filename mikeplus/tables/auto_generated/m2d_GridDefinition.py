from mikeplus.tables.base_geometry_table import BaseGeometryTable
from mikeplus.tables.base_geometry_table import BaseColumns

class m2d_GridDefinitionTableColumns(BaseColumns):
    """Column names for m2d_GridDefinition (Grid definition)."""
    MUID = "MUID"
    """ID"""
    Projection = "Projection"
    """Projection"""
    Easting = "Easting"
    """Easting [m]"""
    Northing = "Northing"
    """Northing [m]"""
    UpperRightEasting = "UpperRightEasting"
    """Upper right easting [m]"""
    UpperRightNorthing = "UpperRightNorthing"
    """Upper right northing [m]"""
    ProjNYCRotation = "ProjNYCRotation"
    """Rotation [deg]"""
    CellXSpacing = "CellXSpacing"
    """Cell X spacing [m]"""
    CellYSpacing = "CellYSpacing"
    """Cell Y spacing [m]"""
    LandValueOptionNo = "LandValueOptionNo"
    """Land value option No."""
    LandValue = "LandValue"
    """Land value [m]"""
    GridLandValueRelative = "GridLandValueRelative"
    """Land value relative [m]"""
    GridBoundaryWidth = "GridBoundaryWidth"
    """Boundary width"""
    GridIndent = "GridIndent"
    """Indent"""

class m2d_GridDefinitionTable(BaseGeometryTable):
    """Table for m2d_GridDefinition (Grid definition)."""
    
    @property
    def columns(self) -> m2d_GridDefinitionTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = m2d_GridDefinitionTableColumns(self)
        return self._columns