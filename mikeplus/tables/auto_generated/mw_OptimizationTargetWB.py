from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class mw_OptimizationTargetWBTableColumns(BaseColumns):
    """Column names for mw_OptimizationTargetWB (mw_OptimizationTargetWB)."""
    MUID = "MUID"
    """ID"""
    OptimTargetID = "OptimTargetID"
    """OptimTargetID"""
    SourcePipe = "SourcePipe"
    """Water source outlet"""
    TargetPct = "TargetPct"
    """Water source percentage [%]"""

class mw_OptimizationTargetWBTable(BaseTable):
    """Table for mw_OptimizationTargetWB (mw_OptimizationTargetWB)."""
    
    @property
    def columns(self) -> mw_OptimizationTargetWBTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mw_OptimizationTargetWBTableColumns(self)
        return self._columns