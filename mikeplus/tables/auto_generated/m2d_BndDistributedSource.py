from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class m2d_BndDistributedSourceTableColumns(BaseColumns):
    """Column names for m2d_BndDistributedSource (m2d_BndDistributedSource)."""
    MUID = "MUID"
    BndID = "BndID"
    Sqn = "Sqn"
    TypeNo = "TypeNo"
    X = "X"
    Y = "Y"

class m2d_BndDistributedSourceTable(BaseTable):
    """Table for m2d_BndDistributedSource (m2d_BndDistributedSource)."""
    
    @property
    def columns(self) -> m2d_BndDistributedSourceTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = m2d_BndDistributedSourceTableColumns(self)
        return self._columns