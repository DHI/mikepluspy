from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class msm_PumpTableColumns(BaseColumns):
    """Column names for msm_Pump (Pumps)."""
    MUID = "MUID"
    Enabled = "Enabled"
    FromNodeID = "FromNodeID"
    ToNodeID = "ToNodeID"
    CapTypeNo = "CapTypeNo"
    StartLevel = "StartLevel"
    StopLevel = "StopLevel"
    AccTime = "AccTime"
    DecTime = "DecTime"
    DutyPoint = "DutyPoint"
    QMaxSetID = "QMaxSetID"
    QMinSetID = "QMinSetID"
    OffSet1 = "OffSet1"
    OffSet2 = "OffSet2"
    RegNo = "RegNo"
    ControlTypeNo = "ControlTypeNo"
    WetWellSetPoint = "WetWellSetPoint"
    SpeedNo = "SpeedNo"
    MaxStartLevel = "MaxStartLevel"
    MinStopLevel = "MinStopLevel"
    MinTimeOn = "MinTimeOn"
    MinTimeOff = "MinTimeOff"
    DataSource = "DataSource"
    AssetName = "AssetName"
    Element_S = "Element_S"
    NetTypeNo = "NetTypeNo"
    Description = "Description"

class msm_PumpTable(BaseTable):
    """Table for msm_Pump (Pumps)."""
    
    @property
    def columns(self) -> msm_PumpTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = msm_PumpTableColumns(self)
        return self._columns