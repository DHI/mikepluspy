from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class mss_AquiferTableColumns(BaseColumns):
    """Column names for mss_Aquifer (Aquifers)."""
    MUID = "MUID"
    Por = "Por"
    WP = "WP"
    FC = "FC"
    K = "K"
    Kslope = "Kslope"
    Yslope = "Yslope"
    UEF = "UEF"
    LED = "LED"
    GWR = "GWR"
    BE = "BE"
    WTE = "WTE"
    UMC = "UMC"
    UZEP = "UZEP"

class mss_AquiferTable(BaseTable):
    """Table for mss_Aquifer (Aquifers)."""
    
    @property
    def columns(self) -> mss_AquiferTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mss_AquiferTableColumns(self)
        return self._columns