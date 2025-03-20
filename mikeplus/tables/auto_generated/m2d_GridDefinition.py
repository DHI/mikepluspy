from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class m2d_GridDefinitionTableColumns(BaseColumns):
    """Column names for m2d_GridDefinition (Grid definition)."""
    MUID = "MUID"
    Projection = "Projection"
    Easting = "Easting"
    Northing = "Northing"
    UpperRightEasting = "UpperRightEasting"
    UpperRightNorthing = "UpperRightNorthing"
    ProjNYCRotation = "ProjNYCRotation"
    CellXSpacing = "CellXSpacing"
    CellYSpacing = "CellYSpacing"
    LandValueOptionNo = "LandValueOptionNo"
    LandValue = "LandValue"
    GridLandValueRelative = "GridLandValueRelative"
    GridBoundaryWidth = "GridBoundaryWidth"
    GridIndent = "GridIndent"

class m2d_GridDefinitionTable(BaseTable):
    """Table for m2d_GridDefinition (Grid definition)."""
    
    @property
    def columns(self) -> m2d_GridDefinitionTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = m2d_GridDefinitionTableColumns(self)
        return self._columns