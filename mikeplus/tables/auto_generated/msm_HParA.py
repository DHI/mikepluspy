from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class msm_HParATableColumns(BaseColumns):
    """Column names for msm_HParA (Parameters time-area)."""
    MUID = "MUID"
    """ID"""
    RedFactor = "RedFactor"
    """Reduction factor [()]"""
    InitLoss = "InitLoss"
    """Initial loss [mm]"""
    ConcTime = "ConcTime"
    """Time of concentration [min]"""
    TAMethodNo = "TAMethodNo"
    """TA Method"""
    TACurveID = "TACurveID"
    """TA CurveID"""
    TACoeff = "TACoeff"
    """TA Coeff."""

class msm_HParATable(BaseTable):
    """Table for msm_HParA (Parameters time-area)."""
    
    @property
    def columns(self) -> msm_HParATableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = msm_HParATableColumns(self)
        return self._columns