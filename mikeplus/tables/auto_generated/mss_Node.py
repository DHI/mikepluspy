from mikeplus.tables.base_geometry_table import BaseGeometryTable
from mikeplus.tables.base_geometry_table import BaseColumns

class mss_NodeTableColumns(BaseColumns):
    """Column names for mss_Node (Nodes)."""
    MUID = "MUID"
    GeomX = "GeomX"
    GeomY = "GeomY"
    TypeNo = "TypeNo"
    Enabled = "Enabled"
    Einv = "Einv"
    GroundLevel = "GroundLevel"
    Dmax = "Dmax"
    D0 = "D0"
    Dsur = "Dsur"
    Apond = "Apond"
    GeomTypeNo = "GeomTypeNo"
    GeomCoeff = "GeomCoeff"
    GeomConst = "GeomConst"
    GeomExponent = "GeomExponent"
    GeomID = "GeomID"
    Fevap = "Fevap"
    StorageInfiltrationNo = "StorageInfiltrationNo"
    StorageSuctionHead = "StorageSuctionHead"
    StorageConductivity = "StorageConductivity"
    StorageInitialDeficit = "StorageInitialDeficit"
    FlapGateTypeNo = "FlapGateTypeNo"
    FixedStage = "FixedStage"
    TideGateID = "TideGateID"
    TideGateTSID = "TideGateTSID"
    FlapGateNo = "FlapGateNo"
    RouteTo = "RouteTo"
    DividerTypeNo = "DividerTypeNo"
    CutoffFlow = "CutoffFlow"
    DivertedFlowID = "DivertedFlowID"
    DivertedMinFlow = "DivertedMinFlow"
    DivertedMaxDepth = "DivertedMaxDepth"
    DivertionCoeff = "DivertionCoeff"
    LinkID = "LinkID"
    Description = "Description"
    DataSource = "DataSource"
    AssetName = "AssetName"
    Element_S = "Element_S"
    NetTypeNo = "NetTypeNo"
    Tag = "Tag"

class mss_NodeTable(BaseGeometryTable):
    """Table for mss_Node (Nodes)."""
    
    @property
    def columns(self) -> mss_NodeTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mss_NodeTableColumns(self)
        return self._columns