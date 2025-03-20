from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class mss_LIDControlDTableColumns(BaseColumns):
    """Column names for mss_LIDControlD (LIDControlD)."""
    MUID = "MUID"
    LIDControlID = "LIDControlID"
    PollutantID = "PollutantID"
    Removal = "Removal"

class mss_LIDControlDTable(BaseTable):
    """Table for mss_LIDControlD (LIDControlD)."""
    
    @property
    def columns(self) -> mss_LIDControlDTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mss_LIDControlDTableColumns(self)
        return self._columns