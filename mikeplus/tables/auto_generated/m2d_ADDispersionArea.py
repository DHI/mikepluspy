from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class m2d_ADDispersionAreaTableColumns(BaseColumns):
    """Column names for m2d_ADDispersionArea (2D AD dispersion)."""
    MUID = "MUID"

class m2d_ADDispersionAreaTable(BaseTable):
    """Table for m2d_ADDispersionArea (2D AD dispersion)."""
    
    @property
    def columns(self) -> m2d_ADDispersionAreaTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = m2d_ADDispersionAreaTableColumns(self)
        return self._columns