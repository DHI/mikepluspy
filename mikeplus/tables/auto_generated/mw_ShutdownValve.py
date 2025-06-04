from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class mw_ShutdownValveTableColumns(BaseColumns):
    """Column names for mw_ShutdownValve (Shutdown valve)."""
    MUID = "MUID"
    """ID"""
    ShutdownID = "ShutdownID"
    """Shutdown Id"""
    StartTime = "StartTime"
    """Start time"""
    EndTime = "EndTime"
    """End time"""
    ValveID = "ValveID"
    """Valve ID"""
    PipeID = "PipeID"
    """Pipe id"""
    Description = "Description"
    """Description"""

class mw_ShutdownValveTable(BaseTable):
    """Table for mw_ShutdownValve (Shutdown valve)."""
    
    @property
    def columns(self) -> mw_ShutdownValveTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mw_ShutdownValveTableColumns(self)
        return self._columns