from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class mrm_RoughnessFactorTableColumns(BaseColumns):
    """Column names for mrm_RoughnessFactor (Roughness factor)."""
    MUID = "MUID"
    RiverID = "RiverID"
    FromChainage = "FromChainage"
    ToChainage = "ToChainage"
    FactorTypeNo = "FactorTypeNo"
    Factor = "Factor"
    FilePath = "FilePath"
    ItemID = "ItemID"

class mrm_RoughnessFactorTable(BaseTable):
    """Table for mrm_RoughnessFactor (Roughness factor)."""
    
    @property
    def columns(self) -> mrm_RoughnessFactorTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mrm_RoughnessFactorTableColumns(self)
        return self._columns