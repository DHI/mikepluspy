from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class mss_CoverageTableColumns(BaseColumns):
    """Column names for mss_Coverage (Coverage)."""
    MUID = "MUID"
    SubCatchID = "SubCatchID"
    LandUseID = "LandUseID"
    Percentage = "Percentage"

class mss_CoverageTable(BaseTable):
    """Table for mss_Coverage (Coverage)."""
    
    @property
    def columns(self) -> mss_CoverageTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mss_CoverageTableColumns(self)
        return self._columns