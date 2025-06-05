from mikeplus.tables.base_geometry_table import BaseGeometryTable
from mikeplus.tables.base_geometry_table import BaseColumns

class msm_OrificeTableColumns(BaseColumns):
    """Column names for msm_Orifice (Orifices)."""
    MUID = "MUID"
    """ID"""
    Enabled = "Enabled"
    """Apply"""
    FromNodeID = "FromNodeID"
    """From node"""
    ToNodeID = "ToNodeID"
    """To node"""
    TypeNo = "TypeNo"
    """Type"""
    InvertLevel = "InvertLevel"
    """Invert level [m]"""
    DischargeCoeff = "DischargeCoeff"
    """Discharge Coeff."""
    Diameter = "Diameter"
    """Diameter [m]"""
    CrsID = "CrsID"
    """Shape"""
    Height = "Height"
    """Height [m]"""
    Width = "Width"
    """Width [m]"""
    ControlTypeNo = "ControlTypeNo"
    """Controlled by control rules"""
    FlapNo = "FlapNo"
    """Non return flap"""
    BladeTypeNo = "BladeTypeNo"
    """Blade type"""
    InitialLevel = "InitialLevel"
    """Initial level [m]"""
    MaxGateLevel = "MaxGateLevel"
    """Max. level [m]"""
    MinGateLevel = "MinGateLevel"
    """Min. level [m]"""
    MaxGateLevelIncreaseSpeed = "MaxGateLevelIncreaseSpeed"
    """Max. speed up [m/s]"""
    MaxGateLevelDecreaseSpeed = "MaxGateLevelDecreaseSpeed"
    """Max. speed down [m/s]"""
    DataSource = "DataSource"
    """Data source"""
    AssetName = "AssetName"
    """Asset ID"""
    Element_S = "Element_S"
    """Status"""
    NetTypeNo = "NetTypeNo"
    """Network type"""
    Description = "Description"
    """Description"""

class msm_OrificeTable(BaseGeometryTable):
    """Table for msm_Orifice (Orifices)."""
    
    @property
    def columns(self) -> msm_OrificeTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = msm_OrificeTableColumns(self)
        return self._columns