from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class msm_PumpESEDTableColumns(BaseColumns):
    """Column names for msm_PumpESED (ESE setupD)."""
    MUID = "MUID"
    """Section ID"""
    PumpESEID = "PumpESEID"
    """PumpESEID"""
    Pump1ID = "Pump1ID"
    """Pump 1"""
    Pump2ID = "Pump2ID"
    """Pump 2"""
    Pump3ID = "Pump3ID"
    """Pump 3"""
    Pump4ID = "Pump4ID"
    """Pump 4"""
    Pump5ID = "Pump5ID"
    """Pump 5"""

class msm_PumpESEDTable(BaseTable):
    """Table for msm_PumpESED (ESE setupD)."""
    
    @property
    def columns(self) -> msm_PumpESEDTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = msm_PumpESEDTableColumns(self)
        return self._columns