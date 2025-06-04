from mikeplus.tables.base_geometry_table import BaseGeometryTable
from mikeplus.tables.base_geometry_table import BaseColumns

class mss_OrificeTableColumns(BaseColumns):
    """Column names for mss_Orifice (Orifices)."""
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
    ShapeTypeNo = "ShapeTypeNo"
    """Orifice shape"""
    Height = "Height"
    """Opening [m]"""
    Width = "Width"
    """Width [m]"""
    CrestHeight = "CrestHeight"
    """Crest height [m]"""
    CrestElev = "CrestElev"
    """Crest elevation [m]"""
    TimeToOpenClose = "TimeToOpenClose"
    """Open/Close time [h]"""
    DischargeCoeff = "DischargeCoeff"
    """Discharge coeff."""
    FlapGateNo = "FlapGateNo"
    """Flap gate"""
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
    Tag = "Tag"
    """Tag"""

class mss_OrificeTable(BaseGeometryTable):
    """Table for mss_Orifice (Orifices)."""
    
    @property
    def columns(self) -> mss_OrificeTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mss_OrificeTableColumns(self)
        return self._columns