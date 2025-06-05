from mikeplus.tables.base_geometry_table import BaseGeometryTable
from mikeplus.tables.base_geometry_table import BaseColumns

class mss_PumpTableColumns(BaseColumns):
    """Column names for mss_Pump (Pumps)."""
    MUID = "MUID"
    """ID"""
    Enabled = "Enabled"
    """Apply"""
    FromNodeID = "FromNodeID"
    """From node"""
    ToNodeID = "ToNodeID"
    """To node"""
    InitialStatusNo = "InitialStatusNo"
    """Initial status ON"""
    IdealPumpNo = "IdealPumpNo"
    """Ideal pump"""
    StartupDepth = "StartupDepth"
    """Startup depth [m]"""
    ShutoffDepth = "ShutoffDepth"
    """Shutoff depth [m]"""
    PumpCurveID = "PumpCurveID"
    """Pump curve ID"""
    DataSource = "DataSource"
    """Data source"""
    AssetName = "AssetName"
    """Asset ID"""
    Element_S = "Element_S"
    """Status"""
    NetTypeNo = "NetTypeNo"
    """Network type"""
    Description = "Description"
    """Description"""
    Tag = "Tag"
    """Tag"""

class mss_PumpTable(BaseGeometryTable):
    """Table for mss_Pump (Pumps)."""
    
    @property
    def columns(self) -> mss_PumpTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mss_PumpTableColumns(self)
        return self._columns