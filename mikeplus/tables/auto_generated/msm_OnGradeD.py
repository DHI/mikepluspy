from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class msm_OnGradeDTableColumns(BaseColumns):
    """Column names for msm_OnGradeD (OnGrade capture data)."""
    MUID = "MUID"
    """MUID"""
    CaptureID = "CaptureID"
    """CaptureID"""
    Sqn = "Sqn"
    """Sqn"""
    QQRelationID = "QQRelationID"
    """QQ relation"""
    Slope = "Slope"
    """Slope [%]"""

class msm_OnGradeDTable(BaseTable):
    """Table for msm_OnGradeD (OnGrade capture data)."""
    
    @property
    def columns(self) -> msm_OnGradeDTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = msm_OnGradeDTableColumns(self)
        return self._columns