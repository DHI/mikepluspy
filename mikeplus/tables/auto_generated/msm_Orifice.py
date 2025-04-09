from mikeplus.tables.base_geometry_table import BaseGeometryTable
from mikeplus.tables.base_geometry_table import BaseColumns

class msm_OrificeTableColumns(BaseColumns):
    """Column names for msm_Orifice (Orifices)."""
    MUID = "MUID"
    Enabled = "Enabled"
    FromNodeID = "FromNodeID"
    ToNodeID = "ToNodeID"
    TypeNo = "TypeNo"
    InvertLevel = "InvertLevel"
    DischargeCoeff = "DischargeCoeff"
    Diameter = "Diameter"
    CrsID = "CrsID"
    Height = "Height"
    Width = "Width"
    ControlTypeNo = "ControlTypeNo"
    FlapNo = "FlapNo"
    BladeTypeNo = "BladeTypeNo"
    InitialLevel = "InitialLevel"
    MaxGateLevel = "MaxGateLevel"
    MinGateLevel = "MinGateLevel"
    MaxGateLevelIncreaseSpeed = "MaxGateLevelIncreaseSpeed"
    MaxGateLevelDecreaseSpeed = "MaxGateLevelDecreaseSpeed"
    DataSource = "DataSource"
    AssetName = "AssetName"
    Element_S = "Element_S"
    NetTypeNo = "NetTypeNo"
    Description = "Description"

class msm_OrificeTable(BaseGeometryTable):
    """Table for msm_Orifice (Orifices)."""
    
    @property
    def columns(self) -> msm_OrificeTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = msm_OrificeTableColumns(self)
        return self._columns