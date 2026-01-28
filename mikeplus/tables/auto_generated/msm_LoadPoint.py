from mikeplus.tables.base_geometry_table import BaseGeometryTable
from mikeplus.tables.base_geometry_table import BaseColumns

class msm_LoadPointTableColumns(BaseColumns):
    """Column names for msm_LoadPoint (Load points)."""
    MUID = "MUID"
    """ID"""
    Enabled = "Enabled"
    """Apply"""
    GeomX = "GeomX"
    """X [m]"""
    GeomY = "GeomY"
    """Y [m]"""
    LoadCategoryNo = "LoadCategoryNo"
    """Load category"""
    LoadFlow = "LoadFlow"
    """Flow [m^3/d]"""
    LoadUnits = "LoadUnits"
    """Person equivalents [()]"""
    LoadConnectionTypeNo = "LoadConnectionTypeNo"
    """Load connection type"""
    NodeID = "NodeID"
    """Node"""
    LinkID = "LinkID"
    """Link"""
    StartChainage = "StartChainage"
    """Start chainage [m]"""
    EndChainage = "EndChainage"
    """End chainage [m]"""
    Description = "Description"
    """Description"""
    DataSource = "DataSource"
    """Data source"""
    AssetName = "AssetName"
    """Asset ID"""
    LoadOwner = "LoadOwner"
    """Load owner"""
    LoadLocation = "LoadLocation"
    """Load location"""
    Date = "Date"
<<<<<<< HEAD
    """Date"""
=======
    EventID = "EventID"
>>>>>>> bc29183 (Update auto generated tables for MIKE+ 2026)

class msm_LoadPointTable(BaseGeometryTable):
    """Table for msm_LoadPoint (Load points)."""
    
    @property
    def columns(self) -> msm_LoadPointTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = msm_LoadPointTableColumns(self)
        return self._columns