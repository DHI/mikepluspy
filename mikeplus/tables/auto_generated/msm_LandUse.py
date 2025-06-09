from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class msm_LandUseTableColumns(BaseColumns):
    """Column names for msm_LandUse (Land uses)."""
    MUID = "MUID"
    """ID"""
    WetLossTypeNo = "WetLossTypeNo"
    """Include wetting loss"""
    WetLoss = "WetLoss"
    """Wet loss [mm]"""
    StorageLossTypeNo = "StorageLossTypeNo"
    """Include storage loss"""
    StorageLoss = "StorageLoss"
    """Storage loss [mm]"""
    FricTypeNo = "FricTypeNo"
    """Formulation"""
    Manning = "Manning"
    """Manning"""
    InfiltrationTypeNo = "InfiltrationTypeNo"
    """Infiltration type"""
    HortonMinRate = "HortonMinRate"
    """Minimum infiltration rate [mm/h]"""
    HortonMaxRate = "HortonMaxRate"
    """Maximum infiltration rate [mm/h]"""
    HortonWetExp = "HortonWetExp"
    """Exponent for wet conditions [/h]"""
    HortonDryExp = "HortonDryExp"
    """Exponent for dry conditions [/h]"""
    GAConduct = "GAConduct"
    """Saturated conductivity [mm/h]"""
    GAMaxMoisture = "GAMaxMoisture"
    """Max soil moisture deficit [%]"""
    GASuction = "GASuction"
    """Average capillary suction [mm]"""
    Description = "Description"
    """Description"""

class msm_LandUseTable(BaseTable):
    """Table for msm_LandUse (Land uses)."""
    
    @property
    def columns(self) -> msm_LandUseTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = msm_LandUseTableColumns(self)
        return self._columns