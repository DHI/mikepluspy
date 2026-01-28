from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class mw_ZoneWBTableColumns(BaseColumns):
    """Column names for mw_ZoneWB (mw_ZoneWB)."""
    MUID = "MUID"
    """ID"""
    ZoneID = "ZoneID"
    """ZoneID"""
    MeasurementID = "MeasurementID"
    """Plot ID"""
    Unit = "Unit"
    """Unit"""
    FlowDerictionNo = "FlowDerictionNo"
    """Positive flow"""
    Volume = "Volume"
    """Volume [m^3]"""

class mw_ZoneWBTable(BaseTable):
    """Table for mw_ZoneWB (mw_ZoneWB)."""
    
    @property
    def columns(self) -> mw_ZoneWBTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mw_ZoneWBTableColumns(self)
        return self._columns