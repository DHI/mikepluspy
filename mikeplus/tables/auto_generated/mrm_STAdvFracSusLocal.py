from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class mrm_STAdvFracSusLocalTableColumns(BaseColumns):
    """Column names for mrm_STAdvFracSusLocal (mrm_STAdvFracSusLocal)."""
    MUID = "MUID"
    """MUID"""
    STFracID = "STFracID"
    """STFracID"""
    LinkID = "LinkID"
    """Link ID"""
    LinkNo = "LinkNo"
    """LinkNo"""
    Chainage = "Chainage"
    """Chainage [m]"""
    ErStress = "ErStress"
    """Erosion shear stress limit [N/m^2]"""
    ErCoef = "ErCoef"
    """Erosion coefficient [g/m^2/d]"""
    DepStress = "DepStress"
    """Deposition shear stress limit [N/m^2]"""

class mrm_STAdvFracSusLocalTable(BaseTable):
    """Table for mrm_STAdvFracSusLocal (mrm_STAdvFracSusLocal)."""
    
    @property
    def columns(self) -> mrm_STAdvFracSusLocalTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mrm_STAdvFracSusLocalTableColumns(self)
        return self._columns