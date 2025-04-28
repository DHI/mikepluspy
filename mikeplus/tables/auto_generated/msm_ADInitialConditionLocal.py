from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class msm_ADInitialConditionLocalTableColumns(BaseColumns):
    """Column names for msm_ADInitialConditionLocal (Local values)."""
    MUID = "MUID"
    ADInitCondID = "ADInitCondID"
    Sqn = "Sqn"
    Description = "Description"
    LocationTypeNo = "LocationTypeNo"
    ListID = "ListID"
    NodeID = "NodeID"
    LinkID = "LinkID"
    LinkNo = "LinkNo"
    StartChainage = "StartChainage"
    EndChainage = "EndChainage"

class msm_ADInitialConditionLocalTable(BaseTable):
    """Table for msm_ADInitialConditionLocal (Local values)."""
    
    @property
    def columns(self) -> msm_ADInitialConditionLocalTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = msm_ADInitialConditionLocalTableColumns(self)
        return self._columns