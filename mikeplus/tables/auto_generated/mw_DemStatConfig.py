from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class mw_DemStatConfigTableColumns(BaseColumns):
    """Column names for mw_DemStatConfig (Statistics and redistribution)."""
    MUID = "MUID"
    MethodNo = "MethodNo"
    NetElemTypeNo = "NetElemTypeNo"
    ZoneTypeNo = "ZoneTypeNo"
    SimulationID = "SimulationID"
    ScenarioID = "ScenarioID"
    SimulationType = "SimulationType"
    StartTime = "StartTime"
    EndTime = "EndTime"

class mw_DemStatConfigTable(BaseTable):
    """Table for mw_DemStatConfig (Statistics and redistribution)."""
    
    @property
    def columns(self) -> mw_DemStatConfigTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mw_DemStatConfigTableColumns(self)
        return self._columns