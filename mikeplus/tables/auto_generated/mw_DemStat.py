from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class mw_DemStatTableColumns(BaseColumns):
    """Column names for mw_DemStat (Statistics and redistribution)."""
    MUID = "MUID"
    """MUID"""
    RecTypeNo = "RecTypeNo"
    """TypeN"""
    ZoneID = "ZoneID"
    """Zone ID"""
    Category = "Category"
    """Category"""
    ZoneType = "ZoneType"
    """Zone type"""
    MinDemand = "MinDemand"
    """MinDemand [m^3/s]"""
    MaxDemand = "MaxDemand"
    """MaxDemand [m^3/s]"""
    AvgDemand = "AvgDemand"
    """AvgDemand [m^3/s]"""
    SumDemand = "SumDemand"
    """SumDemand [m^3]"""
    NewAvgDemand = "NewAvgDemand"
    """NewAvgDemand [m^3/s]"""
    NewSumDemand = "NewSumDemand"
    """NewSumDemand [m^3]"""
    Sqn = "Sqn"
    """Sqn"""

class mw_DemStatTable(BaseTable):
    """Table for mw_DemStat (Statistics and redistribution)."""
    
    @property
    def columns(self) -> mw_DemStatTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mw_DemStatTableColumns(self)
        return self._columns