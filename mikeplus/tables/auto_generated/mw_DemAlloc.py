from mikeplus.tables.base_geometry_table import BaseGeometryTable
from mikeplus.tables.base_geometry_table import BaseColumns

class mw_DemAllocTableColumns(BaseColumns):
    """Column names for mw_DemAlloc (Demand allocations)."""
    MUID = "MUID"
    GeomX = "GeomX"
    GeomY = "GeomY"
    ConnectionTypeNo = "ConnectionTypeNo"
    JunctionID = "JunctionID"
    PipeID = "PipeID"
    Pattern = "Pattern"
    Dem_category = "Dem_category"
    Dem_Location = "Dem_Location"
    Demand = "Demand"
    EstHeight = "EstHeight"
    Elevation = "Elevation"
    AssetName = "AssetName"
    Dem_Owner = "Dem_Owner"
    Description = "Description"

class mw_DemAllocTable(BaseGeometryTable):
    """Table for mw_DemAlloc (Demand allocations)."""
    
    @property
    def columns(self) -> mw_DemAllocTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mw_DemAllocTableColumns(self)
        return self._columns