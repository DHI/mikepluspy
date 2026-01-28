from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class msm_STTableColumns(BaseColumns):
    """Column names for msm_ST (General parameters)."""
    MUID = "MUID"
    """ID"""
    AnalysisNo = "AnalysisNo"
    """Analysis type"""
    ModelTypeNo = "ModelTypeNo"
    """Transport model"""
    NbFractions = "NbFractions"
    """Number of fractions"""
    IncludeMorphUpdate = "IncludeMorphUpdate"
    """Include morphological update"""
    IniManningTypeNo = "IniManningTypeNo"
    """Manning Type"""
    IniManning = "IniManning"
    """Manning value"""
    IniSediDepth = "IniSediDepth"
    """Sediment depth [m]"""
    LimitPassiveDepthNo = "LimitPassiveDepthNo"
    """Limited passive layer depth"""
    PassiveDepth = "PassiveDepth"
    """Passive layer depth [m]"""
    DensityFricSedi = "DensityFricSedi"
    """Relative density [()]"""
    STPorosity = "STPorosity"
    """Porosity of deposits [()]"""
    KinViscosity = "KinViscosity"
    """Kinematic viscosity [m^2/s]"""
    d90d50 = "d90d50"
    """d90/d50 [()]"""
    MaxErosionConc = "MaxErosionConc"
    """Maximum concentration allowed due to erosion [g/m^3]"""
    SkinFrictModelNo = "SkinFrictModelNo"
    """Skin friction model"""
    UseEgiazaroff = "UseEgiazaroff"
    """Use Egiazaroff hiding function"""

class msm_STTable(BaseTable):
    """Table for msm_ST (General parameters)."""
    
    @property
    def columns(self) -> msm_STTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = msm_STTableColumns(self)
        return self._columns