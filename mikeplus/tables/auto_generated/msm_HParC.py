from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class msm_HParCTableColumns(BaseColumns):
    """Column names for msm_HParC (Parameters linear reservoir)."""
    MUID = "MUID"
    MaxCap = "MaxCap"
    Rfactor = "Rfactor"
    Iloss = "Iloss"
    Lagtime = "Lagtime"
    InfiltrNo = "InfiltrNo"
    MinCap = "MinCap"
    WetCond = "WetCond"
    DryCond = "DryCond"
    Ctime = "Ctime"

class msm_HParCTable(BaseTable):
    """Table for msm_HParC (Parameters linear reservoir)."""
    
    @property
    def columns(self) -> msm_HParCTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = msm_HParCTableColumns(self)
        return self._columns