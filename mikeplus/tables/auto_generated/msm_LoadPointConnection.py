from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class msm_LoadPointConnectionTableColumns(BaseColumns):
    """Column names for msm_LoadPointConnection (Load point connections)."""
    MUID = "MUID"
    LoadPointID = "LoadPointID"
    LocationID = "LocationID"
    LocationTypeNo = "LocationTypeNo"

class msm_LoadPointConnectionTable(BaseTable):
    """Table for msm_LoadPointConnection (Load point connections)."""
    
    @property
    def columns(self) -> msm_LoadPointConnectionTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = msm_LoadPointConnectionTableColumns(self)
        return self._columns