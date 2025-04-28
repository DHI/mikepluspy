from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class mrm_WindScaleFactorLocalTableColumns(BaseColumns):
    """Column names for mrm_WindScaleFactorLocal (Wind scaling factors)."""
    MUID = "MUID"
    LinkID = "LinkID"
    Chainage = "Chainage"
    ScaleFactor = "ScaleFactor"

class mrm_WindScaleFactorLocalTable(BaseTable):
    """Table for mrm_WindScaleFactorLocal (Wind scaling factors)."""
    
    @property
    def columns(self) -> mrm_WindScaleFactorLocalTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mrm_WindScaleFactorLocalTableColumns(self)
        return self._columns