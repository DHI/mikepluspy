from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class mrm_SHECouplingsTableColumns(BaseColumns):
    """Column names for mrm_SHECouplings (Groundwater couplings)."""
    MUID = "MUID"
    ApplyNo = "ApplyNo"
    TypeNo = "TypeNo"
    RiverID = "RiverID"
    FromChainage = "FromChainage"
    ToChainage = "ToChainage"
    WeirCoef = "WeirCoef"
    WeirExpCoeff = "WeirExpCoeff"
    MinHeight = "MinHeight"
    OverbankSpillNo = "OverbankSpillNo"
    MinFlowArea = "MinFlowArea"
    ConductanceNo = "ConductanceNo"
    LeakageCoef = "LeakageCoef"
    LineResExcNo = "LineResExcNo"
    FloodAreaNo = "FloodAreaNo"
    FloodCode = "FloodCode"
    BedTopoNo = "BedTopoNo"
    BedLeakageNo = "BedLeakageNo"
    NodeID = "NodeID"
    LinkID = "LinkID"
    CoupleToOverlandFlowNo = "CoupleToOverlandFlowNo"
    ExchangeCoeff = "ExchangeCoeff"
    ExchangeExponent = "ExchangeExponent"
    CoupleToDrainageNo = "CoupleToDrainageNo"
    GridCode = "GridCode"
    CoupleToSaturatedZoneNo = "CoupleToSaturatedZoneNo"
    ExchangeTypeNo = "ExchangeTypeNo"
    GroutingCoeff = "GroutingCoeff"
    GroutingThickness = "GroutingThickness"
    CoupleToSaturatedZoneDrainageNo = "CoupleToSaturatedZoneDrainageNo"
    NetworkGridCode = "NetworkGridCode"

class mrm_SHECouplingsTable(BaseTable):
    """Table for mrm_SHECouplings (Groundwater couplings)."""
    
    @property
    def columns(self) -> mrm_SHECouplingsTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mrm_SHECouplingsTableColumns(self)
        return self._columns