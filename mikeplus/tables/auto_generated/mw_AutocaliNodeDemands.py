from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class mw_AutocaliNodeDemandsTableColumns(BaseColumns):
    """Column names for mw_AutocaliNodeDemands (mw_AutocaliNodeDemands)."""
    MUID = "MUID"
    """MUID"""
    AutoCaliID = "AutoCaliID"
    """AutoCaliID"""
    PatternID = "PatternID"
    """Pattern ID"""
    Enable = "Enable"
    """Is active"""
    MinFactor = "MinFactor"
    """Minimum factor"""
    MaxFactor = "MaxFactor"
    """Maximum factor"""
    CalibratedFactor = "CalibratedFactor"
    """Calibrated factor"""
    ApprovedFactor = "ApprovedFactor"
    """Approved factor"""
    Description = "Description"
    """Description"""

class mw_AutocaliNodeDemandsTable(BaseTable):
    """Table for mw_AutocaliNodeDemands (mw_AutocaliNodeDemands)."""
    
    @property
    def columns(self) -> mw_AutocaliNodeDemandsTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mw_AutocaliNodeDemandsTableColumns(self)
        return self._columns