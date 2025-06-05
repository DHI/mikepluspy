from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class msm_STFractionTableColumns(BaseColumns):
    """Column names for msm_STFraction (Sediment fractions)."""
    MUID = "MUID"
    """ID"""
    TransportTypeNo = "TransportTypeNo"
    """Sediment type"""
    GrainSize = "GrainSize"
    """Grain size [mm]"""
    FallVelModeNo = "FallVelModeNo"
    """Fall velocity mode"""
    FallVelocity = "FallVelocity"
    """Fall velocity value [cm/s]"""
    ErodabilityCoef = "ErodabilityCoef"
    """Erosion coefficient [g/m^2/s]"""
    CritTauDepo = "CritTauDepo"
    """Deposition shear stress limit [N/m^2]"""
    CritTauEro = "CritTauEro"
    """Erosion shear stress limit [N/m^2]"""

class msm_STFractionTable(BaseTable):
    """Table for msm_STFraction (Sediment fractions)."""
    
    @property
    def columns(self) -> msm_STFractionTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = msm_STFractionTableColumns(self)
        return self._columns