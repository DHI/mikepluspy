from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class m2d_ADEvaporationDTableColumns(BaseColumns):
    """Column names for m2d_ADEvaporationD (AD evaporations area in 2D domain)."""
    MUID = "MUID"
    """MUID"""
    EvapoID = "EvapoID"
    """EvapoID"""
    Sqn = "Sqn"
    """Priority"""
    ApplyNo = "ApplyNo"
    """Apply"""
    AreaID = "AreaID"
    """Polygon ID"""
    LocalEvapo = "LocalEvapo"
    """Evaporation"""
    Description = "Description"
    """Description"""

class m2d_ADEvaporationDTable(BaseTable):
    """Table for m2d_ADEvaporationD (AD evaporations area in 2D domain)."""
    
    @property
    def columns(self) -> m2d_ADEvaporationDTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = m2d_ADEvaporationDTableColumns(self)
        return self._columns