from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class mw_AutocaliNodeDemandsTableColumns(BaseColumns):
    """Column names for mw_AutocaliNodeDemands (mw_AutocaliNodeDemands)."""
    MUID = "MUID"
    AutoCaliID = "AutoCaliID"
    PatternID = "PatternID"
    Enable = "Enable"
    MinFactor = "MinFactor"
    MaxFactor = "MaxFactor"
    CalibratedFactor = "CalibratedFactor"
    ApprovedFactor = "ApprovedFactor"
    Description = "Description"

class mw_AutocaliNodeDemandsTable(BaseTable):
    """Table for mw_AutocaliNodeDemands (mw_AutocaliNodeDemands)."""
    
    @property
    def columns(self) -> mw_AutocaliNodeDemandsTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mw_AutocaliNodeDemandsTableColumns(self)
        return self._columns