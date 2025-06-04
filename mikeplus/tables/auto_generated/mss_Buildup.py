from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class mss_BuildupTableColumns(BaseColumns):
    """Column names for mss_Buildup (Buildup)."""
    MUID = "MUID"
    """MUID"""
    LanduseID = "LanduseID"
    """LanduseID"""
    PollutantID = "PollutantID"
    """Pollutant ID"""
    FuncTypeNo = "FuncTypeNo"
    """Function type"""
    NormalizerNo = "NormalizerNo"
    """Normalizer"""
    C1 = "C1"
    """Maximum buildup"""
    C2 = "C2"
    """Rate"""
    C3 = "C3"
    """Time exponent"""
    ExternalTimeSeriesID = "ExternalTimeSeriesID"
    """Time series"""
    C2_ScalingFactor = "C2_ScalingFactor"
    """Scaling factor [()]"""

class mss_BuildupTable(BaseTable):
    """Table for mss_Buildup (Buildup)."""
    
    @property
    def columns(self) -> mss_BuildupTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mss_BuildupTableColumns(self)
        return self._columns