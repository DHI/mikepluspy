from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class mw_ShutdownPlanningTableColumns(BaseColumns):
    """Column names for mw_ShutdownPlanning (Shutdown planning)."""
    MUID = "MUID"
    """ID"""
    ValveFilePath = "ValveFilePath"
    """Target layer"""
    ValveIDField = "ValveIDField"
    """Valve node ID"""
    ServicePre = "ServicePre"
    """Service pressure [m]"""
    Tolerance = "Tolerance"
    """Tolerance [m]"""
    UnavailableValveList = "UnavailableValveList"
    """Unavailable valves"""

class mw_ShutdownPlanningTable(BaseTable):
    """Table for mw_ShutdownPlanning (Shutdown planning)."""
    
    @property
    def columns(self) -> mw_ShutdownPlanningTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mw_ShutdownPlanningTableColumns(self)
        return self._columns