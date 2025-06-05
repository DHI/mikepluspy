from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class mw_AutocaliPipesFrictTableColumns(BaseColumns):
    """Column names for mw_AutocaliPipesFrict (mw_AutocaliPipesFrict)."""
    MUID = "MUID"
    """Control ID"""
    AutoCaliID = "AutoCaliID"
    """AutoCaliID"""
    Enable = "Enable"
    """Is active"""
    SelectionID = "SelectionID"
    """Selection ID"""
    MinFriction = "MinFriction"
    """Minimum friction"""
    MaxFriction = "MaxFriction"
    """Maximum friction"""
    CalibratedFriction = "CalibratedFriction"
    """Calibrated friction [mm]"""
    ApprovedFriction = "ApprovedFriction"
    """Approved friction [mm]"""
    Description = "Description"
    """Description"""

class mw_AutocaliPipesFrictTable(BaseTable):
    """Table for mw_AutocaliPipesFrict (mw_AutocaliPipesFrict)."""
    
    @property
    def columns(self) -> mw_AutocaliPipesFrictTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mw_AutocaliPipesFrictTableColumns(self)
        return self._columns