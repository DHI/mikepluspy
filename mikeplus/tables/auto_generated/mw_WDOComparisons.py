from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class mw_WDOComparisonsTableColumns(BaseColumns):
    """Column names for mw_WDOComparisons (Comparisons)."""
    MUID = "MUID"
    Enabled = "Enabled"
    ID = "ID"
    ModelType = "ModelType"
    ModelID = "ModelID"
    ModelMult = "ModelMult"
    ModelOffset = "ModelOffset"
    SensorID = "SensorID"
    SensorTable = "SensorTable"
    SensorMult = "SensorMult"
    SensorOffset = "SensorOffset"
    ComparisonTable = "ComparisonTable"
    AlarmLow = "AlarmLow"
    AlarmHigh = "AlarmHigh"
    AlarmLowLow = "AlarmLowLow"
    AlarmHighHigh = "AlarmHighHigh"
    AlarmMin = "AlarmMin"
    AlarmMax = "AlarmMax"
    Comment = "Comment"

class mw_WDOComparisonsTable(BaseTable):
    """Table for mw_WDOComparisons (Comparisons)."""
    
    @property
    def columns(self) -> mw_WDOComparisonsTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mw_WDOComparisonsTableColumns(self)
        return self._columns