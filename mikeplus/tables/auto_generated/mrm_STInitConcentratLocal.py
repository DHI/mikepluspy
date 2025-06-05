from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class mrm_STInitConcentratLocalTableColumns(BaseColumns):
    """Column names for mrm_STInitConcentratLocal (ST initial concentrations)."""
    MUID = "MUID"
    """MUID"""
    ConnectionTypeNo = "ConnectionTypeNo"
    """Connection type"""
    ListName = "ListName"
    """List"""
    LinkID = "LinkID"
    """Entire link"""
    Chainage = "Chainage"
    """Chainage [m]"""
    LocalFractionID = "LocalFractionID"
    """Cohesive fraction"""
    LocalConcentration = "LocalConcentration"
    """Initial concentration [g/m^3]"""
    LinkNo = "LinkNo"
    """LinkNo"""

class mrm_STInitConcentratLocalTable(BaseTable):
    """Table for mrm_STInitConcentratLocal (ST initial concentrations)."""
    
    @property
    def columns(self) -> mrm_STInitConcentratLocalTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mrm_STInitConcentratLocalTableColumns(self)
        return self._columns