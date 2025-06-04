from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class m2d_BndDistributedSourceTableColumns(BaseColumns):
    """Column names for m2d_BndDistributedSource (m2d_BndDistributedSource)."""
    MUID = "MUID"
    """MUID"""
    BndID = "BndID"
    """BndID"""
    Sqn = "Sqn"
    """Sqn"""
    TypeNo = "TypeNo"
    """TypeNo"""
    X = "X"
    """X coordinate [m]"""
    Y = "Y"
    """Y coordinate [m]"""

class m2d_BndDistributedSourceTable(BaseTable):
    """Table for m2d_BndDistributedSource (m2d_BndDistributedSource)."""
    
    @property
    def columns(self) -> m2d_BndDistributedSourceTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = m2d_BndDistributedSourceTableColumns(self)
        return self._columns