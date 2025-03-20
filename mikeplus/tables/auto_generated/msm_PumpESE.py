from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class msm_PumpESETableColumns(BaseColumns):
    """Column names for msm_PumpESE (Emergency storage estimation)."""
    MUID = "MUID"
    Description = "Description"
    SimulationID = "SimulationID"
    RunModeNo = "RunModeNo"
    StopTime = "StopTime"
    CheckWetWellNo = "CheckWetWellNo"
    UsPumpStopNo = "UsPumpStopNo"
    UsPumpStopDelay = "UsPumpStopDelay"
    AlarmSetID = "AlarmSetID"

class msm_PumpESETable(BaseTable):
    """Table for msm_PumpESE (Emergency storage estimation)."""
    
    @property
    def columns(self) -> msm_PumpESETableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = msm_PumpESETableColumns(self)
        return self._columns