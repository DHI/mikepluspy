from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class mss_ProjectEventsTableColumns(BaseColumns):
    """Column names for mss_ProjectEvents (Events)."""
    MUID = "MUID"
    SimulationID = "SimulationID"
    StartTime = "StartTime"
    EndTime = "EndTime"
    IncludeEvent = "IncludeEvent"

class mss_ProjectEventsTable(BaseTable):
    """Table for mss_ProjectEvents (Events)."""
    
    @property
    def columns(self) -> mss_ProjectEventsTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mss_ProjectEventsTableColumns(self)
        return self._columns