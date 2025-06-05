from mikeplus.tables.base_geometry_table import BaseGeometryTable
from mikeplus.tables.base_geometry_table import BaseColumns

class msm_WeirTableColumns(BaseColumns):
    """Column names for msm_Weir (Weirs)."""
    MUID = "MUID"
    """ID"""
    Enabled = "Enabled"
    """Apply"""
    FromNodeID = "FromNodeID"
    """From node"""
    ToNodeID = "ToNodeID"
    """To node"""
    TypeNo = "TypeNo"
    """Computational method"""
    CrestLevel = "CrestLevel"
    """Crest level [m]"""
    Coeff = "Coeff"
    """Discharge coeff."""
    CrestWidth = "CrestWidth"
    """Crest width [m]"""
    AngleNo = "AngleNo"
    """Orientation"""
    QHID = "QHID"
    """Q-H table"""
    WeirCrestID = "WeirCrestID"
    """Crest shape"""
    ControlTypeNo = "ControlTypeNo"
    """Controlled by control rules"""
    FlapNo = "FlapNo"
    """Non return flap"""
    MaxCrestLevel = "MaxCrestLevel"
    """Max. level [m]"""
    MinCrestLevel = "MinCrestLevel"
    """Min. level [m]"""
    MaxCrestLevelIncreaseSpeed = "MaxCrestLevelIncreaseSpeed"
    """Max. speed up [m/s]"""
    MaxCrestLevelDecreaseSpeed = "MaxCrestLevelDecreaseSpeed"
    """Max. speed down [m/s]"""
    InitialLevel = "InitialLevel"
    """Initial level [m]"""
    SHAPE_Length = "SHAPE_Length"
    """Shape length [m]"""
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

class msm_WeirTable(BaseGeometryTable):
    """Table for msm_Weir (Weirs)."""
    
    @property
    def columns(self) -> msm_WeirTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = msm_WeirTableColumns(self)
        return self._columns