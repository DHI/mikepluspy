from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class msm_HParSeasonalVariationTableColumns(BaseColumns):
    """Column names for msm_HParSeasonalVariation (Seasonal variation)."""
    MUID = "MUID"
    ParRdiiID = "ParRdiiID"
    MonthNo = "MonthNo"
    Month = "Month"
    Variation = "Variation"
    Abstraction = "Abstraction"
    DegreeDayCoeff = "DegreeDayCoeff"
    IrrigationCrop = "IrrigationCrop"
    Groundwater = "Groundwater"
    OverlandFlow = "OverlandFlow"
    Evaporation = "Evaporation"

class msm_HParSeasonalVariationTable(BaseTable):
    """Table for msm_HParSeasonalVariation (Seasonal variation)."""
    
    @property
    def columns(self) -> msm_HParSeasonalVariationTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = msm_HParSeasonalVariationTableColumns(self)
        return self._columns