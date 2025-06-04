from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class mss_TransectTableColumns(BaseColumns):
    """Column names for mss_Transect (Transects)."""
    MUID = "MUID"
    """ID"""
    Description = "Description"
    """Description"""
    Xleft = "Xleft"
    """Left bank station [m]"""
    Xright = "Xright"
    """Right bank station [m]"""
    Wfactor = "Wfactor"
    """Horizontal shrink/expand fact"""
    Eoffset = "Eoffset"
    """Elevation offset [m]"""
    Lfactor = "Lfactor"
    """Meander ratio"""
    Nleft = "Nleft"
    """Left overbank n [s/m^(1/3)]"""
    Nright = "Nright"
    """Right overbank n [s/m^(1/3)]"""
    NChannel = "NChannel"
    """Channel n [s/m^(1/3)]"""
    ApplyCoordinateNo = "ApplyCoordinateNo"
    """ApplyCoordinateNo"""

class mss_TransectTable(BaseTable):
    """Table for mss_Transect (Transects)."""
    
    @property
    def columns(self) -> mss_TransectTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mss_TransectTableColumns(self)
        return self._columns