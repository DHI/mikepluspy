from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class msm_LandUseTableColumns(BaseColumns):
    """Column names for msm_LandUse (Land uses)."""
    MUID = "MUID"
    WetLossTypeNo = "WetLossTypeNo"
    WetLoss = "WetLoss"
    StorageLossTypeNo = "StorageLossTypeNo"
    StorageLoss = "StorageLoss"
    FricTypeNo = "FricTypeNo"
    Manning = "Manning"
    InfiltrationTypeNo = "InfiltrationTypeNo"
    HortonMinRate = "HortonMinRate"
    HortonMaxRate = "HortonMaxRate"
    HortonWetExp = "HortonWetExp"
    HortonDryExp = "HortonDryExp"
    GAConduct = "GAConduct"
    GAMaxMoisture = "GAMaxMoisture"
    GASuction = "GASuction"
    Description = "Description"

class msm_LandUseTable(BaseTable):
    """Table for msm_LandUse (Land uses)."""
    
    @property
    def columns(self) -> msm_LandUseTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = msm_LandUseTableColumns(self)
        return self._columns