from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class msm_LIDusageTableColumns(BaseColumns):
    """Column names for msm_LIDusage (LID deployment)."""
    MUID = "MUID"
    """ID"""
    CatchmentID = "CatchmentID"
    """Catchment ID"""
    LidID = "LidID"
    """LID ID"""
    IncludeNo = "IncludeNo"
    """Apply"""
    ReplicateNumber = "ReplicateNumber"
    """Number of units"""
    CollectingNo = "CollectingNo"
    """Collecting type"""
    CollectingArea = "CollectingArea"
    """Collecting area [m^2]"""
    CollectingAreaPercent = "CollectingAreaPercent"
    """% Collecting area [%]"""
    UnitArea = "UnitArea"
    """Unit area [m^2]"""
    UnitAreaPercent = "UnitAreaPercent"
    """% Unit area [%]"""
    Width = "Width"
    """Width [m]"""
    InitSatSurface = "InitSatSurface"
    """Surface [%]"""
    InitSatSoil = "InitSatSoil"
    """Soil/pavement [%]"""
    InitSatStorage = "InitSatStorage"
    """Storage [%]"""

class msm_LIDusageTable(BaseTable):
    """Table for msm_LIDusage (LID deployment)."""
    
    @property
    def columns(self) -> msm_LIDusageTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = msm_LIDusageTableColumns(self)
        return self._columns