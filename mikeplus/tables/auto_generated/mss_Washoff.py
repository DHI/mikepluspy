from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class mss_WashoffTableColumns(BaseColumns):
    """Column names for mss_Washoff (Washoff)."""
    MUID = "MUID"
    """MUID"""
    LanduseID = "LanduseID"
    """LanduseID"""
    PollutantID = "PollutantID"
    """Pollutant ID"""
    FuncTypeNo = "FuncTypeNo"
    """Function type"""
    C1 = "C1"
    """Coefficient [()]"""
    C2 = "C2"
    """Exponent [()]"""
    SweepEfficiency = "SweepEfficiency"
    """Cleaning efficiency [%]"""
    BMPEfficiency = "BMPEfficiency"
    """BMP efficiency [%]"""

class mss_WashoffTable(BaseTable):
    """Table for mss_Washoff (Washoff)."""
    
    @property
    def columns(self) -> mss_WashoffTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mss_WashoffTableColumns(self)
        return self._columns