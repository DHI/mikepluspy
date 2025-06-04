from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class msm_LTSInitTableColumns(BaseColumns):
    """Column names for msm_LTSInit (LTS initial conditions)."""
    MUID = "MUID"
    """MUID"""
    HotStartFilename = "HotStartFilename"
    """Hot start file"""
    InitDate = "InitDate"
    """Date"""
    InitFrom = "InitFrom"
    """From [m^3/s]"""
    InitTo = "InitTo"
    """To [m^3/s]"""

class msm_LTSInitTable(BaseTable):
    """Table for msm_LTSInit (LTS initial conditions)."""
    
    @property
    def columns(self) -> msm_LTSInitTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = msm_LTSInitTableColumns(self)
        return self._columns