from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class msm_HParBTableColumns(BaseColumns):
    """Column names for msm_HParB (Parameters kinematic wave)."""
    MUID = "MUID"
    WetSteep = "WetSteep"
    WetFlat = "WetFlat"
    WetSmall = "WetSmall"
    WetMedium = "WetMedium"
    WetLarge = "WetLarge"
    StorageFlat = "StorageFlat"
    StorageSmall = "StorageSmall"
    StorageMedium = "StorageMedium"
    StorageLarge = "StorageLarge"
    InfMaxSmall = "InfMaxSmall"
    InfMaxMedium = "InfMaxMedium"
    InfMaxLarge = "InfMaxLarge"
    InfMinSmall = "InfMinSmall"
    InfMinMedium = "InfMinMedium"
    InfMinLarge = "InfMinLarge"
    InfExpWetSmall = "InfExpWetSmall"
    InfExpWetMedium = "InfExpWetMedium"
    InfExpWetLarge = "InfExpWetLarge"
    InfExpDrySmall = "InfExpDrySmall"
    InfExpDryMedium = "InfExpDryMedium"
    InfExpDryLarge = "InfExpDryLarge"
    FricTypeNo = "FricTypeNo"
    ManningSteep = "ManningSteep"
    ManningFlat = "ManningFlat"
    ManningSmall = "ManningSmall"
    ManningMedium = "ManningMedium"
    ManningLarge = "ManningLarge"

class msm_HParBTable(BaseTable):
    """Table for msm_HParB (Parameters kinematic wave)."""
    
    @property
    def columns(self) -> msm_HParBTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = msm_HParBTableColumns(self)
        return self._columns