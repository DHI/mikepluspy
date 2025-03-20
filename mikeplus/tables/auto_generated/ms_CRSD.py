from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class ms_CRSDTableColumns(BaseColumns):
    """Column names for ms_CRSD (Raw data)."""
    MUID = "MUID"
    CrsID = "CrsID"
    Sqn = "Sqn"
    HX = "HX"
    WZ = "WZ"
    RelRes = "RelRes"
    MarksValue = "MarksValue"
    MarksString = "MarksString"
    MarksValue1 = "MarksValue1"
    MarksValue2 = "MarksValue2"
    MarksValue3 = "MarksValue3"
    MarksValue4 = "MarksValue4"
    MarksValue5 = "MarksValue5"

class ms_CRSDTable(BaseTable):
    """Table for ms_CRSD (Raw data)."""
    
    @property
    def columns(self) -> ms_CRSDTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = ms_CRSDTableColumns(self)
        return self._columns