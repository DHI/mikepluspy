from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class mrm_BridgeCrsTableColumns(BaseColumns):
    """Column names for mrm_BridgeCrs (mrm_BridgeCrs)."""
    MUID = "MUID"
    Type = "Type"
    Sqn = "Sqn"
    BridgeOpeningID = "BridgeOpeningID"
    S = "S"
    Z = "Z"
    Rough = "Rough"
    MarkerNo = "MarkerNo"

class mrm_BridgeCrsTable(BaseTable):
    """Table for mrm_BridgeCrs (mrm_BridgeCrs)."""
    
    @property
    def columns(self) -> mrm_BridgeCrsTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mrm_BridgeCrsTableColumns(self)
        return self._columns