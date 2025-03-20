from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class mrm_WeirQHRelationTableColumns(BaseColumns):
    """Column names for mrm_WeirQHRelation (Weir Qh relations)."""
    MUID = "MUID"
    WeirID = "WeirID"
    Sqn = "Sqn"
    Q = "Q"
    HPos = "HPos"
    HNeg = "HNeg"
    HWeir = "HWeir"
    Width = "Width"
    Area = "Area"

class mrm_WeirQHRelationTable(BaseTable):
    """Table for mrm_WeirQHRelation (Weir Qh relations)."""
    
    @property
    def columns(self) -> mrm_WeirQHRelationTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mrm_WeirQHRelationTableColumns(self)
        return self._columns