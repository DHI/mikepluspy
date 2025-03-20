from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class mw_ReliabilityLocalTableColumns(BaseColumns):
    """Column names for mw_ReliabilityLocal (Pressure dependent demands)."""
    MUID = "MUID"
    JunctionID = "JunctionID"
    IsPressureDependent = "IsPressureDependent"
    HasLocalData = "HasLocalData"
    MinPre = "MinPre"
    RequiredPre = "RequiredPre"
    Description = "Description"

class mw_ReliabilityLocalTable(BaseTable):
    """Table for mw_ReliabilityLocal (Pressure dependent demands)."""
    
    @property
    def columns(self) -> mw_ReliabilityLocalTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mw_ReliabilityLocalTableColumns(self)
        return self._columns