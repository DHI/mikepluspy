from mikeplus.tables.base_geometry_table import BaseGeometryTable
from mikeplus.tables.base_geometry_table import BaseColumns

class mrm_StorageTableColumns(BaseColumns):
    """Column names for mrm_Storage (Storages)."""
    MUID = "MUID"
    Enabled = "Enabled"
    GeomInteriorPointX = "GeomInteriorPointX"
    GeomInteriorPointY = "GeomInteriorPointY"
    StorageTypeNo = "StorageTypeNo"
    BottomArea = "BottomArea"
    GeomTableID = "GeomTableID"
    DataSource = "DataSource"
    AssetName = "AssetName"
    Element_S = "Element_S"
    NetTypeNo = "NetTypeNo"
    Description = "Description"

class mrm_StorageTable(BaseGeometryTable):
    """Table for mrm_Storage (Storages)."""
    
    @property
    def columns(self) -> mrm_StorageTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mrm_StorageTableColumns(self)
        return self._columns