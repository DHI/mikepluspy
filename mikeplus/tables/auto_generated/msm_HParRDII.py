from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class msm_HParRDIITableColumns(BaseColumns):
    """Column names for msm_HParRDII (Parameters RDI)."""
    MUID = "MUID"
    Umax = "Umax"
    Lmax = "Lmax"
    Cqof = "Cqof"
    GwCarea = "GwCarea"
    Ck = "Ck"
    Ck2TypeNo = "Ck2TypeNo"
    Ck2 = "Ck2"
    Ckif = "Ckif"
    Ckbf = "Ckbf"
    Tof = "Tof"
    Tif = "Tif"
    Tg = "Tg"
    InitU = "InitU"
    InitL = "InitL"
    InitGwl = "InitGwl"
    InitOf = "InitOf"
    InitIf = "InitIf"
    InitBF = "InitBF"
    InitBFLow = "InitBFLow"
    SnowStorage = "SnowStorage"
    GwSy = "GwSy"
    GwLmin = "GwLmin"
    GWLbf0 = "GWLbf0"
    GWLfl1 = "GWLfl1"
    LowerBFTypeNo = "LowerBFTypeNo"
    CQLow = "CQLow"
    CKLow = "CKLow"
    GWSeasonTypeNo = "GWSeasonTypeNo"
    GWLBFMin = "GWLBFMin"
    AbstractionTypeNo = "AbstractionTypeNo"
    AbstractionSourceTypeNo = "AbstractionSourceTypeNo"
    SnowmeltNo = "SnowmeltNo"
    T0 = "T0"
    SnowmeltC = "SnowmeltC"
    SnowmeltCTypeNo = "SnowmeltCTypeNo"
    RadiationTypeNo = "RadiationTypeNo"
    RadiationCoef = "RadiationCoef"
    RainfallCoefTypeNo = "RainfallCoefTypeNo"
    RainfallCoef = "RainfallCoef"
    ElevZonesNo = "ElevZonesNo"
    CorrectDryTempNo = "CorrectDryTempNo"
    CorrectDryTempCorrection = "CorrectDryTempCorrection"
    CorrectWetTempNo = "CorrectWetTempNo"
    CorrectWetTempCorrection = "CorrectWetTempCorrection"
    TempStationElev = "TempStationElev"
    CorrectPrecNo = "CorrectPrecNo"
    CorrectPrecCorrection = "CorrectPrecCorrection"
    PrecStationElev = "PrecStationElev"
    IncludeIrrigationNo = "IncludeIrrigationNo"
    K0inf = "K0inf"
    PClgw = "PClgw"
    PClr = "PClr"
    PCexr = "PCexr"
    RiverID = "RiverID"
    Chainage = "Chainage"
    IncludeSeasonalVarNo = "IncludeSeasonalVarNo"
    ObjFuncWaterBalanceNo = "ObjFuncWaterBalanceNo"
    ObjFuncRmsErrorNo = "ObjFuncRmsErrorNo"
    ObjFuncPeakflowNo = "ObjFuncPeakflowNo"
    ObjFuncPeakflow = "ObjFuncPeakflow"
    ObjFuncLowflowNo = "ObjFuncLowflowNo"
    ObjFuncLowflow = "ObjFuncLowflow"
    ObjFuncMaxEvaluation = "ObjFuncMaxEvaluation"
    ObjFuncInitDaysExcluded = "ObjFuncInitDaysExcluded"

class msm_HParRDIITable(BaseTable):
    """Table for msm_HParRDII (Parameters RDI)."""
    
    @property
    def columns(self) -> msm_HParRDIITableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = msm_HParRDIITableColumns(self)
        return self._columns