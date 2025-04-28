from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class mw_ReliabilityTableColumns(BaseColumns):
    """Column names for mw_Reliability (mw_Reliability)."""
    MUID = "MUID"
    EnablePddNo = "EnablePddNo"
    MinPre = "MinPre"
    RequiredPre = "RequiredPre"
    nCoeff = "nCoeff"
    Notes = "Notes"
    GlobalNodePddNo = "GlobalNodePddNo"
    EquationNo = "EquationNo"

class mw_ReliabilityTable(BaseTable):
    """Table for mw_Reliability (mw_Reliability)."""
    
    @property
    def columns(self) -> mw_ReliabilityTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mw_ReliabilityTableColumns(self)
        return self._columns