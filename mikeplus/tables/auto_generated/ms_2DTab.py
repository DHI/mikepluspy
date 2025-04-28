from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class ms_2DTabTableColumns(BaseColumns):
    """Column names for ms_2DTab (Two-dimensional tables)."""
    MUID = "MUID"
    TypeNo = "TypeNo"
    Description = "Description"

class ms_2DTabTable(BaseTable):
    """Table for ms_2DTab (Two-dimensional tables)."""
    
    @property
    def columns(self) -> ms_2DTabTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = ms_2DTabTableColumns(self)
        return self._columns