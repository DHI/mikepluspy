from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class mrm_BridgeCrsTableColumns(BaseColumns):
    """Column names for mrm_BridgeCrs (mrm_BridgeCrs)."""
    MUID = "MUID"
    """MUID"""
    Type = "Type"
    """Type"""
    Sqn = "Sqn"
    """Sqn"""
    BridgeOpeningID = "BridgeOpeningID"
    """River bridge opening ID"""
    S = "S"
    """S [m]"""
    Z = "Z"
    """Z [m]"""
    Rough = "Rough"
    """Roughness"""
    MarkerNo = "MarkerNo"
    """Marker"""

class mrm_BridgeCrsTable(BaseTable):
    """Table for mrm_BridgeCrs (mrm_BridgeCrs)."""
    
    @property
    def columns(self) -> mrm_BridgeCrsTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mrm_BridgeCrsTableColumns(self)
        return self._columns