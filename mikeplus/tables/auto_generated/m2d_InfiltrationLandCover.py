from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class m2d_InfiltrationLandCoverTableColumns(BaseColumns):
    """Column names for m2d_InfiltrationLandCover (2D infiltration)."""
    MUID = "MUID"
    CodeValue = "CodeValue"
    Sqn = "Sqn"
    TypeNo = "TypeNo"
    InfRate = "InfRate"
    InfCurve = "InfCurve"
    LeakRate = "LeakRate"
    LevelDepth = "LevelDepth"
    Porosity = "Porosity"
    Percentage = "Percentage"

class m2d_InfiltrationLandCoverTable(BaseTable):
    """Table for m2d_InfiltrationLandCover (2D infiltration)."""
    
    @property
    def columns(self) -> m2d_InfiltrationLandCoverTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = m2d_InfiltrationLandCoverTableColumns(self)
        return self._columns