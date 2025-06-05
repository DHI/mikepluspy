from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class mw_LossTableColumns(BaseColumns):
    """Column names for mw_Loss (Loss coefficient)."""
    MUID = "MUID"
    """MUID"""
    Coeff = "Coeff"
    """Loss coefficient"""
    Description = "Description"
    """Description"""

class mw_LossTable(BaseTable):
    """Table for mw_Loss (Loss coefficient)."""
    
    @property
    def columns(self) -> mw_LossTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mw_LossTableColumns(self)
        return self._columns