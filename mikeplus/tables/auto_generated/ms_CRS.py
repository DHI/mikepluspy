from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class ms_CRSTableColumns(BaseColumns):
    """Column names for ms_CRS (Generic shapes)."""
    MUID = "MUID"
    """ID"""
    AllowRecalculation = "AllowRecalculation"
    """AllowRecalculation"""
    TypeNo = "TypeNo"
    """Type"""
    Description = "Description"
    """Description"""

class ms_CRSTable(BaseTable):
    """Table for ms_CRS (Generic shapes)."""
    
    @property
    def columns(self) -> ms_CRSTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = ms_CRSTableColumns(self)
        return self._columns