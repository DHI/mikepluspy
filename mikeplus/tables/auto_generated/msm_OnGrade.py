from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class msm_OnGradeTableColumns(BaseColumns):
    """Column names for msm_OnGrade (OnGrade captures)."""
    MUID = "MUID"
    """ID"""

class msm_OnGradeTable(BaseTable):
    """Table for msm_OnGrade (OnGrade captures)."""
    
    @property
    def columns(self) -> msm_OnGradeTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = msm_OnGradeTableColumns(self)
        return self._columns