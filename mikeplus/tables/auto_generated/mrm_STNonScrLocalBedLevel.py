from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class mrm_STNonScrLocalBedLevelTableColumns(BaseColumns):
    """Column names for mrm_STNonScrLocalBedLevel (Non-scouring bed level)."""
    MUID = "MUID"
    """MUID"""
    LinkID = "LinkID"
    """Link ID"""
    Chainage = "Chainage"
    """Chainage [m]"""
    LocUnlimitedNo = "LocUnlimitedNo"
    """Unlimited"""
    LocLevel = "LocLevel"
    """Non-scouring bed level [m]"""
    LinkNo = "LinkNo"
    """LinkNo"""

class mrm_STNonScrLocalBedLevelTable(BaseTable):
    """Table for mrm_STNonScrLocalBedLevel (Non-scouring bed level)."""
    
    @property
    def columns(self) -> mrm_STNonScrLocalBedLevelTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mrm_STNonScrLocalBedLevelTableColumns(self)
        return self._columns