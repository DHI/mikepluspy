from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class mw_WDODemandZonesTableColumns(BaseColumns):
    """Column names for mw_WDODemandZones (Demand zones)."""
    MUID = "MUID"
    ZoneID = "ZoneID"
    ID = "ID"
    Enabled = "Enabled"
    SensorID = "SensorID"
    SensorTable = "SensorTable"
    PatternID = "PatternID"
    Mult = "Mult"
    OffsetValue = "OffsetValue"
    Rematch = "Rematch"
    Comment = "Comment"
    LeakageNo = "LeakageNo"
    Population = "Population"
    ServiceConnections = "ServiceConnections"
    ServicePipesLength = "ServicePipesLength"
    MinNightUse = "MinNightUse"

class mw_WDODemandZonesTable(BaseTable):
    """Table for mw_WDODemandZones (Demand zones)."""
    
    @property
    def columns(self) -> mw_WDODemandZonesTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mw_WDODemandZonesTableColumns(self)
        return self._columns