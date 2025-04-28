from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class msm_STInitDepthLocalTableColumns(BaseColumns):
    """Column names for msm_STInitDepthLocal (ST initial depths)."""
    MUID = "MUID"
    ConnectionTypeNo = "ConnectionTypeNo"
    LinkID = "LinkID"
    ListName = "ListName"
    Chainage = "Chainage"
    LocSediDepth = "LocSediDepth"
    LocPassiveDepth = "LocPassiveDepth"
    LinkNo = "LinkNo"

class msm_STInitDepthLocalTable(BaseTable):
    """Table for msm_STInitDepthLocal (ST initial depths)."""
    
    @property
    def columns(self) -> msm_STInitDepthLocalTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = msm_STInitDepthLocalTableColumns(self)
        return self._columns