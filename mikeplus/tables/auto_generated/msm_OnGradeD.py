from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class msm_OnGradeDTableColumns(BaseColumns):
    """Column names for msm_OnGradeD (OnGrade capture data)."""
    MUID = "MUID"
    CaptureID = "CaptureID"
    Sqn = "Sqn"
    QQRelationID = "QQRelationID"
    Slope = "Slope"

class msm_OnGradeDTable(BaseTable):
    """Table for msm_OnGradeD (OnGrade capture data)."""
    
    @property
    def columns(self) -> msm_OnGradeDTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = msm_OnGradeDTableColumns(self)
        return self._columns