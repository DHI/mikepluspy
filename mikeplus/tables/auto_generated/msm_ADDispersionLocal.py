from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class msm_ADDispersionLocalTableColumns(BaseColumns):
    """Column names for msm_ADDispersionLocal (AD Dispersion)."""
    MUID = "MUID"
    """ID"""
    ConnectionTypeNo = "ConnectionTypeNo"
    """Connection type"""
    LinkListFile = "LinkListFile"
    """Node List File"""
    LinkID = "LinkID"
    """Link ID"""
    StartChainage = "StartChainage"
    """Start chainage [m]"""
    EndChainage = "EndChainage"
    """End chainage [m]"""
    DispFactor = "DispFactor"
    """Dispersion factor"""
    Exponent = "Exponent"
    """Exponent"""
    MinDispCoef = "MinDispCoef"
    """Minimum dispersion coefficient [m^2/s]"""
    MaxDispCoef = "MaxDispCoef"
    """Maximum dispersion coefficient [m^2/s]"""

class msm_ADDispersionLocalTable(BaseTable):
    """Table for msm_ADDispersionLocal (AD Dispersion)."""
    
    @property
    def columns(self) -> msm_ADDispersionLocalTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = msm_ADDispersionLocalTableColumns(self)
        return self._columns