from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class msm_STInitDepthFractDefaultTableColumns(BaseColumns):
    """Column names for msm_STInitDepthFractDefault (msm_STInitDepthFractDefault)."""
    MUID = "MUID"
    TypeNo = "TypeNo"
    FractionID = "FractionID"
    FracPercentActive = "FracPercentActive"
    FracPercentPassive = "FracPercentPassive"

class msm_STInitDepthFractDefaultTable(BaseTable):
    """Table for msm_STInitDepthFractDefault (msm_STInitDepthFractDefault)."""
    
    @property
    def columns(self) -> msm_STInitDepthFractDefaultTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = msm_STInitDepthFractDefaultTableColumns(self)
        return self._columns