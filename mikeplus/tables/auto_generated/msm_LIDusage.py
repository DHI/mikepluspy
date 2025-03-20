from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class msm_LIDusageTableColumns(BaseColumns):
    """Column names for msm_LIDusage (LID deployment)."""
    MUID = "MUID"
    CatchmentID = "CatchmentID"
    LidID = "LidID"
    IncludeNo = "IncludeNo"
    ReplicateNumber = "ReplicateNumber"
    CollectingNo = "CollectingNo"
    CollectingArea = "CollectingArea"
    CollectingAreaPercent = "CollectingAreaPercent"
    UnitArea = "UnitArea"
    UnitAreaPercent = "UnitAreaPercent"
    Width = "Width"
    InitSatSurface = "InitSatSurface"
    InitSatSoil = "InitSatSoil"
    InitSatStorage = "InitSatStorage"

class msm_LIDusageTable(BaseTable):
    """Table for msm_LIDusage (LID deployment)."""
    
    @property
    def columns(self) -> msm_LIDusageTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = msm_LIDusageTableColumns(self)
        return self._columns