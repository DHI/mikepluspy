from mikeplus.tables.base_geometry_table import BaseGeometryTable
from mikeplus.tables.base_geometry_table import BaseColumns

class msm_ValveTableColumns(BaseColumns):
    """Column names for msm_Valve (Valves)."""
    MUID = "MUID"
    """ID"""
    Enabled = "Enabled"
    """Apply"""
    FromNodeID = "FromNodeID"
    """From node"""
    ToNodeID = "ToNodeID"
    """To node"""
    InvertLevel = "InvertLevel"
    """Invert level [m]"""
    Area = "Area"
    """Flow area [m^2]"""
    Diameter = "Diameter"
    """Diameter [m]"""
    Opening = "Opening"
    """Valve opening [%]"""
    RatingCurveID = "RatingCurveID"
    """Rating Curve"""
    ControlTypeNo = "ControlTypeNo"
    """Controlled by control rules"""
    FlapNo = "FlapNo"
    """Non return flap"""
    MaxValveOpening = "MaxValveOpening"
    """Max opening [%]"""
    MinValveOpening = "MinValveOpening"
    """Min opening [%]"""
    MaxValveSpeed = "MaxValveSpeed"
    """Max speed [%/s]"""
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

class msm_ValveTable(BaseGeometryTable):
    """Table for msm_Valve (Valves)."""
    
    @property
    def columns(self) -> msm_ValveTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = msm_ValveTableColumns(self)
        return self._columns