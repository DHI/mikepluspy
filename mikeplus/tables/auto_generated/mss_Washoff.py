from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class mss_WashoffTableColumns(BaseColumns):
    """Column names for mss_Washoff (Washoff)."""
    MUID = "MUID"
    LanduseID = "LanduseID"
    PollutantID = "PollutantID"
    FuncTypeNo = "FuncTypeNo"
    C1 = "C1"
    C2 = "C2"
    SweepEfficiency = "SweepEfficiency"
    BMPEfficiency = "BMPEfficiency"

class mss_WashoffTable(BaseTable):
    """Table for mss_Washoff (Washoff)."""
    
    @property
    def columns(self) -> mss_WashoffTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mss_WashoffTableColumns(self)
        return self._columns