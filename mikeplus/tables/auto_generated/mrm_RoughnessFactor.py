from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class mrm_RoughnessFactorTableColumns(BaseColumns):
    """Column names for mrm_RoughnessFactor (Roughness factor)."""
    MUID = "MUID"
    """ID"""
    RiverID = "RiverID"
    """River ID"""
    FromChainage = "FromChainage"
    """From chainage [m]"""
    ToChainage = "ToChainage"
    """To chainage [m]"""
    FactorTypeNo = "FactorTypeNo"
    """Factor type"""
    Factor = "Factor"
    """Factor [()]"""
    FilePath = "FilePath"
    """File"""
    ItemID = "ItemID"
    """Item ID"""

class mrm_RoughnessFactorTable(BaseTable):
    """Table for mrm_RoughnessFactor (Roughness factor)."""
    
    @property
    def columns(self) -> mrm_RoughnessFactorTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mrm_RoughnessFactorTableColumns(self)
        return self._columns