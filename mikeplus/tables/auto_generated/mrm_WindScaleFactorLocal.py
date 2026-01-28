from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class mrm_WindScaleFactorLocalTableColumns(BaseColumns):
    """Column names for mrm_WindScaleFactorLocal (Wind scaling factors)."""
    MUID = "MUID"
    """ID"""
    LinkID = "LinkID"
    """River ID"""
    Chainage = "Chainage"
    """Chainage [m]"""
    ScaleFactor = "ScaleFactor"
    """Wind scale factor [()]"""

class mrm_WindScaleFactorLocalTable(BaseTable):
    """Table for mrm_WindScaleFactorLocal (Wind scaling factors)."""
    
    @property
    def columns(self) -> mrm_WindScaleFactorLocalTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mrm_WindScaleFactorLocalTableColumns(self)
        return self._columns