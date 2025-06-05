from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class ms_CRSDTableColumns(BaseColumns):
    """Column names for ms_CRSD (Raw data)."""
    MUID = "MUID"
    """MUID"""
    CrsID = "CrsID"
    """CrsID"""
    Sqn = "Sqn"
    """Sqn"""
    HX = "HX"
    """H [m]"""
    WZ = "WZ"
    """W [m]"""
    RelRes = "RelRes"
    """Relative roughness"""
    MarksValue = "MarksValue"
    """Marker"""
    MarksString = "MarksString"
    """Marker"""
    MarksValue1 = "MarksValue1"
    """Left levee bank"""
    MarksValue2 = "MarksValue2"
    """Lowest point/River alignment"""
    MarksValue3 = "MarksValue3"
    """Right levee bank"""
    MarksValue4 = "MarksValue4"
    """Left low flow bank"""
    MarksValue5 = "MarksValue5"
    """Right low flow bank"""

class ms_CRSDTable(BaseTable):
    """Table for ms_CRSD (Raw data)."""
    
    @property
    def columns(self) -> ms_CRSDTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = ms_CRSDTableColumns(self)
        return self._columns