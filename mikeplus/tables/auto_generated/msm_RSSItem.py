from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class msm_RSSItemTableColumns(BaseColumns):
    """Column names for msm_RSSItem (RSSItem)."""
    MUID = "MUID"
    SelectionID = "SelectionID"
    GroupNo = "GroupNo"
    ItemNo = "ItemNo"
    ItemText = "ItemText"
    ItemParam = "ItemParam"

class msm_RSSItemTable(BaseTable):
    """Table for msm_RSSItem (RSSItem)."""
    
    @property
    def columns(self) -> msm_RSSItemTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = msm_RSSItemTableColumns(self)
        return self._columns