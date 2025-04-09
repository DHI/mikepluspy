from mikeplus.tables.base_geometry_table import BaseGeometryTable
from mikeplus.tables.base_geometry_table import BaseColumns

class msm_NodeTableColumns(BaseColumns):
    """Column names for msm_Node (Nodes)."""
    MUID = "MUID"
    Enabled = "Enabled"
    GeomX = "GeomX"
    GeomY = "GeomY"
    TypeNo = "TypeNo"
    Diameter = "Diameter"
    GroundLevel = "GroundLevel"
    InvertLevel = "InvertLevel"
    GeometryID = "GeometryID"
    BranchID = "BranchID"
    BranchChainage = "BranchChainage"
    CoverTypeNo = "CoverTypeNo"
    BufferPressure = "BufferPressure"
    SpillCoef = "SpillCoef"
    ManholeCoverDisplacementID = "ManholeCoverDisplacementID"
    InletControlNo = "InletControlNo"
    MaxInlet = "MaxInlet"
    QHTypeNo = "QHTypeNo"
    OutletQHID = "OutletQHID"
    LossParID = "LossParID"
    LossParNo = "LossParNo"
    LossTypeNo = "LossTypeNo"
    LossCoeffKm = "LossCoeffKm"
    LossCoeffContraction = "LossCoeffContraction"
    LossCoeffTotal = "LossCoeffTotal"
    EffAreaNo = "EffAreaNo"
    PMTypeNo = "PMTypeNo"
    PMLevel = "PMLevel"
    InfiltrationNo = "InfiltrationNo"
    InitialWL = "InitialWL"
    InfConstValue = "InfConstValue"
    KfsSide = "KfsSide"
    PorosityFill = "PorosityFill"
    KfsBottomNo = "KfsBottomNo"
    KfsBottom = "KfsBottom"
    DataSource = "DataSource"
    AssetName = "AssetName"
    SubModelNo = "SubModelNo"
    CriticalLevel = "CriticalLevel"
    Element_S = "Element_S"
    NetTypeNo = "NetTypeNo"
    Description = "Description"

class msm_NodeTable(BaseGeometryTable):
    """Table for msm_Node (Nodes)."""
    
    @property
    def columns(self) -> msm_NodeTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = msm_NodeTableColumns(self)
        return self._columns