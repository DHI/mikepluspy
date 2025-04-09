from mikeplus.tables.base_geometry_table import BaseGeometryTable
from mikeplus.tables.base_geometry_table import BaseColumns

class mw_PumpTableColumns(BaseColumns):
    """Column names for mw_Pump (Pumps)."""
    MUID = "MUID"
    FromNodeID = "FromNodeID"
    ToNodeID = "ToNodeID"
    TypeNo = "TypeNo"
    CurveTypeNo = "CurveTypeNo"
    QHCurveID = "QHCurveID"
    Setting = "Setting"
    PatternID = "PatternID"
    Elev = "Elev"
    ZoneID = "ZoneID"
    StatusNo = "StatusNo"
    Enabled = "Enabled"
    Par2 = "Par2"
    Par3 = "Par3"
    Par1 = "Par1"
    Par4 = "Par4"
    Par5 = "Par5"
    Par6 = "Par6"
    VSD_TypeNo = "VSD_TypeNo"
    VSD_Node = "VSD_Node"
    VSD_Link = "VSD_Link"
    VSD_CtrlLevelTypeNo = "VSD_CtrlLevelTypeNo"
    VSD_Pressure = "VSD_Pressure"
    VSD_HGL = "VSD_HGL"
    VSD_MinSpeed = "VSD_MinSpeed"
    VSD_MaxSpeed = "VSD_MaxSpeed"
    VSD_CtrlFlow = "VSD_CtrlFlow"
    VSD_Curve = "VSD_Curve"
    EPrice = "EPrice"
    EPatternID = "EPatternID"
    EfCurveID = "EfCurveID"
    P_ScheduleNo = "P_ScheduleNo"
    P_ScheduleID = "P_ScheduleID"
    P_Speed = "P_Speed"
    P_IW = "P_IW"
    P_PTorqueID = "P_PTorqueID"
    C_MTorqueID = "C_MTorqueID"
    P_TTripoff = "P_TTripoff"
    p_TStartup = "p_TStartup"
    DataSource = "DataSource"
    AssetName = "AssetName"
    Element_S = "Element_S"
    StreetName = "StreetName"
    Description = "Description"
    Note = "Note"
    CDate = "CDate"

class mw_PumpTable(BaseGeometryTable):
    """Table for mw_Pump (Pumps)."""
    
    @property
    def columns(self) -> mw_PumpTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mw_PumpTableColumns(self)
        return self._columns