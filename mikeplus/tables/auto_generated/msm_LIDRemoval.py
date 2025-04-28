from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class msm_LIDRemovalTableColumns(BaseColumns):
    """Column names for msm_LIDRemoval (Pollutions removal in LIDS)."""
    MUID = "MUID"
    LIDID = "LIDID"
    ComponentID = "ComponentID"
    OverflowRemovalFac = "OverflowRemovalFac"
    DrainRemovalFac = "DrainRemovalFac"

class msm_LIDRemovalTable(BaseTable):
    """Table for msm_LIDRemoval (Pollutions removal in LIDS)."""
    
    @property
    def columns(self) -> msm_LIDRemovalTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = msm_LIDRemovalTableColumns(self)
        return self._columns