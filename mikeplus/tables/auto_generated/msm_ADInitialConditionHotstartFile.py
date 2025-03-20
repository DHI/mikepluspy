from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class msm_ADInitialConditionHotstartFileTableColumns(BaseColumns):
    """Column names for msm_ADInitialConditionHotstartFile (Hotstart files)."""
    MUID = "MUID"
    InitCondID = "InitCondID"
    Sqn = "Sqn"
    FilePath = "FilePath"
    UseStartTimeNo = "UseStartTimeNo"
    DateTime = "DateTime"

class msm_ADInitialConditionHotstartFileTable(BaseTable):
    """Table for msm_ADInitialConditionHotstartFile (Hotstart files)."""
    
    @property
    def columns(self) -> msm_ADInitialConditionHotstartFileTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = msm_ADInitialConditionHotstartFileTableColumns(self)
        return self._columns