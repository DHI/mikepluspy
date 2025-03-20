from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class mw_ValveTableColumns(BaseColumns):
    """Column names for mw_Valve (Valves)."""
    MUID = "MUID"
    FromNodeID = "FromNodeID"
    ToNodeID = "ToNodeID"
    TypeNo = "TypeNo"
    SettingNo = "SettingNo"
    Setting = "Setting"
    Diameter = "Diameter"
    LossCoeff = "LossCoeff"
    StatusNo = "StatusNo"
    HLCurveID = "HLCurveID"
    Elev = "Elev"
    ZoneID = "ZoneID"
    Enabled = "Enabled"
    DataSource = "DataSource"
    AssetName = "AssetName"
    Element_S = "Element_S"
    StreetName = "StreetName"
    Description = "Description"
    Note = "Note"
    CDate = "CDate"
    LCoeff = "LCoeff"
    OperCurveID = "OperCurveID"
    ValveCurveID = "ValveCurveID"
    FullStrokeTime = "FullStrokeTime"
    LevelControlEnabled = "LevelControlEnabled"
    TankID = "TankID"
    LevelOpen = "LevelOpen"
    LevelClose = "LevelClose"

class mw_ValveTable(BaseTable):
    """Table for mw_Valve (Valves)."""
    
    @property
    def columns(self) -> mw_ValveTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mw_ValveTableColumns(self)
        return self._columns