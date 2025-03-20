from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class mw_WDODemandPredictionsTableColumns(BaseColumns):
    """Column names for mw_WDODemandPredictions (Demand predictions)."""
    MUID = "MUID"
    ID = "ID"
    Enabled = "Enabled"
    SensorID = "SensorID"
    SensorTable = "SensorTable"
    PredictTable = "PredictTable"
    PredictStep = "PredictStep"
    PredictDuration = "PredictDuration"
    PredictType = "PredictType"
    HistoryDuration = "HistoryDuration"
    Runs = "Runs"
    Comment = "Comment"
    Param1 = "Param1"
    Param2 = "Param2"
    Param3 = "Param3"
    Param4 = "Param4"
    Param5 = "Param5"
    Param6 = "Param6"
    Param7 = "Param7"
    Param8 = "Param8"
    SensorMult = "SensorMult"
    SensorOffset = "SensorOffset"
    ZoneID = "ZoneID"

class mw_WDODemandPredictionsTable(BaseTable):
    """Table for mw_WDODemandPredictions (Demand predictions)."""
    
    @property
    def columns(self) -> mw_WDODemandPredictionsTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mw_WDODemandPredictionsTableColumns(self)
        return self._columns