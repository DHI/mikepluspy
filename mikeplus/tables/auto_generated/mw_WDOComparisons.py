from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class mw_WDOComparisonsTableColumns(BaseColumns):
    """Column names for mw_WDOComparisons (Comparisons)."""
    MUID = "MUID"
    """ID"""
    Enabled = "Enabled"
    """Is active"""
    ID = "ID"
    """ID"""
    ModelType = "ModelType"
    """Model type"""
    ModelID = "ModelID"
    """Model ID"""
    ModelMult = "ModelMult"
    """Model multiplier [()]"""
    ModelOffset = "ModelOffset"
    """Model offset"""
    SensorID = "SensorID"
    """Sensor ID"""
    SensorTable = "SensorTable"
    """Sensor table"""
    SensorMult = "SensorMult"
    """Sensor multiplier [()]"""
    SensorOffset = "SensorOffset"
    """Sensor offset [()]"""
    ComparisonTable = "ComparisonTable"
    """Comparison table"""
    AlarmLow = "AlarmLow"
    """Low alarm"""
    AlarmHigh = "AlarmHigh"
    """High alarm"""
    AlarmLowLow = "AlarmLowLow"
    """Alarm low low"""
    AlarmHighHigh = "AlarmHighHigh"
    """Alarm high high"""
    AlarmMin = "AlarmMin"
    """Min alarm"""
    AlarmMax = "AlarmMax"
    """Max alarm"""
    Comment = "Comment"
    """Description"""

class mw_WDOComparisonsTable(BaseTable):
    """Table for mw_WDOComparisons (Comparisons)."""
    
    @property
    def columns(self) -> mw_WDOComparisonsTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mw_WDOComparisonsTableColumns(self)
        return self._columns