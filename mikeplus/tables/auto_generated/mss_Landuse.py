from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class mss_LanduseTableColumns(BaseColumns):
    """Column names for mss_Landuse (Land uses)."""
    MUID = "MUID"
    """ID"""
    SweepInterval = "SweepInterval"
    """Interval between sweeps [d]"""
    Availability = "Availability"
    """Pollutant availability [()]"""
    LastSweep = "LastSweep"
    """Last sweep [d]"""
    Description = "Description"
    """Description"""

class mss_LanduseTable(BaseTable):
    """Table for mss_Landuse (Land uses)."""
    
    @property
    def columns(self) -> mss_LanduseTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mss_LanduseTableColumns(self)
        return self._columns