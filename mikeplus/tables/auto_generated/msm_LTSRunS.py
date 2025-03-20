from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class msm_LTSRunSTableColumns(BaseColumns):
    """Column names for msm_LTSRunS (Run time stop criteria)."""
    MUID = "MUID"
    ApplyNo = "ApplyNo"
    ConditionNo = "ConditionNo"
    LocationNo = "LocationNo"
    LocationID = "LocationID"
    StopValue = "StopValue"
    StopTime = "StopTime"

class msm_LTSRunSTable(BaseTable):
    """Table for msm_LTSRunS (Run time stop criteria)."""
    
    @property
    def columns(self) -> msm_LTSRunSTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = msm_LTSRunSTableColumns(self)
        return self._columns