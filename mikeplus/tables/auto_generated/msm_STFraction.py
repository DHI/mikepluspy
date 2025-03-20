from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class msm_STFractionTableColumns(BaseColumns):
    """Column names for msm_STFraction (Sediment fractions)."""
    MUID = "MUID"
    TransportTypeNo = "TransportTypeNo"
    GrainSize = "GrainSize"
    FallVelModeNo = "FallVelModeNo"
    FallVelocity = "FallVelocity"
    ErodabilityCoef = "ErodabilityCoef"
    CritTauDepo = "CritTauDepo"
    CritTauEro = "CritTauEro"

class msm_STFractionTable(BaseTable):
    """Table for msm_STFraction (Sediment fractions)."""
    
    @property
    def columns(self) -> msm_STFractionTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = msm_STFractionTableColumns(self)
        return self._columns