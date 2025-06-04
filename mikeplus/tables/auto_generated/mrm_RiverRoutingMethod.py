from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class mrm_RiverRoutingMethodTableColumns(BaseColumns):
    """Column names for mrm_RiverRoutingMethod (Simple routing locations)."""
    BranchID = "BranchID"
    """BranchID"""
    MUID = "MUID"
    """ID"""
    Chainage = "Chainage"
    """Chainage [m]"""
    FlowMethodNo = "FlowMethodNo"
    """Method"""
    FlowDelay = "FlowDelay"
    """Delay parameter [min]"""
    FlowShape = "FlowShape"
    """Shape parameter [()]"""
    WLMethodNo = "WLMethodNo"
    """Method"""
    QhRelationID = "QhRelationID"
    """Q/h relation"""

class mrm_RiverRoutingMethodTable(BaseTable):
    """Table for mrm_RiverRoutingMethod (Simple routing locations)."""
    
    @property
    def columns(self) -> mrm_RiverRoutingMethodTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mrm_RiverRoutingMethodTableColumns(self)
        return self._columns