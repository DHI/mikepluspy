from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class mw_EnergyTableColumns(BaseColumns):
    """Column names for mw_Energy (Cost analysis)."""
    MUID = "MUID"
    Price = "Price"
    PricePatID = "PricePatID"
    DemCharge = "DemCharge"
    Effic = "Effic"
    PumpCurrency = "PumpCurrency"
    CarbonFactor = "CarbonFactor"
    TurbinePrice = "TurbinePrice"
    TurbineEffic = "TurbineEffic"
    TurbinePriPatID = "TurbinePriPatID"
    TurbineCurrency = "TurbineCurrency"
    OtherUnit = "OtherUnit"

class mw_EnergyTable(BaseTable):
    """Table for mw_Energy (Cost analysis)."""
    
    @property
    def columns(self) -> mw_EnergyTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mw_EnergyTableColumns(self)
        return self._columns