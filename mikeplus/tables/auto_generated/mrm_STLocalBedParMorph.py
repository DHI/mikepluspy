from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class mrm_STLocalBedParMorphTableColumns(BaseColumns):
    """Column names for mrm_STLocalBedParMorph (Local update method)."""
    MUID = "MUID"
    LinkID = "LinkID"
    Chainage = "Chainage"
    MethodNo = "MethodNo"
    LinkNo = "LinkNo"

class mrm_STLocalBedParMorphTable(BaseTable):
    """Table for mrm_STLocalBedParMorph (Local update method)."""
    
    @property
    def columns(self) -> mrm_STLocalBedParMorphTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mrm_STLocalBedParMorphTableColumns(self)
        return self._columns