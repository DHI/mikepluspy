from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class mss_HydrographTableColumns(BaseColumns):
    """Column names for mss_Hydrograph (RDII hydrographs)."""
    MUID = "MUID"
    RaingageID = "RaingageID"
    Description = "Description"

class mss_HydrographTable(BaseTable):
    """Table for mss_Hydrograph (RDII hydrographs)."""
    
    @property
    def columns(self) -> mss_HydrographTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mss_HydrographTableColumns(self)
        return self._columns