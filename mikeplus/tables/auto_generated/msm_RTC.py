from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class msm_RTCTableColumns(BaseColumns):
    """Column names for msm_RTC (Control rules)."""
    MUID = "MUID"
    """ID"""
    ApplyNo = "ApplyNo"
    """Apply"""
    StructureTypeNo = "StructureTypeNo"
    """Structure type"""
    PumpID = "PumpID"
    """Pump ID (CS)"""
    WeirID = "WeirID"
    """Weir ID (CS)"""
    ValveID = "ValveID"
    """Valve ID"""
    OrifriceGateID = "OrifriceGateID"
    """Orifice Gate ID"""
    OrificeWeirID = "OrificeWeirID"
    """Orifice Weir ID"""
    WeirRiverID = "WeirRiverID"
    """Weir ID (Rivers)"""
    CulvertRiverID = "CulvertRiverID"
    """Culvert ID"""
    DirectDischargeRiverID = "DirectDischargeRiverID"
    """Direct discharge ID"""
    DambreakID = "DambreakID"
    """Dambreak ID"""
    GateRiverID = "GateRiverID"
    """Gate ID"""
    PumpRiverID = "PumpRiverID"
    """Pump ID (Rivers)"""
    BridgeRiverID = "BridgeRiverID"
    """River bridge ID"""
    TabulatedID = "TabulatedID"
    """Tabulated ID"""
    Description = "Description"
    """Description"""

class msm_RTCTable(BaseTable):
    """Table for msm_RTC (Control rules)."""
    
    @property
    def columns(self) -> msm_RTCTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = msm_RTCTableColumns(self)
        return self._columns