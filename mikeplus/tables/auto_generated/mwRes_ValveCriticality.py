from mikeplus.tables.base_geometry_table import BaseGeometryTable
from mikeplus.tables.base_geometry_table import BaseColumns

class mwRes_ValveCriticalityTableColumns(BaseColumns):
    """Column names for mwRes_ValveCriticality (Valve criticality)."""
    MUID = "MUID"
    ValveID = "ValveID"
    NoClosedValve = "NoClosedValve"
    ListClosedPipe = "ListClosedPipe"
    ListClosedValve = "ListClosedValve"
    sumlength = "sumlength"

class mwRes_ValveCriticalityTable(BaseGeometryTable):
    """Table for mwRes_ValveCriticality (Valve criticality)."""
    
    @property
    def columns(self) -> mwRes_ValveCriticalityTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mwRes_ValveCriticalityTableColumns(self)
        return self._columns