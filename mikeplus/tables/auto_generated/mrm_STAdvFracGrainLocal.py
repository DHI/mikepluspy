from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class mrm_STAdvFracGrainLocalTableColumns(BaseColumns):
    """Column names for mrm_STAdvFracGrainLocal (mrm_STAdvFracGrainLocal)."""
    MUID = "MUID"
    STFracID = "STFracID"
    GrainSize = "GrainSize"
    TypeNo = "TypeNo"
    LinkID = "LinkID"
    LinkNo = "LinkNo"
    Chainage = "Chainage"
    ListID = "ListID"

class mrm_STAdvFracGrainLocalTable(BaseTable):
    """Table for mrm_STAdvFracGrainLocal (mrm_STAdvFracGrainLocal)."""
    
    @property
    def columns(self) -> mrm_STAdvFracGrainLocalTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mrm_STAdvFracGrainLocalTableColumns(self)
        return self._columns