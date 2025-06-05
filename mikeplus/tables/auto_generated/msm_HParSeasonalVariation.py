from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class msm_HParSeasonalVariationTableColumns(BaseColumns):
    """Column names for msm_HParSeasonalVariation (Seasonal variation)."""
    MUID = "MUID"
    """MUID"""
    ParRdiiID = "ParRdiiID"
    """ParRdiiID"""
    MonthNo = "MonthNo"
    """Month"""
    Month = "Month"
    """Month"""
    Variation = "Variation"
    """Variation of groundwater maximum water depth [()]"""
    Abstraction = "Abstraction"
    """Abstraction [mm/mth]"""
    DegreeDayCoeff = "DegreeDayCoeff"
    """Degree-day coefficient for snowmelt [mm/deg C/d]"""
    IrrigationCrop = "IrrigationCrop"
    """Irrigation crop coefficient [()]"""
    Groundwater = "Groundwater"
    """Irrigation operational and conveyance losses in percent of abstracted water / Groundwater [%]"""
    OverlandFlow = "OverlandFlow"
    """Irrigation operational and conveyance losses in percent of abstracted water / Overland flow [%]"""
    Evaporation = "Evaporation"
    """Irrigation operational and conveyance losses in percent of abstracted water / Evaporation [%]"""

class msm_HParSeasonalVariationTable(BaseTable):
    """Table for msm_HParSeasonalVariation (Seasonal variation)."""
    
    @property
    def columns(self) -> msm_HParSeasonalVariationTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = msm_HParSeasonalVariationTableColumns(self)
        return self._columns