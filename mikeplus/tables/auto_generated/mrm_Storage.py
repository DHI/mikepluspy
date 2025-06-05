from mikeplus.tables.base_geometry_table import BaseGeometryTable
from mikeplus.tables.base_geometry_table import BaseColumns

class mrm_StorageTableColumns(BaseColumns):
    """Column names for mrm_Storage (Storages)."""
    MUID = "MUID"
    """ID"""
    Enabled = "Enabled"
    """Apply"""
    GeomInteriorPointX = "GeomInteriorPointX"
    """X coordinate [m]"""
    GeomInteriorPointY = "GeomInteriorPointY"
    """Y coordinate [m]"""
    StorageTypeNo = "StorageTypeNo"
    """Storage capacity type"""
    BottomArea = "BottomArea"
    """Area at bottom elevation [m^2]"""
    GeomTableID = "GeomTableID"
    """Geometry table"""
    DataSource = "DataSource"
    """Data source"""
    AssetName = "AssetName"
    """Asset ID"""
    Element_S = "Element_S"
    """Element status"""
    NetTypeNo = "NetTypeNo"
    """Network type"""
    Description = "Description"
    """Description"""

class mrm_StorageTable(BaseGeometryTable):
    """Table for mrm_Storage (Storages)."""
    
    @property
    def columns(self) -> mrm_StorageTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mrm_StorageTableColumns(self)
        return self._columns