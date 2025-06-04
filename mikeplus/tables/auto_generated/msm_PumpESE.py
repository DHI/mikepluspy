from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class msm_PumpESETableColumns(BaseColumns):
    """Column names for msm_PumpESE (Emergency storage estimation)."""
    MUID = "MUID"
    """ID"""
    Description = "Description"
    """Description"""
    SimulationID = "SimulationID"
    """Simulation ID"""
    RunModeNo = "RunModeNo"
    """Run mode"""
    StopTime = "StopTime"
    """Pump stop time"""
    CheckWetWellNo = "CheckWetWellNo"
    """Check wet well alarm level only"""
    UsPumpStopNo = "UsPumpStopNo"
    """Upstream pumps stop"""
    UsPumpStopDelay = "UsPumpStopDelay"
    """Delay [min]"""
    AlarmSetID = "AlarmSetID"
    """Alarm set ID"""

class msm_PumpESETable(BaseTable):
    """Table for msm_PumpESE (Emergency storage estimation)."""
    
    @property
    def columns(self) -> msm_PumpESETableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = msm_PumpESETableColumns(self)
        return self._columns