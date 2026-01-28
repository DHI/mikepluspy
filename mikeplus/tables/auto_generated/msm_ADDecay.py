from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class msm_ADDecayTableColumns(BaseColumns):
    """Column names for msm_ADDecay (Decay)."""
    MUID = "MUID"
    """ID"""
    LocTypeNo = "LocTypeNo"
    """Type"""
    ListID = "ListID"
    """List ID"""
    LinkID = "LinkID"
    """Link ID"""
    StartChainage = "StartChainage"
    """Start chainage [m]"""
    EndChainage = "EndChainage"
    """End chainage [m]"""
    LocalWQCompID = "LocalWQCompID"
    """WQ component"""
    LocalDecay = "LocalDecay"
    """Decay [/h]"""

class msm_ADDecayTable(BaseTable):
    """Table for msm_ADDecay (Decay)."""
    
    @property
    def columns(self) -> msm_ADDecayTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = msm_ADDecayTableColumns(self)
        return self._columns