from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class msm_HParATableColumns(BaseColumns):
    """Column names for msm_HParA (Parameters time-area)."""
    MUID = "MUID"
    RedFactor = "RedFactor"
    InitLoss = "InitLoss"
    ConcTime = "ConcTime"
    TAMethodNo = "TAMethodNo"
    TACurveID = "TACurveID"
    TACoeff = "TACoeff"

class msm_HParATable(BaseTable):
    """Table for msm_HParA (Parameters time-area)."""
    
    @property
    def columns(self) -> msm_HParATableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = msm_HParATableColumns(self)
        return self._columns