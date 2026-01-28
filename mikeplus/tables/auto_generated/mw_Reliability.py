from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class mw_ReliabilityTableColumns(BaseColumns):
    """Column names for mw_Reliability (mw_Reliability)."""
    MUID = "MUID"
    """ID"""
    EnablePddNo = "EnablePddNo"
    """Enable PDD simulation"""
    MinPre = "MinPre"
    """Minimum pressure [m]"""
    RequiredPre = "RequiredPre"
    """Required pressure [m]"""
    nCoeff = "nCoeff"
    """Exponent"""
    Notes = "Notes"
    """Notes"""
    GlobalNodePddNo = "GlobalNodePddNo"
    """Global node are pressure dependent"""
    EquationNo = "EquationNo"
    """Formula"""

class mw_ReliabilityTable(BaseTable):
    """Table for mw_Reliability (mw_Reliability)."""
    
    @property
    def columns(self) -> mw_ReliabilityTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mw_ReliabilityTableColumns(self)
        return self._columns