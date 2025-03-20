from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class msm_STTableColumns(BaseColumns):
    """Column names for msm_ST (General parameters)."""
    MUID = "MUID"
    AnalysisNo = "AnalysisNo"
    ModelTypeNo = "ModelTypeNo"
    NbFractions = "NbFractions"
    IncludeMorphUpdate = "IncludeMorphUpdate"
    IniManningTypeNo = "IniManningTypeNo"
    IniManning = "IniManning"
    IniSediDepth = "IniSediDepth"
    LimitPassiveDepthNo = "LimitPassiveDepthNo"
    PassiveDepth = "PassiveDepth"
    DensityFricSedi = "DensityFricSedi"
    STPorosity = "STPorosity"
    KinViscosity = "KinViscosity"
    d90d50 = "d90d50"
    MaxErosionConc = "MaxErosionConc"
    SkinFrictModelNo = "SkinFrictModelNo"
    UseEgiazaroff = "UseEgiazaroff"

class msm_STTable(BaseTable):
    """Table for msm_ST (General parameters)."""
    
    @property
    def columns(self) -> msm_STTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = msm_STTableColumns(self)
        return self._columns