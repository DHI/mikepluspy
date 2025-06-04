from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class mrm_STLocalBedParMorphTableColumns(BaseColumns):
    """Column names for mrm_STLocalBedParMorph (Local update method)."""
    MUID = "MUID"
    """MUID"""
    LinkID = "LinkID"
    """River ID"""
    Chainage = "Chainage"
    """Chainage [m]"""
    MethodNo = "MethodNo"
    """Method"""
    LinkNo = "LinkNo"
    """LinkNo"""

class mrm_STLocalBedParMorphTable(BaseTable):
    """Table for mrm_STLocalBedParMorph (Local update method)."""
    
    @property
    def columns(self) -> mrm_STLocalBedParMorphTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mrm_STLocalBedParMorphTableColumns(self)
        return self._columns