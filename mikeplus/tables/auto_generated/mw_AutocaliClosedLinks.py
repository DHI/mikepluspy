from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class mw_AutocaliClosedLinksTableColumns(BaseColumns):
    """Column names for mw_AutocaliClosedLinks (mw_AutocaliClosedLinks)."""
    MUID = "MUID"
    """MUID"""
    AutoCaliID = "AutoCaliID"
    """AutoCaliID"""
    LinkTypeNo = "LinkTypeNo"
    """Link type"""
    LinkID = "LinkID"
    """Link ID"""
    Enable = "Enable"
    """Is active"""
    CurrStatus = "CurrStatus"
    """Current status"""
    CalibratedStatus = "CalibratedStatus"
    """Calibrated status"""
    ApprovedStatus = "ApprovedStatus"
    """Approved status"""
    Description = "Description"
    """Description"""

class mw_AutocaliClosedLinksTable(BaseTable):
    """Table for mw_AutocaliClosedLinks (mw_AutocaliClosedLinks)."""
    
    @property
    def columns(self) -> mw_AutocaliClosedLinksTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mw_AutocaliClosedLinksTableColumns(self)
        return self._columns