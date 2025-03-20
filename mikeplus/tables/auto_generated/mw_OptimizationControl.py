from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class mw_OptimizationControlTableColumns(BaseColumns):
    """Column names for mw_OptimizationControl (Controls)."""
    MUID = "MUID"
    OptimizationID = "OptimizationID"
    CtrlID = "CtrlID"
    Enabled = "Enabled"
    LinkTypeNo = "LinkTypeNo"
    LinkID = "LinkID"
    TypeNo = "TypeNo"
    PatternLength = "PatternLength"
    MinDecisionInterval = "MinDecisionInterval"
    CurveID = "CurveID"
    Description = "Description"

class mw_OptimizationControlTable(BaseTable):
    """Table for mw_OptimizationControl (Controls)."""
    
    @property
    def columns(self) -> mw_OptimizationControlTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mw_OptimizationControlTableColumns(self)
        return self._columns