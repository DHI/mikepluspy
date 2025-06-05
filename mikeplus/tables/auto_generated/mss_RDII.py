from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class mss_RDIITableColumns(BaseColumns):
    """Column names for mss_RDII (RDII)."""
    MUID = "MUID"
    """ID"""
    NodeID = "NodeID"
    """Node ID"""
    HydrographID = "HydrographID"
    """Hydrograph ID"""
    SewerArea = "SewerArea"
    """Sewershed area [ha]"""
    Description = "Description"
    """Description"""

class mss_RDIITable(BaseTable):
    """Table for mss_RDII (RDII)."""
    
    @property
    def columns(self) -> mss_RDIITableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mss_RDIITableColumns(self)
        return self._columns