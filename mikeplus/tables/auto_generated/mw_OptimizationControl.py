from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class mw_OptimizationControlTableColumns(BaseColumns):
    """Column names for mw_OptimizationControl (Controls)."""
    MUID = "MUID"
    """MUID"""
    OptimizationID = "OptimizationID"
    """OptimizationID"""
    CtrlID = "CtrlID"
    """Control ID"""
    Enabled = "Enabled"
    """Is active"""
    LinkTypeNo = "LinkTypeNo"
    """Controlled link type"""
    LinkID = "LinkID"
    """Controlled link ID"""
    TypeNo = "TypeNo"
    """Control type"""
    PatternLength = "PatternLength"
    """Pattern length"""
    MinDecisionInterval = "MinDecisionInterval"
    """Minimum decision interval"""
    CurveID = "CurveID"
    """Optimization setpoint table"""
    Description = "Description"
    """Description"""

class mw_OptimizationControlTable(BaseTable):
    """Table for mw_OptimizationControl (Controls)."""
    
    @property
    def columns(self) -> mw_OptimizationControlTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mw_OptimizationControlTableColumns(self)
        return self._columns