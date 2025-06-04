from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class mwRes_Sustainability_NodeTableColumns(BaseColumns):
    """Column names for mwRes_Sustainability_Node (mwRes_Sustainability_Node)."""
    MUID = "MUID"
    """ID"""
    PressureAnomalies = "PressureAnomalies"
    """Pressure anomalies [m]"""
    PressureDistribution = "PressureDistribution"
    """Pressure distribution [m]"""
    PressureFluctuation = "PressureFluctuation"
    """Pressure fluctuation [m]"""

class mwRes_Sustainability_NodeTable(BaseTable):
    """Table for mwRes_Sustainability_Node (mwRes_Sustainability_Node)."""
    
    @property
    def columns(self) -> mwRes_Sustainability_NodeTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mwRes_Sustainability_NodeTableColumns(self)
        return self._columns