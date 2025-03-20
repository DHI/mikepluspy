from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class mw_TankTableColumns(BaseColumns):
    """Column names for mw_Tank (Tanks)."""
    MUID = "MUID"
    GeomX = "GeomX"
    GeomY = "GeomY"
    HGLTypeNo = "HGLTypeNo"
    Elev = "Elev"
    ZoneID = "ZoneID"
    Enabled = "Enabled"
    TypeNo = "TypeNo"
    VolCurveID = "VolCurveID"
    Width = "Width"
    Length = "Length"
    Diameter = "Diameter"
    MinLevel = "MinLevel"
    MinLevel_HGL = "MinLevel_HGL"
    InitLevel = "InitLevel"
    InitLevel_HGL = "InitLevel_HGL"
    MaxLevel = "MaxLevel"
    MaxLevel_HGL = "MaxLevel_HGL"
    MinVol = "MinVol"
    OperationalVolume = "OperationalVolume"
    OverflowNo = "OverflowNo"
    HGLLevelTypeNo = "HGLLevelTypeNo"
    HGL = "HGL"
    PatternID = "PatternID"
    Z = "Z"
    ReactionCoefficient = "ReactionCoefficient"
    MixModelNo = "MixModelNo"
    ComVol = "ComVol"
    Init_Quality_Concentration = "Init_Quality_Concentration"
    Init_Quality_Percentage = "Init_Quality_Percentage"
    Init_Quality_Hour = "Init_Quality_Hour"
    DataSource = "DataSource"
    AssetName = "AssetName"
    Element_S = "Element_S"
    Description = "Description"
    Note = "Note"

class mw_TankTable(BaseTable):
    """Table for mw_Tank (Tanks)."""
    
    @property
    def columns(self) -> mw_TankTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mw_TankTableColumns(self)
        return self._columns