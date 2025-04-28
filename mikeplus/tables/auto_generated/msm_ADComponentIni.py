from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class msm_ADComponentIniTableColumns(BaseColumns):
    """Column names for msm_ADComponentIni (msm_ADComponentIni)."""
    MUID = "MUID"
    ComponentID = "ComponentID"
    ConnectionTypeNo = "ConnectionTypeNo"
    NodeListFile = "NodeListFile"
    NodeID = "NodeID"
    InitCondLocalValue = "InitCondLocalValue"

class msm_ADComponentIniTable(BaseTable):
    """Table for msm_ADComponentIni (msm_ADComponentIni)."""
    
    @property
    def columns(self) -> msm_ADComponentIniTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = msm_ADComponentIniTableColumns(self)
        return self._columns