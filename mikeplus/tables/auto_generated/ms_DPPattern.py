from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class ms_DPPatternTableColumns(BaseColumns):
    """Column names for ms_DPPattern (Diurnal patterns)."""
    MUID = "MUID"
    """ID"""
    DeltaT = "DeltaT"
    """Delta [min]"""
    Description = "Description"
    """Description"""

class ms_DPPatternTable(BaseTable):
    """Table for ms_DPPattern (Diurnal patterns)."""
    
    @property
    def columns(self) -> ms_DPPatternTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = ms_DPPatternTableColumns(self)
        return self._columns