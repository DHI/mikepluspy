from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class mw_WDOAggSensorsDTableColumns(BaseColumns):
    """Column names for mw_WDOAggSensorsD (Aggregation sensors)."""
    MUID = "MUID"
    AggSensorID = "AggSensorID"
    SensorID = "SensorID"
    SensorTable = "SensorTable"
    SensorMode = "SensorMode"
    Mult = "Mult"
    OffsetValue = "OffsetValue"
    Enabled = "Enabled"
    Comment = "Comment"

class mw_WDOAggSensorsDTable(BaseTable):
    """Table for mw_WDOAggSensorsD (Aggregation sensors)."""
    
    @property
    def columns(self) -> mw_WDOAggSensorsDTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mw_WDOAggSensorsDTableColumns(self)
        return self._columns