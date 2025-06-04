from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class mw_SourceTableColumns(BaseColumns):
    """Column names for mw_Source (Point constituent source)."""
    MUID = "MUID"
    """ID"""
    NodeTypeNo = "NodeTypeNo"
    """Node type"""
    NodeID = "NodeID"
    """Node ID"""
    SrcTypeNo = "SrcTypeNo"
    """Source type"""
    PatternID = "PatternID"
    """Pattern"""
    Enabled = "Enabled"
    """Is active"""
    Conc = "Conc"
    """Concentration [mu-g/m^3]"""

class mw_SourceTable(BaseTable):
    """Table for mw_Source (Point constituent source)."""
    
    @property
    def columns(self) -> mw_SourceTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mw_SourceTableColumns(self)
        return self._columns