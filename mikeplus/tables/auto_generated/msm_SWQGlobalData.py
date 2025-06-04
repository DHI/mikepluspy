from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class msm_SWQGlobalDataTableColumns(BaseColumns):
    """Column names for msm_SWQGlobalData (SWQ global data)."""
    MUID = "MUID"
    """ID"""
    ADWPini = "ADWPini"
    """Initial ADWP [h]"""
    ADWPmin = "ADWPmin"
    """Min. ADWP [h]"""
    EventThreshold = "EventThreshold"
    """Event threshold [mm/h]"""

class msm_SWQGlobalDataTable(BaseTable):
    """Table for msm_SWQGlobalData (SWQ global data)."""
    
    @property
    def columns(self) -> msm_SWQGlobalDataTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = msm_SWQGlobalDataTableColumns(self)
        return self._columns