from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class mw_SourceTableColumns(BaseColumns):
    """Column names for mw_Source (Point constituent source)."""
    MUID = "MUID"
    NodeTypeNo = "NodeTypeNo"
    NodeID = "NodeID"
    SrcTypeNo = "SrcTypeNo"
    PatternID = "PatternID"
    Enabled = "Enabled"
    Conc = "Conc"

class mw_SourceTable(BaseTable):
    """Table for mw_Source (Point constituent source)."""
    
    @property
    def columns(self) -> mw_SourceTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mw_SourceTableColumns(self)
        return self._columns