from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class mw_AutocaliLeaksTableColumns(BaseColumns):
    """Column names for mw_AutocaliLeaks (mw_AutocaliLeaks)."""
    MUID = "MUID"
    """MUID"""
    AutoCaliID = "AutoCaliID"
    """AutoCaliID"""
    JunctionID = "JunctionID"
    """Junction ID"""
    Enable = "Enable"
    """Is active"""
    MaxEmCoeff = "MaxEmCoeff"
    """Maximum emitter coeff [l/s/m^(1/2)]"""
    CalibratedEmCoeff = "CalibratedEmCoeff"
    """Calibrated emitter coeff [l/s/m^(1/2)]"""
    CalibratedLeak = "CalibratedLeak"
    """Calibrated leakage [m^3/s]"""
    ApprovedEmCoeff = "ApprovedEmCoeff"
    """Approved emitter coeff [l/s/m^(1/2)]"""
    Description = "Description"
    """Description"""

class mw_AutocaliLeaksTable(BaseTable):
    """Table for mw_AutocaliLeaks (mw_AutocaliLeaks)."""
    
    @property
    def columns(self) -> mw_AutocaliLeaksTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mw_AutocaliLeaksTableColumns(self)
        return self._columns