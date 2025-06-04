from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class msm_LTSJobListCriteriaTableColumns(BaseColumns):
    """Column names for msm_LTSJobListCriteria (Job list criteria)."""
    MUID = "MUID"
    """ID"""
    ApplyNo = "ApplyNo"
    """Apply"""
    ConditionNo = "ConditionNo"
    """Type"""
    LocationNo = "LocationNo"
    """Location type"""
    LocationID = "LocationID"
    """Location"""
    StartValue = "StartValue"
    """Start threshold [m^3/s]"""
    StartTime = "StartTime"
    """Start duration [min]"""
    StopValue = "StopValue"
    """Stop threshold [m^3/s]"""
    StopTime = "StopTime"
    """Stop duration [min]"""

class msm_LTSJobListCriteriaTable(BaseTable):
    """Table for msm_LTSJobListCriteria (Job list criteria)."""
    
    @property
    def columns(self) -> msm_LTSJobListCriteriaTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = msm_LTSJobListCriteriaTableColumns(self)
        return self._columns