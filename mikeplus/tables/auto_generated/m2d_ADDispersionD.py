from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class m2d_ADDispersionDTableColumns(BaseColumns):
    """Column names for m2d_ADDispersionD (Dispersion area, 2D)."""
    MUID = "MUID"
    """MUID"""
    DisperID = "DisperID"
    """DisperID"""
    Sqn = "Sqn"
    """Priority"""
    ApplyNo = "ApplyNo"
    """Apply"""
    AreaID = "AreaID"
    """Polygon ID"""
    LocalDisper = "LocalDisper"
    """Dispersion coefficient"""
    Description = "Description"
    """Description"""

class m2d_ADDispersionDTable(BaseTable):
    """Table for m2d_ADDispersionD (Dispersion area, 2D)."""
    
    @property
    def columns(self) -> m2d_ADDispersionDTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = m2d_ADDispersionDTableColumns(self)
        return self._columns