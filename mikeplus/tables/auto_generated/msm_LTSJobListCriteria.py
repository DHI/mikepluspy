from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class msm_LTSJobListCriteriaTableColumns(BaseColumns):
    """Column names for msm_LTSJobListCriteria (Job list criteria)."""
    MUID = "MUID"
    ApplyNo = "ApplyNo"
    ConditionNo = "ConditionNo"
    LocationNo = "LocationNo"
    LocationID = "LocationID"
    StartValue = "StartValue"
    StartTime = "StartTime"
    StopValue = "StopValue"
    StopTime = "StopTime"

class msm_LTSJobListCriteriaTable(BaseTable):
    """Table for msm_LTSJobListCriteria (Job list criteria)."""
    
    @property
    def columns(self) -> msm_LTSJobListCriteriaTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = msm_LTSJobListCriteriaTableColumns(self)
        return self._columns