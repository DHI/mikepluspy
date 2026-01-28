from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class mss_StreetTableColumns(BaseColumns):
    """Column names for mss_Street (Streets)."""
    MUID = "MUID"
    RoadWidth = "RoadWidth"
    CurbHeight = "CurbHeight"
    CrossSlope = "CrossSlope"
    RoadRoughness = "RoadRoughness"
    NumSidesTypeNo = "NumSidesTypeNo"
    GutterDepression = "GutterDepression"
    GutterWidth = "GutterWidth"
    BackingWidth = "BackingWidth"
    BackingSlope = "BackingSlope"
    BackingRoughness = "BackingRoughness"
    Description = "Description"

class mss_StreetTable(BaseTable):
    """Table for mss_Street (Streets)."""
    
    @property
    def columns(self) -> mss_StreetTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mss_StreetTableColumns(self)
        return self._columns