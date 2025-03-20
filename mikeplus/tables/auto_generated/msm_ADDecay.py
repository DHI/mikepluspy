from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class msm_ADDecayTableColumns(BaseColumns):
    """Column names for msm_ADDecay (Decay)."""
    MUID = "MUID"
    LocTypeNo = "LocTypeNo"
    ListID = "ListID"
    LinkID = "LinkID"
    StartChainage = "StartChainage"
    EndChainage = "EndChainage"
    LocalWQCompID = "LocalWQCompID"
    LocalDecay = "LocalDecay"

class msm_ADDecayTable(BaseTable):
    """Table for msm_ADDecay (Decay)."""
    
    @property
    def columns(self) -> msm_ADDecayTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = msm_ADDecayTableColumns(self)
        return self._columns