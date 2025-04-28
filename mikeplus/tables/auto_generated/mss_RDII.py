from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class mss_RDIITableColumns(BaseColumns):
    """Column names for mss_RDII (RDII)."""
    MUID = "MUID"
    NodeID = "NodeID"
    HydrographID = "HydrographID"
    SewerArea = "SewerArea"
    Description = "Description"

class mss_RDIITable(BaseTable):
    """Table for mss_RDII (RDII)."""
    
    @property
    def columns(self) -> mss_RDIITableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mss_RDIITableColumns(self)
        return self._columns