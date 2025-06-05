from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class mw_TraceNodeTableColumns(BaseColumns):
    """Column names for mw_TraceNode (Trace nodes)."""
    MUID = "MUID"
    """ID"""
    NodeTypeNo = "NodeTypeNo"
    """Node type"""
    NodeID = "NodeID"
    """Node ID"""
    Description = "Description"
    """Description"""
    Enabled = "Enabled"
    """Is active"""

class mw_TraceNodeTable(BaseTable):
    """Table for mw_TraceNode (Trace nodes)."""
    
    @property
    def columns(self) -> mw_TraceNodeTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mw_TraceNodeTableColumns(self)
        return self._columns