from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class mrm_STPassiveLinkTableColumns(BaseColumns):
    """Column names for mrm_STPassiveLink (Passive links)."""
    MUID = "MUID"
    LinkID = "LinkID"
    LinkNo = "LinkNo"
    StartChainage = "StartChainage"
    EndChainage = "EndChainage"

class mrm_STPassiveLinkTable(BaseTable):
    """Table for mrm_STPassiveLink (Passive links)."""
    
    @property
    def columns(self) -> mrm_STPassiveLinkTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mrm_STPassiveLinkTableColumns(self)
        return self._columns