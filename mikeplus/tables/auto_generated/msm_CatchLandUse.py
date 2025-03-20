from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class msm_CatchLandUseTableColumns(BaseColumns):
    """Column names for msm_CatchLandUse (msm_CatchLandUse)."""
    MUID = "MUID"
    CatchmentID = "CatchmentID"
    LandUseID = "LandUseID"
    LandUseIDType = "LandUseIDType"
    ModelType = "ModelType"
    LandUseContrib = "LandUseContrib"

class msm_CatchLandUseTable(BaseTable):
    """Table for msm_CatchLandUse (msm_CatchLandUse)."""
    
    @property
    def columns(self) -> msm_CatchLandUseTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = msm_CatchLandUseTableColumns(self)
        return self._columns