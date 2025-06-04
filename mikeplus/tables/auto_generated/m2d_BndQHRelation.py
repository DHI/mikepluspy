from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class m2d_BndQHRelationTableColumns(BaseColumns):
    """Column names for m2d_BndQHRelation (Q/h relation)."""
    MUID = "MUID"
    """MUID"""
    BndID = "BndID"
    """BndID"""
    Sqn = "Sqn"
    """Sqn"""
    Q = "Q"
    """Discharge [m^3/s]"""
    H = "H"
    """Water level [m]"""

class m2d_BndQHRelationTable(BaseTable):
    """Table for m2d_BndQHRelation (Q/h relation)."""
    
    @property
    def columns(self) -> m2d_BndQHRelationTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = m2d_BndQHRelationTableColumns(self)
        return self._columns