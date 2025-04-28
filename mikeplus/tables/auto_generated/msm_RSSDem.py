from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class msm_RSSDemTableColumns(BaseColumns):
    """Column names for msm_RSSDem (RSSDem)."""
    MUID = "MUID"
    Sqn = "Sqn"
    FileName = "FileName"
    ItemID = "ItemID"
    ItemNo = "ItemNo"

class msm_RSSDemTable(BaseTable):
    """Table for msm_RSSDem (RSSDem)."""
    
    @property
    def columns(self) -> msm_RSSDemTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = msm_RSSDemTableColumns(self)
        return self._columns