from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class ms_MaterialTableColumns(BaseColumns):
    """Column names for ms_Material (Materials)."""
    MUID = "MUID"
    Manning = "Manning"
    ManningN = "ManningN"
    EQRough = "EQRough"
    HWCoef = "HWCoef"
    Description = "Description"

class ms_MaterialTable(BaseTable):
    """Table for ms_Material (Materials)."""
    
    @property
    def columns(self) -> ms_MaterialTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = ms_MaterialTableColumns(self)
        return self._columns