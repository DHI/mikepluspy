from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class mss_LinkTableColumns(BaseColumns):
    """Column names for mss_Link (Conduits)."""
    MUID = "MUID"
    FromNodeID = "FromNodeID"
    ToNodeID = "ToNodeID"
    ShapeTypeNo = "ShapeTypeNo"
    Length = "Length"
    GeometricLength = "GeometricLength"
    InletInvert = "InletInvert"
    OutletInvert = "OutletInvert"
    InletInvert_C = "InletInvert_C"
    OutletInvert_C = "OutletInvert_C"
    InletInvert_Offset = "InletInvert_Offset"
    OutletInvert_Offset = "OutletInvert_Offset"
    Depth = "Depth"
    SedimentDepth = "SedimentDepth"
    BottomWidth = "BottomWidth"
    TopWidth = "TopWidth"
    LeftSideSlope = "LeftSideSlope"
    TriangleHeight = "TriangleHeight"
    BottomRadius = "BottomRadius"
    Barrels = "Barrels"
    RightSideSlope = "RightSideSlope"
    Slope = "Slope"
    Exponent = "Exponent"
    SidewallsNo = "SidewallsNo"
    TransectID = "TransectID"
    ShapeID = "ShapeID"
    FricNo = "FricNo"
    MaterialID = "MaterialID"
    Roughness = "Roughness"
    AvgLossCoeff = "AvgLossCoeff"
    ForceMainRoughnessHW = "ForceMainRoughnessHW"
    ForceMainRoughnessDW = "ForceMainRoughnessDW"
    EntryLossCoeff = "EntryLossCoeff"
    ExitLossCoeff = "ExitLossCoeff"
    FlapGateNo = "FlapGateNo"
    InitialFlow = "InitialFlow"
    MaxFlow = "MaxFlow"
    CulvertCode = "CulvertCode"
    SeepageRate = "SeepageRate"
    AssetName = "AssetName"
    DataSource = "DataSource"
    NetTypeNo = "NetTypeNo"
    Description = "Description"
    Tag = "Tag"
    Enabled = "Enabled"
    Element_S = "Element_S"

class mss_LinkTable(BaseTable):
    """Table for mss_Link (Conduits)."""
    
    @property
    def columns(self) -> mss_LinkTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mss_LinkTableColumns(self)
        return self._columns