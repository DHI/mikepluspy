from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class ms_TabDTableColumns(BaseColumns):
    """Column names for ms_TabD (Curve values)."""
    MUID = "MUID"
    TabID = "TabID"
    Sqn = "Sqn"
    DateTime = "DateTime"
    Value1 = "Value1"
    DerivedValue = "DerivedValue"
    Value2 = "Value2"
    Value3 = "Value3"
    Value4 = "Value4"

class ms_TabDTable(BaseTable):
    """Table for ms_TabD (Curve values)."""
    
    @property
    def columns(self) -> ms_TabDTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = ms_TabDTableColumns(self)
        return self._columns