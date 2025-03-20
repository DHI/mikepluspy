from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class mw_FrictionTableColumns(BaseColumns):
    """Column names for mw_Friction (Roughness)."""
    MUID = "MUID"
    DW = "DW"
    HW = "HW"
    M = "M"
    MHW = "MHW"
    Description = "Description"

class mw_FrictionTable(BaseTable):
    """Table for mw_Friction (Roughness)."""
    
    @property
    def columns(self) -> mw_FrictionTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mw_FrictionTableColumns(self)
        return self._columns