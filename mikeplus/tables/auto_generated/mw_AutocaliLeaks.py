from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class mw_AutocaliLeaksTableColumns(BaseColumns):
    """Column names for mw_AutocaliLeaks (mw_AutocaliLeaks)."""
    MUID = "MUID"
    AutoCaliID = "AutoCaliID"
    JunctionID = "JunctionID"
    Enable = "Enable"
    MaxEmCoeff = "MaxEmCoeff"
    CalibratedEmCoeff = "CalibratedEmCoeff"
    CalibratedLeak = "CalibratedLeak"
    ApprovedEmCoeff = "ApprovedEmCoeff"
    Description = "Description"

class mw_AutocaliLeaksTable(BaseTable):
    """Table for mw_AutocaliLeaks (mw_AutocaliLeaks)."""
    
    @property
    def columns(self) -> mw_AutocaliLeaksTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mw_AutocaliLeaksTableColumns(self)
        return self._columns