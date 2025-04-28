from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class msm_AlarmLevelDTableColumns(BaseColumns):
    """Column names for msm_AlarmLevelD (Levels in alarm set)."""
    MUID = "MUID"
    AlarmLevelID = "AlarmLevelID"
    NodeID = "NodeID"
    AlarmLevel = "AlarmLevel"
    AllowUpdate = "AllowUpdate"

class msm_AlarmLevelDTable(BaseTable):
    """Table for msm_AlarmLevelD (Levels in alarm set)."""
    
    @property
    def columns(self) -> msm_AlarmLevelDTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = msm_AlarmLevelDTableColumns(self)
        return self._columns