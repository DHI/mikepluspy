from .FieldNameBase import DescriptionFieldBase, FieldNameBase
from System.Collections.Generic import Dictionary
from System import Object
from System import String

class TableBase:
    def __init__(self):
        self.tableName: str = ""
        self.values = Dictionary[String, Object]()
        self.values[FieldNameBase.MUID]: str = None
        self.values[FieldNameBase.AltID]: str = None
        self.values[FieldNameBase.Active]: int = None

class GeomBase(TableBase):
    def __init__(self):
        TableBase.__init__(self)
        self.values["GeometryWkt"]: str = None


class MsmNodeFields(DescriptionFieldBase):
    Enabled = "Enabled"
    TypeNo = "TypeNo"
    InvertLevel = "InvertLevel"
    GroundLevel = "GroundLevel"
    Diameter = "Diameter"
    CriticalLevel = "CriticalLevel"
    LossParID = "LossParID"
    GeometryID = "GeometryID"
    BranchID = "BranchID"
    BranchChainage = "BranchChainage"
    LossParNo = "LossParNo"
    LossTypeNo = "LossTypeNo"
    LossCoeffKm = "LossCoeffKm"
    LossCoeffContraction = "LossCoeffContraction"
    LossCoeffTotal = "LossCoeffTotal"
    EffAreaNo = "EffAreaNo"
    PMTypeNo = "PMTypeNo"
    PMLevel = "PMLevel"
    CoverTypeNo = "CoverTypeNo"
    BufferPressure = "BufferPressure"
    SpillCoef = "SpillCoef"
    QHTypeNo = "QHTypeNo"
    OutletQHID = "OutletQHID"
    InletControlNo = "InletControlNo"
    MaxInlet = "MaxInlet"
    SubModelNo = "SubModelNo"
    InfiltrationNo = "InfiltrationNo"
    InitialWL = "InitialWL"
    InfConstValue = "InfConstValue"
    KfsSide = "KfsSide"
    PorosityFill = "PorosityFill"
    KfsBottomNo = "KfsBottomNo"
    KfsBottom = "KfsBottom"

class MsmNode(GeomBase):
    def __init__(self):
        GeomBase.__init__(self)
        self.tableName = "msm_Node"
        self.values[MsmNodeFields.Enabled]: int = None
        self.values[MsmNodeFields.TypeNo]: int = None
        self.values[MsmNodeFields.InvertLevel]: float = None
        self.values[MsmNodeFields.GroundLevel]: float = None
        self.values[MsmNodeFields.Diameter]: float = None
        self.values[MsmNodeFields.BranchID]: str = None
        self.values[MsmNodeFields.BranchChainage]: float = None
        self.values[MsmNodeFields.CriticalLevel]: float = None
        self.values[MsmNodeFields.LossParID]: str = None
        self.values[MsmNodeFields.GeometryID]: str = None
        self.values[MsmNodeFields.LossParNo]: int = None
        self.values[MsmNodeFields.LossTypeNo]: int = None
        self.values[MsmNodeFields.LossCoeffKm]: float = None
        self.values[MsmNodeFields.LossCoeffContraction]: float = None
        self.values[MsmNodeFields.LossCoeffTotal]: float = None
        self.values[MsmNodeFields.EffAreaNo]: int = None
        self.values[MsmNodeFields.PMTypeNo]: int = None
        self.values[MsmNodeFields.PMLevel]: float = None
        self.values[MsmNodeFields.CoverTypeNo]: int = None
        self.values[MsmNodeFields.BufferPressure]: float = None
        self.values[MsmNodeFields.SpillCoef]: float = None
        self.values[MsmNodeFields.QHTypeNo]: int = None
        self.values[MsmNodeFields.OutletQHID]: str = None
        self.values[MsmNodeFields.InletControlNo]: int = None
        self.values[MsmNodeFields.MaxInlet]: float = None
        self.values[MsmNodeFields.InfiltrationNo]: int = None
        self.values[MsmNodeFields.InitialWL]: float = None
        self.values[MsmNodeFields.InfConstValue]: float = None
        self.values[MsmNodeFields.KfsSide]: float = None
        self.values[MsmNodeFields.PorosityFill]: float = None
        self.values[MsmNodeFields.KfsBottomNo]: int = None
        self.values[MsmNodeFields.KfsBottom]: float = None
        self.values[MsmNodeFields.DataSource]: str = None
        self.values[MsmNodeFields.AssetName]: str = None
        self.values[MsmNodeFields.SubModelNo]: int = None
        self.values[MsmNodeFields.Description]: str = None
        self.values[MsmNodeFields.Element_S]: int = None
        self.values[MsmNodeFields.NetTypeNo]: int = None
    
