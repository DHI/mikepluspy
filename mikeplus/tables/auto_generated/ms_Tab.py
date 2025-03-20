from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class ms_TabTableColumns(BaseColumns):
    """Column names for ms_Tab (Curves and relations)."""
    MUID = "MUID"
    TypeNo = "TypeNo"
    Description = "Description"

class ms_TabTable(BaseTable):
    """Table for ms_Tab (Curves and relations)."""
    
    @property
    def columns(self) -> ms_TabTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = ms_TabTableColumns(self)
        return self._columns