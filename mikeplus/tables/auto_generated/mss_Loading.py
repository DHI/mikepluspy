from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class mss_LoadingTableColumns(BaseColumns):
    """Column names for mss_Loading (Initial loading)."""
    MUID = "MUID"
    """ID"""
    CatchID = "CatchID"
    """Catchment ID"""
    PollutantID = "PollutantID"
    """Pollutant ID"""
    InitBuildUp = "InitBuildUp"
    """Initial buildup [kg/ha]"""
    Description = "Description"
    """Description"""

class mss_LoadingTable(BaseTable):
    """Table for mss_Loading (Initial loading)."""
    
    @property
    def columns(self) -> mss_LoadingTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mss_LoadingTableColumns(self)
        return self._columns