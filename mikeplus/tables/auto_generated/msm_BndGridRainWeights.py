from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class msm_BndGridRainWeightsTableColumns(BaseColumns):
    """Column names for msm_BndGridRainWeights (msm_BndGridRainWeights)."""
    MUID = "MUID"
    BoundaryID = "BoundaryID"
    CatchmentID = "CatchmentID"
    I = "I"
    J = "J"
    Weight = "Weight"

class msm_BndGridRainWeightsTable(BaseTable):
    """Table for msm_BndGridRainWeights (msm_BndGridRainWeights)."""
    
    @property
    def columns(self) -> msm_BndGridRainWeightsTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = msm_BndGridRainWeightsTableColumns(self)
        return self._columns