from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class mw_EPAMSXTableColumns(BaseColumns):
    """Column names for mw_EPAMSX (Multi-species analysis)."""
    MUID = "MUID"
    Description = "Description"
    Content = "Content"

class mw_EPAMSXTable(BaseTable):
    """Table for mw_EPAMSX (Multi-species analysis)."""
    
    @property
    def columns(self) -> mw_EPAMSXTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mw_EPAMSXTableColumns(self)
        return self._columns