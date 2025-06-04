from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class mw_WDOSensorsTableColumns(BaseColumns):
    """Column names for mw_WDOSensors (Sensors)."""
    MUID = "MUID"
    """MUID"""
    SensorId = "SensorId"
    """ID"""
    ID = "ID"
    """ID"""
    Enabled = "Enabled"
    """Is active"""
    SensorTable = "SensorTable"
    """Sensor table"""
    ModelType = "ModelType"
    """Model type"""
    ModelID = "ModelID"
    """Model ID"""
    Mult = "Mult"
    """Multiplier [()]"""
    OffsetValue = "OffsetValue"
    """Offset"""
    Comment = "Comment"
    """Description"""

class mw_WDOSensorsTable(BaseTable):
    """Table for mw_WDOSensors (Sensors)."""
    
    @property
    def columns(self) -> mw_WDOSensorsTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mw_WDOSensorsTableColumns(self)
        return self._columns