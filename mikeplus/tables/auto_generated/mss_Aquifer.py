from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class mss_AquiferTableColumns(BaseColumns):
    """Column names for mss_Aquifer (Aquifers)."""
    MUID = "MUID"
    """ID"""
    Por = "Por"
    """Porosity"""
    WP = "WP"
    """Wilting point"""
    FC = "FC"
    """Field capacity"""
    K = "K"
    """Conductivity, K [mm/h]"""
    Kslope = "Kslope"
    """Slope of conductivity"""
    Yslope = "Yslope"
    """Slope of soil tension"""
    UEF = "UEF"
    """Fraction of total evap"""
    LED = "LED"
    """Max depth [m]"""
    GWR = "GWR"
    """Rate of percolation [mm/h]"""
    BE = "BE"
    """Aquifer elevation [m]"""
    WTE = "WTE"
    """Water table elevation [m]"""
    UMC = "UMC"
    """Initial moisture content"""
    UZEP = "UZEP"
    """Upper zone evaporation"""

class mss_AquiferTable(BaseTable):
    """Table for mss_Aquifer (Aquifers)."""
    
    @property
    def columns(self) -> mss_AquiferTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mss_AquiferTableColumns(self)
        return self._columns