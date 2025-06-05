from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class mrm_STLocalBedParThickTableColumns(BaseColumns):
    """Column names for mrm_STLocalBedParThick (Local target thickness)."""
    MUID = "MUID"
    """MUID"""
    LinkID = "LinkID"
    """Link ID"""
    Chainage = "Chainage"
    """Chainage [m]"""
    LocFactor = "LocFactor"
    """Factor [()]"""
    LocLayerDepthNo = "LocLayerDepthNo"
    """Layer depth type"""
    LocMin = "LocMin"
    """Minimum value [m]"""
    LocMax = "LocMax"
    """Maximum value [m]"""
    LinkNo = "LinkNo"
    """LinkNo"""

class mrm_STLocalBedParThickTable(BaseTable):
    """Table for mrm_STLocalBedParThick (Local target thickness)."""
    
    @property
    def columns(self) -> mrm_STLocalBedParThickTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mrm_STLocalBedParThickTableColumns(self)
        return self._columns