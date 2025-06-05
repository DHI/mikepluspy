from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class mw_WDOControlsTableColumns(BaseColumns):
    """Column names for mw_WDOControls (Controls)."""
    MUID = "MUID"
    """ID"""
    ID = "ID"
    """ID"""
    ControlType = "ControlType"
    """Control type"""
    Enabled = "Enabled"
    """Is active"""
    SensorID = "SensorID"
    """Sensor ID"""
    SensorTable = "SensorTable"
    """Sensor table"""
    ModelID = "ModelID"
    """Model ID"""
    Override = "Override"
    """Override faulty data"""
    Priority = "Priority"
    """Priority"""
    Mult = "Mult"
    """Multiplier [()]"""
    OffsetValue = "OffsetValue"
    """Offset [()]"""
    Comment = "Comment"
    """Description"""

class mw_WDOControlsTable(BaseTable):
    """Table for mw_WDOControls (Controls)."""
    
    @property
    def columns(self) -> mw_WDOControlsTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mw_WDOControlsTableColumns(self)
        return self._columns