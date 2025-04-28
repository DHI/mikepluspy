from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class msm_HDInitialConditionHotstartFileTableColumns(BaseColumns):
    """Column names for msm_HDInitialConditionHotstartFile (Hotstart files)."""
    MUID = "MUID"
    InitCondID = "InitCondID"
    Sqn = "Sqn"
    FilePath = "FilePath"
    UseStartTimeNo = "UseStartTimeNo"
    DateTime = "DateTime"

class msm_HDInitialConditionHotstartFileTable(BaseTable):
    """Table for msm_HDInitialConditionHotstartFile (Hotstart files)."""
    
    @property
    def columns(self) -> msm_HDInitialConditionHotstartFileTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = msm_HDInitialConditionHotstartFileTableColumns(self)
        return self._columns