from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class m2d_ADInfiltrationDTableColumns(BaseColumns):
    """Column names for m2d_ADInfiltrationD (AD infiltration area in 2D domain)."""
    MUID = "MUID"
    """MUID"""
    InfilID = "InfilID"
    """InfilID"""
    Sqn = "Sqn"
    """Priority"""
    ApplyNo = "ApplyNo"
    """Apply"""
    AreaID = "AreaID"
    """Polygon ID"""
    LocalInfil = "LocalInfil"
    """Infiltration"""
    Description = "Description"
    """Description"""

class m2d_ADInfiltrationDTable(BaseTable):
    """Table for m2d_ADInfiltrationD (AD infiltration area in 2D domain)."""
    
    @property
    def columns(self) -> m2d_ADInfiltrationDTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = m2d_ADInfiltrationDTableColumns(self)
        return self._columns