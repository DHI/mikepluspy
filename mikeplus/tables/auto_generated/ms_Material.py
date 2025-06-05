from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class ms_MaterialTableColumns(BaseColumns):
    """Column names for ms_Material (Materials)."""
    MUID = "MUID"
    """ID"""
    Manning = "Manning"
    """Manning (M) [m^(1/3)/s]"""
    ManningN = "ManningN"
    """Manning (n) [s/m^(1/3)]"""
    EQRough = "EQRough"
    """Equivalent roughness [m]"""
    HWCoef = "HWCoef"
    """Hazen-Williams coefficient"""
    Description = "Description"
    """Description"""

class ms_MaterialTable(BaseTable):
    """Table for ms_Material (Materials)."""
    
    @property
    def columns(self) -> ms_MaterialTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = ms_MaterialTableColumns(self)
        return self._columns