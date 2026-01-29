from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class mw_WDOAggSensorsDTableColumns(BaseColumns):
    """Column names for mw_WDOAggSensorsD (Aggregation sensors)."""
    MUID = "MUID"
    """ID"""
    AggSensorID = "AggSensorID"
    """AggSensorID"""
    SensorID = "SensorID"
    """Sensor ID"""
    SensorTable = "SensorTable"
    """Sensor table"""
    SensorMode = "SensorMode"
    """Sensor mode"""
    Mult = "Mult"
    """Multiplier [()]"""
    OffsetValue = "OffsetValue"
    """Offset [()]"""
    Enabled = "Enabled"
    """Is active"""
    Comment = "Comment"
    """Description"""

class mw_WDOAggSensorsDTable(BaseTable):
    """Table for mw_WDOAggSensorsD (Aggregation sensors)."""
    
    @property
    def columns(self) -> mw_WDOAggSensorsDTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mw_WDOAggSensorsDTableColumns(self)
        return self._columns