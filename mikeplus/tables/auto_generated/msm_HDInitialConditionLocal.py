from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class msm_HDInitialConditionLocalTableColumns(BaseColumns):
    """Column names for msm_HDInitialConditionLocal (Local values)."""
    MUID = "MUID"
    InitCondID = "InitCondID"
    Sqn = "Sqn"
    Description = "Description"
    LocationTypeNo = "LocationTypeNo"
    ListID = "ListID"
    NodeID = "NodeID"
    LinkID = "LinkID"
    LinkNo = "LinkNo"
    StartChainage = "StartChainage"
    EndChainage = "EndChainage"
    LevelDepthTypeNo = "LevelDepthTypeNo"
    LevelDepth = "LevelDepth"
    DischargeTypeNo = "DischargeTypeNo"
    Discharge = "Discharge"

class msm_HDInitialConditionLocalTable(BaseTable):
    """Table for msm_HDInitialConditionLocal (Local values)."""
    
    @property
    def columns(self) -> msm_HDInitialConditionLocalTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = msm_HDInitialConditionLocalTableColumns(self)
        return self._columns