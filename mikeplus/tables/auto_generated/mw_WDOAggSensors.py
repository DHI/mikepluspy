from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class mw_WDOAggSensorsTableColumns(BaseColumns):
    """Column names for mw_WDOAggSensors (Aggregation sensors)."""
    MUID = "MUID"
    """ID"""
    Comment = "Comment"
    """Description"""
    Enabled = "Enabled"
    """Is active"""
    OutputTable = "OutputTable"
    """Output table"""

class mw_WDOAggSensorsTable(BaseTable):
    """Table for mw_WDOAggSensors (Aggregation sensors)."""
    
    @property
    def columns(self) -> mw_WDOAggSensorsTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mw_WDOAggSensorsTableColumns(self)
        return self._columns