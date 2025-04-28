from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class mss_TransectCoordTableColumns(BaseColumns):
    """Column names for mss_TransectCoord (Transects data)."""
    MUID = "MUID"
    TransectID = "TransectID"
    Sqn = "Sqn"
    X = "X"
    Y = "Y"

class mss_TransectCoordTable(BaseTable):
    """Table for mss_TransectCoord (Transects data)."""
    
    @property
    def columns(self) -> mss_TransectCoordTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mss_TransectCoordTableColumns(self)
        return self._columns