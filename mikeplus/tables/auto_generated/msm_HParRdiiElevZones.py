from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class msm_HParRdiiElevZonesTableColumns(BaseColumns):
    """Column names for msm_HParRdiiElevZones (Elevation zones)."""
    MUID = "MUID"
    ParRdiiID = "ParRdiiID"
    Sqn = "Sqn"
    Elevation = "Elevation"
    Area = "Area"
    MinStorage = "MinStorage"
    MaxStorage = "MaxStorage"
    MaxWaterRetain = "MaxWaterRetain"
    DryTempCorrection = "DryTempCorrection"
    WetTempCorrection = "WetTempCorrection"
    PrecipTempCorrection = "PrecipTempCorrection"
    SnowStorage = "SnowStorage"
    WaterInSnow = "WaterInSnow"

class msm_HParRdiiElevZonesTable(BaseTable):
    """Table for msm_HParRdiiElevZones (Elevation zones)."""
    
    @property
    def columns(self) -> msm_HParRdiiElevZonesTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = msm_HParRdiiElevZonesTableColumns(self)
        return self._columns