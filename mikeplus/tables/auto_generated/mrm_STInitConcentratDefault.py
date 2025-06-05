from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class mrm_STInitConcentratDefaultTableColumns(BaseColumns):
    """Column names for mrm_STInitConcentratDefault (ST initial concentrations)."""
    MUID = "MUID"
    """MUID"""
    DefaultFrac = "DefaultFrac"
    """Cohesive fraction"""
    GlobalIniConc = "GlobalIniConc"
    """Initial concentration [g/m^3]"""

class mrm_STInitConcentratDefaultTable(BaseTable):
    """Table for mrm_STInitConcentratDefault (ST initial concentrations)."""
    
    @property
    def columns(self) -> mrm_STInitConcentratDefaultTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mrm_STInitConcentratDefaultTableColumns(self)
        return self._columns