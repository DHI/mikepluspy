from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class mrm_STLocalBedParThickTableColumns(BaseColumns):
    """Column names for mrm_STLocalBedParThick (Local target thickness)."""
    MUID = "MUID"
    LinkID = "LinkID"
    Chainage = "Chainage"
    LocFactor = "LocFactor"
    LocLayerDepthNo = "LocLayerDepthNo"
    LocMin = "LocMin"
    LocMax = "LocMax"
    LinkNo = "LinkNo"

class mrm_STLocalBedParThickTable(BaseTable):
    """Table for mrm_STLocalBedParThick (Local target thickness)."""
    
    @property
    def columns(self) -> mrm_STLocalBedParThickTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mrm_STLocalBedParThickTableColumns(self)
        return self._columns