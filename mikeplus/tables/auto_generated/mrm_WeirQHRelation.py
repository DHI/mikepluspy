from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class mrm_WeirQHRelationTableColumns(BaseColumns):
    """Column names for mrm_WeirQHRelation (Weir Qh relations)."""
    MUID = "MUID"
    """MUID"""
    WeirID = "WeirID"
    """WeirID"""
    Sqn = "Sqn"
    """Sqn"""
    Q = "Q"
    """Q [m^3/s]"""
    HPos = "HPos"
    """H-Pos [m]"""
    HNeg = "HNeg"
    """H-Neg [m]"""
    HWeir = "HWeir"
    """H-Weir [m]"""
    Width = "Width"
    """Width [m]"""
    Area = "Area"
    """Area [m^2]"""

class mrm_WeirQHRelationTable(BaseTable):
    """Table for mrm_WeirQHRelation (Weir Qh relations)."""
    
    @property
    def columns(self) -> mrm_WeirQHRelationTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mrm_WeirQHRelationTableColumns(self)
        return self._columns