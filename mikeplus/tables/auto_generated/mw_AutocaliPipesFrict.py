from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class mw_AutocaliPipesFrictTableColumns(BaseColumns):
    """Column names for mw_AutocaliPipesFrict (mw_AutocaliPipesFrict)."""
    MUID = "MUID"
    AutoCaliID = "AutoCaliID"
    Enable = "Enable"
    SelectionID = "SelectionID"
    MinFriction = "MinFriction"
    MaxFriction = "MaxFriction"
    CalibratedFriction = "CalibratedFriction"
    ApprovedFriction = "ApprovedFriction"
    Description = "Description"

class mw_AutocaliPipesFrictTable(BaseTable):
    """Table for mw_AutocaliPipesFrict (mw_AutocaliPipesFrict)."""
    
    @property
    def columns(self) -> mw_AutocaliPipesFrictTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mw_AutocaliPipesFrictTableColumns(self)
        return self._columns