from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class msm_PumpESEDTableColumns(BaseColumns):
    """Column names for msm_PumpESED (ESE setupD)."""
    MUID = "MUID"
    PumpESEID = "PumpESEID"
    Pump1ID = "Pump1ID"
    Pump2ID = "Pump2ID"
    Pump3ID = "Pump3ID"
    Pump4ID = "Pump4ID"
    Pump5ID = "Pump5ID"

class msm_PumpESEDTable(BaseTable):
    """Table for msm_PumpESED (ESE setupD)."""
    
    @property
    def columns(self) -> msm_PumpESEDTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = msm_PumpESEDTableColumns(self)
        return self._columns