from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class mss_WeirTableColumns(BaseColumns):
    """Column names for mss_Weir (Weirs)."""
    MUID = "MUID"
    Enabled = "Enabled"
    FromNodeID = "FromNodeID"
    ToNodeID = "ToNodeID"
    TypeNo = "TypeNo"
    InvertLevel = "InvertLevel"
    Height = "Height"
    Length = "Length"
    SideSlope = "SideSlope"
    CrestHeight = "CrestHeight"
    DischargeCoeff = "DischargeCoeff"
    DischargeCoeff_RoadWay = "DischargeCoeff_RoadWay"
    DischargeCoeff_SideFlow = "DischargeCoeff_SideFlow"
    DischargeCoeff_V = "DischargeCoeff_V"
    FlapGateNo = "FlapGateNo"
    CanSurchargeNo = "CanSurchargeNo"
    NoEndContractions = "NoEndContractions"
    CoeffCurveID = "CoeffCurveID"
    Cd2 = "Cd2"
    RoadWidth = "RoadWidth"
    RoadSurf = "RoadSurf"
    DataSource = "DataSource"
    AssetName = "AssetName"
    Element_S = "Element_S"
    NetTypeNo = "NetTypeNo"
    Description = "Description"
    Tag = "Tag"

class mss_WeirTable(BaseTable):
    """Table for mss_Weir (Weirs)."""
    
    @property
    def columns(self) -> mss_WeirTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mss_WeirTableColumns(self)
        return self._columns