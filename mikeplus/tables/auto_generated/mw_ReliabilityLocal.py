from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class mw_ReliabilityLocalTableColumns(BaseColumns):
    """Column names for mw_ReliabilityLocal (Pressure dependent demands)."""
    MUID = "MUID"
    """ID"""
    JunctionID = "JunctionID"
    """Junction Id"""
    IsPressureDependent = "IsPressureDependent"
    """Is pressure dependent"""
    HasLocalData = "HasLocalData"
    """Has local data"""
    MinPre = "MinPre"
    """Minimum pressure [m]"""
    RequiredPre = "RequiredPre"
    """Required pressure [m]"""
    Description = "Description"
    """Description"""

class mw_ReliabilityLocalTable(BaseTable):
    """Table for mw_ReliabilityLocal (Pressure dependent demands)."""
    
    @property
    def columns(self) -> mw_ReliabilityLocalTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mw_ReliabilityLocalTableColumns(self)
        return self._columns