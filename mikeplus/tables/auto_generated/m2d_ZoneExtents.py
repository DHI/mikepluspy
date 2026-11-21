from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class m2d_ZoneExtentsTableColumns(BaseColumns):
    """Column names for m2d_ZoneExtents (m2d_ZoneExtents)."""
    MUID = "MUID"
    """Zone ID"""
    CodeNumber = "CodeNumber"
    """Code number"""

class m2d_ZoneExtentsTable(BaseTable):
    """Table for m2d_ZoneExtents (m2d_ZoneExtents)."""
    
    @property
    def columns(self) -> m2d_ZoneExtentsTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = m2d_ZoneExtentsTableColumns(self)
        return self._columns