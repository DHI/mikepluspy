from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class mss_TabDTableColumns(BaseColumns):
    """Column names for mss_TabD (Curve values)."""
    MUID = "MUID"
    TabID = "TabID"
    Sqn = "Sqn"
    Value1 = "Value1"
    Value2 = "Value2"

class mss_TabDTable(BaseTable):
    """Table for mss_TabD (Curve values)."""
    
    @property
    def columns(self) -> mss_TabDTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mss_TabDTableColumns(self)
        return self._columns