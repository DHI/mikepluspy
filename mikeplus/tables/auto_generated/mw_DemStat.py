from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class mw_DemStatTableColumns(BaseColumns):
    """Column names for mw_DemStat (Statistics and redistribution)."""
    MUID = "MUID"
    RecTypeNo = "RecTypeNo"
    ZoneID = "ZoneID"
    Category = "Category"
    ZoneType = "ZoneType"
    MinDemand = "MinDemand"
    MaxDemand = "MaxDemand"
    AvgDemand = "AvgDemand"
    SumDemand = "SumDemand"
    NewAvgDemand = "NewAvgDemand"
    NewSumDemand = "NewSumDemand"
    Sqn = "Sqn"

class mw_DemStatTable(BaseTable):
    """Table for mw_DemStat (Statistics and redistribution)."""
    
    @property
    def columns(self) -> mw_DemStatTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mw_DemStatTableColumns(self)
        return self._columns