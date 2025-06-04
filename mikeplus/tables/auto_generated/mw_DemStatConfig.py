from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class mw_DemStatConfigTableColumns(BaseColumns):
    """Column names for mw_DemStatConfig (Statistics and redistribution)."""
    MUID = "MUID"
    """MUID"""
    MethodNo = "MethodNo"
    """ Demand method"""
    NetElemTypeNo = "NetElemTypeNo"
    """Zone ID"""
    ZoneTypeNo = "ZoneTypeNo"
    """Zone type"""
    SimulationID = "SimulationID"
    """Active simulation ID"""
    ScenarioID = "ScenarioID"
    """Scenario ID"""
    SimulationType = "SimulationType"
    """Simulation type"""
    StartTime = "StartTime"
    """Start time"""
    EndTime = "EndTime"
    """End time"""

class mw_DemStatConfigTable(BaseTable):
    """Table for mw_DemStatConfig (Statistics and redistribution)."""
    
    @property
    def columns(self) -> mw_DemStatConfigTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mw_DemStatConfigTableColumns(self)
        return self._columns