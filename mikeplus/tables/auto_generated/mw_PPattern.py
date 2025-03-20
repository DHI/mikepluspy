from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class mw_PPatternTableColumns(BaseColumns):
    """Column names for mw_PPattern (Patterns)."""
    MUID = "MUID"
    TypeNo = "TypeNo"
    Category = "Category"
    Description = "Description"
    UseAbsDateTime = "UseAbsDateTime"
    Duration = "Duration"
    MonF = "MonF"
    TueF = "TueF"
    WedF = "WedF"
    ThuF = "ThuF"
    FriF = "FriF"
    SatF = "SatF"
    SunF = "SunF"
    JanF = "JanF"
    FebF = "FebF"
    MarF = "MarF"
    AprF = "AprF"
    MayF = "MayF"
    JunF = "JunF"
    JulF = "JulF"
    AugF = "AugF"
    SepF = "SepF"
    OctF = "OctF"
    NovF = "NovF"
    DecF = "DecF"

class mw_PPatternTable(BaseTable):
    """Table for mw_PPattern (Patterns)."""
    
    @property
    def columns(self) -> mw_PPatternTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mw_PPatternTableColumns(self)
        return self._columns