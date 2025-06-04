from mikeplus.tables.base_geometry_table import BaseGeometryTable
from mikeplus.tables.base_geometry_table import BaseColumns

class mwRes_ValveCriticalityTableColumns(BaseColumns):
    """Column names for mwRes_ValveCriticality (Valve criticality)."""
    MUID = "MUID"
    """ID"""
    ValveID = "ValveID"
    """Valve ID"""
    NoClosedValve = "NoClosedValve"
    """No of closed valves"""
    ListClosedPipe = "ListClosedPipe"
    """Closed pipes"""
    ListClosedValve = "ListClosedValve"
    """Closed valves"""
    sumlength = "sumlength"
    """Sum length of pipe"""

class mwRes_ValveCriticalityTable(BaseGeometryTable):
    """Table for mwRes_ValveCriticality (Valve criticality)."""
    
    @property
    def columns(self) -> mwRes_ValveCriticalityTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mwRes_ValveCriticalityTableColumns(self)
        return self._columns