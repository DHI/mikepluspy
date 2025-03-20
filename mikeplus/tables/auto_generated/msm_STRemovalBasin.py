from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class msm_STRemovalBasinTableColumns(BaseColumns):
    """Column names for msm_STRemovalBasin (Sediment removal in basins)."""
    MUID = "MUID"
    NodeID = "NodeID"
    RemovalCoef = "RemovalCoef"

class msm_STRemovalBasinTable(BaseTable):
    """Table for msm_STRemovalBasin (Sediment removal in basins)."""
    
    @property
    def columns(self) -> msm_STRemovalBasinTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = msm_STRemovalBasinTableColumns(self)
        return self._columns