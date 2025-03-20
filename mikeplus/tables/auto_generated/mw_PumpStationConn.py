from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class mw_PumpStationConnTableColumns(BaseColumns):
    """Column names for mw_PumpStationConn (Pump stations connection)."""
    MUID = "MUID"
    PumpStationID = "PumpStationID"
    PumpID = "PumpID"

class mw_PumpStationConnTable(BaseTable):
    """Table for mw_PumpStationConn (Pump stations connection)."""
    
    @property
    def columns(self) -> mw_PumpStationConnTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mw_PumpStationConnTableColumns(self)
        return self._columns