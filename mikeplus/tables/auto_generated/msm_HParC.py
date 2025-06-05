from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class msm_HParCTableColumns(BaseColumns):
    """Column names for msm_HParC (Parameters linear reservoir)."""
    MUID = "MUID"
    """ID"""
    MaxCap = "MaxCap"
    """Maximum [mm/h]"""
    Rfactor = "Rfactor"
    """Reduction factor [()]"""
    Iloss = "Iloss"
    """Initial loss [mm]"""
    Lagtime = "Lagtime"
    """Lag time (C2 only) [min]"""
    InfiltrNo = "InfiltrNo"
    """Infiltration"""
    MinCap = "MinCap"
    """Minimum [mm/h]"""
    WetCond = "WetCond"
    """Wet condition [/h]"""
    DryCond = "DryCond"
    """Dry condition [/h]"""
    Ctime = "Ctime"
    """Time constant (C1 only) [/h]"""

class msm_HParCTable(BaseTable):
    """Table for msm_HParC (Parameters linear reservoir)."""
    
    @property
    def columns(self) -> msm_HParCTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = msm_HParCTableColumns(self)
        return self._columns