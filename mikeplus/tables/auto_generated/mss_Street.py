from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class mss_StreetTableColumns(BaseColumns):
    """Column names for mss_Street (Streets)."""
    MUID = "MUID"
    """ID"""
    RoadWidth = "RoadWidth"
    """Road width (Tcrown) [m]"""
    CurbHeight = "CurbHeight"
    """Curb height (Hcurb) [m]"""
    CrossSlope = "CrossSlope"
    """Cross slope (Sx) [%]"""
    RoadRoughness = "RoadRoughness"
    """Road roughness [s/m^(1/3)]"""
    NumSidesTypeNo = "NumSidesTypeNo"
    """Number of sides"""
    GutterDepression = "GutterDepression"
    """Gutter depression (a) [m]"""
    GutterWidth = "GutterWidth"
    """Gutter width (W) [m]"""
    BackingWidth = "BackingWidth"
    """Backing width (Tback) [m]"""
    BackingSlope = "BackingSlope"
    """Backing slope (Sback) [%]"""
    BackingRoughness = "BackingRoughness"
    """Backing roughness [s/m^(1/3)]"""
    Description = "Description"
    """Description"""

class mss_StreetTable(BaseTable):
    """Table for mss_Street (Streets)."""
    
    @property
    def columns(self) -> mss_StreetTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mss_StreetTableColumns(self)
        return self._columns