from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class mss_BuildupTableColumns(BaseColumns):
    """Column names for mss_Buildup (Buildup)."""
    MUID = "MUID"
    LanduseID = "LanduseID"
    PollutantID = "PollutantID"
    FuncTypeNo = "FuncTypeNo"
    NormalizerNo = "NormalizerNo"
    C1 = "C1"
    C2 = "C2"
    C3 = "C3"
    ExternalTimeSeriesID = "ExternalTimeSeriesID"
    C2_ScalingFactor = "C2_ScalingFactor"

class mss_BuildupTable(BaseTable):
    """Table for mss_Buildup (Buildup)."""
    
    @property
    def columns(self) -> mss_BuildupTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mss_BuildupTableColumns(self)
        return self._columns