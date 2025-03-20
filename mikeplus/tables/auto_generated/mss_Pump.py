from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class mss_PumpTableColumns(BaseColumns):
    """Column names for mss_Pump (Pumps)."""
    MUID = "MUID"
    Enabled = "Enabled"
    FromNodeID = "FromNodeID"
    ToNodeID = "ToNodeID"
    InitialStatusNo = "InitialStatusNo"
    IdealPumpNo = "IdealPumpNo"
    StartupDepth = "StartupDepth"
    ShutoffDepth = "ShutoffDepth"
    PumpCurveID = "PumpCurveID"
    DataSource = "DataSource"
    AssetName = "AssetName"
    Element_S = "Element_S"
    NetTypeNo = "NetTypeNo"
    Description = "Description"
    Tag = "Tag"

class mss_PumpTable(BaseTable):
    """Table for mss_Pump (Pumps)."""
    
    @property
    def columns(self) -> mss_PumpTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mss_PumpTableColumns(self)
        return self._columns