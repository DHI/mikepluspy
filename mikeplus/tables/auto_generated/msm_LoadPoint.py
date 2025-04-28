from mikeplus.tables.base_geometry_table import BaseGeometryTable
from mikeplus.tables.base_geometry_table import BaseColumns

class msm_LoadPointTableColumns(BaseColumns):
    """Column names for msm_LoadPoint (Load points)."""
    MUID = "MUID"
    Enabled = "Enabled"
    GeomX = "GeomX"
    GeomY = "GeomY"
    LoadCategoryNo = "LoadCategoryNo"
    LoadFlow = "LoadFlow"
    LoadUnits = "LoadUnits"
    LoadConnectionTypeNo = "LoadConnectionTypeNo"
    NodeID = "NodeID"
    LinkID = "LinkID"
    StartChainage = "StartChainage"
    EndChainage = "EndChainage"
    Description = "Description"
    DataSource = "DataSource"
    AssetName = "AssetName"
    LoadOwner = "LoadOwner"
    LoadLocation = "LoadLocation"
    Date = "Date"

class msm_LoadPointTable(BaseGeometryTable):
    """Table for msm_LoadPoint (Load points)."""
    
    @property
    def columns(self) -> msm_LoadPointTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = msm_LoadPointTableColumns(self)
        return self._columns