from mikeplus.tables.base_geometry_table import BaseGeometryTable
from mikeplus.tables.base_geometry_table import BaseColumns

class mrm_GateTableColumns(BaseColumns):
    """Column names for mrm_Gate (Gates)."""
    MUID = "MUID"
    Enabled = "Enabled"
    RiverID = "RiverID"
    Chainage = "Chainage"
    TypeNo = "TypeNo"
    GateNo = "GateNo"
    Width = "Width"
    MaxLevel = "MaxLevel"
    SillLevel = "SillLevel"
    Height = "Height"
    Trunnion = "Trunnion"
    Radius = "Radius"
    HorizOffset = "HorizOffset"
    MaxSpeed = "MaxSpeed"
    InitialLevel = "InitialLevel"
    ApplyFactorNo = "ApplyFactorNo"
    FactorValue = "FactorValue"
    PosInflow = "PosInflow"
    PosOutflow = "PosOutflow"
    PosFreeflow = "PosFreeflow"
    NegInflow = "NegInflow"
    NegOutflow = "NegOutflow"
    NegFreeflow = "NegFreeflow"
    ContracCoef = "ContracCoef"
    HeadLossCmTypeNo = "HeadLossCmTypeNo"
    RadialFactor = "RadialFactor"
    RadialCoef = "RadialCoef"
    RadialExp = "RadialExp"
    RadialTranBottom = "RadialTranBottom"
    RadialTranDepth = "RadialTranDepth"
    Sluice_a_ContSub = "Sluice_a_ContSub"
    Sluice_a_ContFree = "Sluice_a_ContFree"
    Sluice_a_UncSub = "Sluice_a_UncSub"
    Sluice_a_UncFree = "Sluice_a_UncFree"
    Sluice_b_ContSub = "Sluice_b_ContSub"
    Sluice_b_ContFree = "Sluice_b_ContFree"
    Sluice_b_UncSub = "Sluice_b_UncSub"
    Sluice_High_ContSub = "Sluice_High_ContSub"
    Sluice_High_ContFree = "Sluice_High_ContFree"
    Sluice_High_UncSub = "Sluice_High_UncSub"
    Sluice_Low_ContSub = "Sluice_Low_ContSub"
    Sluice_Low_ContFree = "Sluice_Low_ContFree"
    Sluice_Low_UncSub = "Sluice_Low_UncSub"
    DataSource = "DataSource"
    Element_S = "Element_S"
    Description = "Description"

class mrm_GateTable(BaseGeometryTable):
    """Table for mrm_Gate (Gates)."""
    
    @property
    def columns(self) -> mrm_GateTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mrm_GateTableColumns(self)
        return self._columns