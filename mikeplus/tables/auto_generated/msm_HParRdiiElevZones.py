from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class msm_HParRdiiElevZonesTableColumns(BaseColumns):
    """Column names for msm_HParRdiiElevZones (Elevation zones)."""
    MUID = "MUID"
    """ID"""
    ParRdiiID = "ParRdiiID"
    """ParRdiiID"""
    Sqn = "Sqn"
    """Zone"""
    Elevation = "Elevation"
    """Elevation [m]"""
    Area = "Area"
    """Area [km^2]"""
    MinStorage = "MinStorage"
    """Min storage for full coverage [mm]"""
    MaxStorage = "MaxStorage"
    """Max storage in zone [mm]"""
    MaxWaterRetain = "MaxWaterRetain"
    """Max water retained in snow [%]"""
    DryTempCorrection = "DryTempCorrection"
    """Dry temperature correction [deg C]"""
    WetTempCorrection = "WetTempCorrection"
    """Wet temperature correction [deg C]"""
    PrecipTempCorrection = "PrecipTempCorrection"
    """Precipitation correction [%]"""
    SnowStorage = "SnowStorage"
    """Snow storage [mm]"""
    WaterInSnow = "WaterInSnow"
    """Water in snow [mm]"""

class msm_HParRdiiElevZonesTable(BaseTable):
    """Table for msm_HParRdiiElevZones (Elevation zones)."""
    
    @property
    def columns(self) -> msm_HParRdiiElevZonesTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = msm_HParRdiiElevZonesTableColumns(self)
        return self._columns