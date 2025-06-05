from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class mss_TransectDTableColumns(BaseColumns):
    """Column names for mss_TransectD (Transects data)."""
    MUID = "MUID"
    """MUID"""
    TransectID = "TransectID"
    """TransectID"""
    Sqn = "Sqn"
    """Sqn"""
    Station = "Station"
    """Station [m]"""
    Elevation = "Elevation"
    """Elevation [m]"""

class mss_TransectDTable(BaseTable):
    """Table for mss_TransectD (Transects data)."""
    
    @property
    def columns(self) -> mss_TransectDTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mss_TransectDTableColumns(self)
        return self._columns