from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class mss_TransectTableColumns(BaseColumns):
    """Column names for mss_Transect (Transects)."""
    MUID = "MUID"
    Description = "Description"
    Xleft = "Xleft"
    Xright = "Xright"
    Wfactor = "Wfactor"
    Eoffset = "Eoffset"
    Lfactor = "Lfactor"
    Nleft = "Nleft"
    Nright = "Nright"
    NChannel = "NChannel"
    ApplyCoordinateNo = "ApplyCoordinateNo"

class mss_TransectTable(BaseTable):
    """Table for mss_Transect (Transects)."""
    
    @property
    def columns(self) -> mss_TransectTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mss_TransectTableColumns(self)
        return self._columns