from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class msm_AlarmLevelTableColumns(BaseColumns):
    """Column names for msm_AlarmLevel (Alarm levels)."""
    MUID = "MUID"
    Description = "Description"
    DefaultFreeBoard = "DefaultFreeBoard"

class msm_AlarmLevelTable(BaseTable):
    """Table for msm_AlarmLevel (Alarm levels)."""
    
    @property
    def columns(self) -> msm_AlarmLevelTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = msm_AlarmLevelTableColumns(self)
        return self._columns