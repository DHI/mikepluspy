from mikeplus.tables.base_geometry_table import BaseGeometryTable
from mikeplus.tables.base_geometry_table import BaseColumns

class msm_CurbInletTableColumns(BaseColumns):
    """Column names for msm_CurbInlet (Curb inlets)."""
    MUID = "MUID"
    """ID"""
    Enabled = "Enabled"
    """Apply"""
    FromNodeID = "FromNodeID"
    """From node"""
    ToNodeID = "ToNodeID"
    """To node"""
    NoOfCurbInlets = "NoOfCurbInlets"
    """Number of inlets"""
    TypeNo = "TypeNo"
    """Type"""
    OriWidth = "OriWidth"
    """Width [m]"""
    OriHeight = "OriHeight"
    """Height [m]"""
    InvertLevel = "InvertLevel"
    """Invert level [m]"""
    CalculatedInvertLevel = "CalculatedInvertLevel"
    """Calculated inver level [m]"""
    Freeboard = "Freeboard"
    """Freeboard [m]"""
    SlopeNo = "SlopeNo"
    """Slope No"""
    Slope = "Slope"
    """Slope [%]"""
    CalculatedSlope = "CalculatedSlope"
    """Calculated slope [%]"""
    BlockageNo = "BlockageNo"
    """BlockageNo"""
    Blockage = "Blockage"
    """Blockage [%]"""
    DQrelationID = "DQrelationID"
    """DQ relation"""
    CaptureID = "CaptureID"
    """Capture ID"""
    Description = "Description"
    """Description"""
    Element_S = "Element_S"
    """Status"""
    NetTypeNo = "NetTypeNo"
    """Network type"""
    AssetName = "AssetName"
    """Asset ID"""
    DataSource = "DataSource"
    """Data source"""

class msm_CurbInletTable(BaseGeometryTable):
    """Table for msm_CurbInlet (Curb inlets)."""
    
    @property
    def columns(self) -> msm_CurbInletTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = msm_CurbInletTableColumns(self)
        return self._columns