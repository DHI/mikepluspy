from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class mss_GroundwaterTableColumns(BaseColumns):
    """Column names for mss_Groundwater (Ground water)."""
    MUID = "MUID"
    """ID"""
    SubCatchID = "SubCatchID"
    """Catchment ID"""
    AquiferID = "AquiferID"
    """Aquifer ID"""
    NodeID = "NodeID"
    """Node ID"""
    SurfElev = "SurfElev"
    """Catchment surface elev. [m]"""
    A1 = "A1"
    """GW flow coefficient (A1) [m^2/s/ha]"""
    B1 = "B1"
    """GW flow exponent (B1)"""
    A2 = "A2"
    """Surface water flow coefficient (A2) [m^2/s/ha]"""
    B2 = "B2"
    """Surface water flow exponent (B2)"""
    A3 = "A3"
    """GW interaction coefficient (A3) [m/s/ha]"""
    Description = "Description"
    """Description"""
    LateralFlowNo = "LateralFlowNo"
    """Custom lateral flow equation"""
    DeepFlowNo = "DeepFlowNo"
    """Custom deep flow equation"""
    LateralFlowEquation = "LateralFlowEquation"
    """Lateral flow equation"""
    DeepFlowEquation = "DeepFlowEquation"
    """Deep flow equation"""
    Hsw = "Hsw"
    """Surface water height (Hsw) [m]"""
    Hcb = "Hcb"
    """Channel bottom height (Hcb) [m]"""
    BottomElev = "BottomElev"
    """Bottom elevation [m]"""
    WTElev = "WTElev"
    """Water table elevation [m]"""
    UZoneMoisture = "UZoneMoisture"
    """Unsat. zone moisture"""

class mss_GroundwaterTable(BaseTable):
    """Table for mss_Groundwater (Ground water)."""
    
    @property
    def columns(self) -> mss_GroundwaterTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mss_GroundwaterTableColumns(self)
        return self._columns