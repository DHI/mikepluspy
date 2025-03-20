from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class m2d_StructureDikeTableColumns(BaseColumns):
    """Column names for m2d_StructureDike (2D dikes)."""
    MUID = "MUID"
    ApplyNo = "ApplyNo"
    DampDepth = "DampDepth"
    WeirCoef = "WeirCoef"
    ChangeType = "ChangeType"
    CorrDatum = "CorrDatum"
    CorrFile = "CorrFile"
    CorrItem = "CorrItem"
    CorrItemNo = "CorrItemNo"
    DataSource = "DataSource"
    Element_S = "Element_S"
    Description = "Description"

class m2d_StructureDikeTable(BaseTable):
    """Table for m2d_StructureDike (2D dikes)."""
    
    @property
    def columns(self) -> m2d_StructureDikeTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = m2d_StructureDikeTableColumns(self)
        return self._columns