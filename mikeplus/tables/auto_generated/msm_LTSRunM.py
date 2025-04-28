from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class msm_LTSRunMTableColumns(BaseColumns):
    """Column names for msm_LTSRunM (Run time stop criteria matrix)."""
    MUID = "MUID"
    Condition1 = "Condition1"
    Condition2 = "Condition2"
    Condition3 = "Condition3"
    Condition4 = "Condition4"
    Condition5 = "Condition5"

class msm_LTSRunMTable(BaseTable):
    """Table for msm_LTSRunM (Run time stop criteria matrix)."""
    
    @property
    def columns(self) -> msm_LTSRunMTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = msm_LTSRunMTableColumns(self)
        return self._columns