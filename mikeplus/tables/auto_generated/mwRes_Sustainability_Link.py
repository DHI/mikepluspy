from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class mwRes_Sustainability_LinkTableColumns(BaseColumns):
    """Column names for mwRes_Sustainability_Link (mwRes_Sustainability_Link)."""
    MUID = "MUID"
    """ID"""
    LinkHeadloss = "LinkHeadloss"
    """Link head loss [m]"""
    ReverseFlow = "ReverseFlow"
    """Reverse flow"""
    FlowVelocity = "FlowVelocity"
    """Flow velocity [m/s]"""
    FlowVelocityFluctuation = "FlowVelocityFluctuation"
    """Flow velocity fluctuation [m/s]"""

class mwRes_Sustainability_LinkTable(BaseTable):
    """Table for mwRes_Sustainability_Link (mwRes_Sustainability_Link)."""
    
    @property
    def columns(self) -> mwRes_Sustainability_LinkTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mwRes_Sustainability_LinkTableColumns(self)
        return self._columns