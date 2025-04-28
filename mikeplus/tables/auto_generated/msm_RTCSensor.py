from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class msm_RTCSensorTableColumns(BaseColumns):
    """Column names for msm_RTCSensor (Sensors)."""
    MUID = "MUID"
    Sqn = "Sqn"
    TypeNo = "TypeNo"
    ComponentID = "ComponentID"
    LocationNo = "LocationNo"
    NodeLocationID = "NodeLocationID"
    LinkLocationID = "LinkLocationID"
    StorageLocationID = "StorageLocationID"
    WeirLocationID = "WeirLocationID"
    OrificeLocationID = "OrificeLocationID"
    ValveLocationID = "ValveLocationID"
    PumpLocationID = "PumpLocationID"
    ActionID = "ActionID"
    RiverStructureTypeNo = "RiverStructureTypeNo"
    RiverStructureID = "RiverStructureID"
    RiverLocationID = "RiverLocationID"
    UpStreamChainage = "UpStreamChainage"
    DownStreamChainage = "DownStreamChainage"
    GateLocationID = "GateLocationID"
    WeirRiverLocationID = "WeirRiverLocationID"
    CulvertRiverLocationID = "CulvertRiverLocationID"
    DirectDischargeRiverLocationID = "DirectDischargeRiverLocationID"
    PumpRiverLocationID = "PumpRiverLocationID"
    BridgeRiverLocationID = "BridgeRiverLocationID"
    TabulatedRiverLocationID = "TabulatedRiverLocationID"
    DambreakRiverLocationID = "DambreakRiverLocationID"
    TSFileName = "TSFileName"
    TSItemName = "TSItemName"
    Chainage = "Chainage"
    Expression = "Expression"
    Description = "Description"

class msm_RTCSensorTable(BaseTable):
    """Table for msm_RTCSensor (Sensors)."""
    
    @property
    def columns(self) -> msm_RTCSensorTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = msm_RTCSensorTableColumns(self)
        return self._columns