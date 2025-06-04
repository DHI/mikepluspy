from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class mw_CurveDTableColumns(BaseColumns):
    """Column names for mw_CurveD (Curve values)."""
    MUID = "MUID"
    """MUID"""
    CurveID = "CurveID"
    """CurveID"""
    Sqn = "Sqn"
    """Sqn"""
    Val1 = "Val1"
    """Value1"""
    Val2 = "Val2"
    """Value2"""
    Val3 = "Val3"
    """Val3"""
    Val4 = "Val4"
    """Val4"""

class mw_CurveDTable(BaseTable):
    """Table for mw_CurveD (Curve values)."""
    
    @property
    def columns(self) -> mw_CurveDTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mw_CurveDTableColumns(self)
        return self._columns