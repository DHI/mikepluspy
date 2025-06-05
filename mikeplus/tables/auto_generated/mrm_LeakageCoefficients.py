from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class mrm_LeakageCoefficientsTableColumns(BaseColumns):
    """Column names for mrm_LeakageCoefficients (Leakage coefficients)."""
    MUID = "MUID"
    """ID"""
    RiverID = "RiverID"
    """River ID"""
    Chainage = "Chainage"
    """Chainage [m]"""
    Leakage = "Leakage"
    """Leakage coefficient [/s]"""

class mrm_LeakageCoefficientsTable(BaseTable):
    """Table for mrm_LeakageCoefficients (Leakage coefficients)."""
    
    @property
    def columns(self) -> mrm_LeakageCoefficientsTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mrm_LeakageCoefficientsTableColumns(self)
        return self._columns