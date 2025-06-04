from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class mss_TabTableColumns(BaseColumns):
    """Column names for mss_Tab (Curves and relations)."""
    MUID = "MUID"
    """ID"""
    TypeNo = "TypeNo"
    """Type"""
    Description = "Description"
    """Description"""

class mss_TabTable(BaseTable):
    """Table for mss_Tab (Curves and relations)."""
    
    @property
    def columns(self) -> mss_TabTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mss_TabTableColumns(self)
        return self._columns