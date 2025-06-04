from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class mw_FlushingOutletTableColumns(BaseColumns):
    """Column names for mw_FlushingOutlet (Flushing outlet table)."""
    MUID = "MUID"
    """ID"""
    Sqn = "Sqn"
    """Sequence"""
    FlushingID = "FlushingID"
    """Flushing id"""
    TypeNo = "TypeNo"
    """Type"""
    OutletID = "OutletID"
    """Outlet ID"""
    LocalNo = "LocalNo"
    """Local no"""
    LocalFlow = "LocalFlow"
    """Local flow [m^3/s]"""

class mw_FlushingOutletTable(BaseTable):
    """Table for mw_FlushingOutlet (Flushing outlet table)."""
    
    @property
    def columns(self) -> mw_FlushingOutletTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mw_FlushingOutletTableColumns(self)
        return self._columns