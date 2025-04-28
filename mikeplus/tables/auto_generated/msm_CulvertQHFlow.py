from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class msm_CulvertQHFlowTableColumns(BaseColumns):
    """Column names for msm_CulvertQHFlow (Q/h relations)."""
    MUID = "MUID"
    CulvertID = "CulvertID"
    Sqn = "Sqn"
    y = "y"
    Qc = "Qc"
    TypeNo = "TypeNo"
    Direction = "Direction"

class msm_CulvertQHFlowTable(BaseTable):
    """Table for msm_CulvertQHFlow (Q/h relations)."""
    
    @property
    def columns(self) -> msm_CulvertQHFlowTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = msm_CulvertQHFlowTableColumns(self)
        return self._columns