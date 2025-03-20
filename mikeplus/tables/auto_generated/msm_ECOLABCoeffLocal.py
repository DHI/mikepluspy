from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class msm_ECOLABCoeffLocalTableColumns(BaseColumns):
    """Column names for msm_ECOLABCoeffLocal (MIKE ECO LAB constants local values)."""
    MUID = "MUID"
    CoefID = "CoefID"
    LocTypeNo = "LocTypeNo"
    ListID = "ListID"
    NodeID = "NodeID"
    LinkID = "LinkID"
    StartChainage = "StartChainage"
    EndChainage = "EndChainage"
    LinkNo = "LinkNo"
    Value = "Value"

class msm_ECOLABCoeffLocalTable(BaseTable):
    """Table for msm_ECOLABCoeffLocal (MIKE ECO LAB constants local values)."""
    
    @property
    def columns(self) -> msm_ECOLABCoeffLocalTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = msm_ECOLABCoeffLocalTableColumns(self)
        return self._columns