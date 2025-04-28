from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class msm_RTCTableColumns(BaseColumns):
    """Column names for msm_RTC (Control rules)."""
    MUID = "MUID"
    ApplyNo = "ApplyNo"
    StructureTypeNo = "StructureTypeNo"
    PumpID = "PumpID"
    WeirID = "WeirID"
    ValveID = "ValveID"
    OrifriceGateID = "OrifriceGateID"
    OrificeWeirID = "OrificeWeirID"
    WeirRiverID = "WeirRiverID"
    CulvertRiverID = "CulvertRiverID"
    DirectDischargeRiverID = "DirectDischargeRiverID"
    DambreakID = "DambreakID"
    GateRiverID = "GateRiverID"
    PumpRiverID = "PumpRiverID"
    BridgeRiverID = "BridgeRiverID"
    TabulatedID = "TabulatedID"
    Description = "Description"

class msm_RTCTable(BaseTable):
    """Table for msm_RTC (Control rules)."""
    
    @property
    def columns(self) -> msm_RTCTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = msm_RTCTableColumns(self)
        return self._columns