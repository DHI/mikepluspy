from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class msm_LTSInitTableColumns(BaseColumns):
    """Column names for msm_LTSInit (LTS initial conditions)."""
    MUID = "MUID"
    HotStartFilename = "HotStartFilename"
    InitDate = "InitDate"
    InitFrom = "InitFrom"
    InitTo = "InitTo"

class msm_LTSInitTable(BaseTable):
    """Table for msm_LTSInit (LTS initial conditions)."""
    
    @property
    def columns(self) -> msm_LTSInitTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = msm_LTSInitTableColumns(self)
        return self._columns