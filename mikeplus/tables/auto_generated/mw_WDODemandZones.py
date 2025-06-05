from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class mw_WDODemandZonesTableColumns(BaseColumns):
    """Column names for mw_WDODemandZones (Demand zones)."""
    MUID = "MUID"
    """ID"""
    ZoneID = "ZoneID"
    """Zone ID"""
    ID = "ID"
    """ID"""
    Enabled = "Enabled"
    """Is active"""
    SensorID = "SensorID"
    """Sensor ID"""
    SensorTable = "SensorTable"
    """Sensor table"""
    PatternID = "PatternID"
    """Pattern ID"""
    Mult = "Mult"
    """Multiplier [()]"""
    OffsetValue = "OffsetValue"
    """Offset [()]"""
    Rematch = "Rematch"
    """Adjust total zone demand to account for additional demands"""
    Comment = "Comment"
    """Description"""
    LeakageNo = "LeakageNo"
    """Include leakage processing"""
    Population = "Population"
    """Population [person]"""
    ServiceConnections = "ServiceConnections"
    """Service connections"""
    ServicePipesLength = "ServicePipesLength"
    """Service pipes length [m]"""
    MinNightUse = "MinNightUse"
    """Minimum night use per person"""

class mw_WDODemandZonesTable(BaseTable):
    """Table for mw_WDODemandZones (Demand zones)."""
    
    @property
    def columns(self) -> mw_WDODemandZonesTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mw_WDODemandZonesTableColumns(self)
        return self._columns