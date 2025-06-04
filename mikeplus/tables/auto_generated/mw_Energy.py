from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class mw_EnergyTableColumns(BaseColumns):
    """Column names for mw_Energy (Cost analysis)."""
    MUID = "MUID"
    """MUID"""
    Price = "Price"
    """Global price"""
    PricePatID = "PricePatID"
    """Price pattern ID"""
    DemCharge = "DemCharge"
    """Demand charge"""
    Effic = "Effic"
    """Pump efficiency [%]"""
    PumpCurrency = "PumpCurrency"
    """Currency"""
    CarbonFactor = "CarbonFactor"
    """Carbon emission factor [kg/kWh]"""
    TurbinePrice = "TurbinePrice"
    """Global price"""
    TurbineEffic = "TurbineEffic"
    """Turbine efficiency [%]"""
    TurbinePriPatID = "TurbinePriPatID"
    """Price pattern ID"""
    TurbineCurrency = "TurbineCurrency"
    """Currency"""
    OtherUnit = "OtherUnit"
    """OtherUnit"""

class mw_EnergyTable(BaseTable):
    """Table for mw_Energy (Cost analysis)."""
    
    @property
    def columns(self) -> mw_EnergyTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mw_EnergyTableColumns(self)
        return self._columns