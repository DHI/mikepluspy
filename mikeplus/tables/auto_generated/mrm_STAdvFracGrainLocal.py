from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class mrm_STAdvFracGrainLocalTableColumns(BaseColumns):
    """Column names for mrm_STAdvFracGrainLocal (mrm_STAdvFracGrainLocal)."""
    MUID = "MUID"
    """ID"""
    STFracID = "STFracID"
    """STFracID"""
    GrainSize = "GrainSize"
    """Local grain size [mm]"""
    TypeNo = "TypeNo"
    """Location type"""
    LinkID = "LinkID"
    """Link ID"""
    LinkNo = "LinkNo"
    """LinkNo"""
    Chainage = "Chainage"
    """Chainage [m]"""
    ListID = "ListID"
    """List ID"""

class mrm_STAdvFracGrainLocalTable(BaseTable):
    """Table for mrm_STAdvFracGrainLocal (mrm_STAdvFracGrainLocal)."""
    
    @property
    def columns(self) -> mrm_STAdvFracGrainLocalTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mrm_STAdvFracGrainLocalTableColumns(self)
        return self._columns