from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class mw_AutocaliClosedLinksTableColumns(BaseColumns):
    """Column names for mw_AutocaliClosedLinks (mw_AutocaliClosedLinks)."""
    MUID = "MUID"
    AutoCaliID = "AutoCaliID"
    LinkTypeNo = "LinkTypeNo"
    LinkID = "LinkID"
    Enable = "Enable"
    CurrStatus = "CurrStatus"
    CalibratedStatus = "CalibratedStatus"
    ApprovedStatus = "ApprovedStatus"
    Description = "Description"

class mw_AutocaliClosedLinksTable(BaseTable):
    """Table for mw_AutocaliClosedLinks (mw_AutocaliClosedLinks)."""
    
    @property
    def columns(self) -> mw_AutocaliClosedLinksTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mw_AutocaliClosedLinksTableColumns(self)
        return self._columns