from mikeplus.tables.base_geometry_table import BaseGeometryTable
from mikeplus.tables.base_geometry_table import BaseColumns

class mw_DemAllocTableColumns(BaseColumns):
    """Column names for mw_DemAlloc (Demand allocations)."""
    MUID = "MUID"
    """ID"""
    GeomX = "GeomX"
    """X [m]"""
    GeomY = "GeomY"
    """Y [m]"""
    ConnectionTypeNo = "ConnectionTypeNo"
    """Allocation type"""
    JunctionID = "JunctionID"
    """Junction ID"""
    PipeID = "PipeID"
    """Pipe ID"""
    Pattern = "Pattern"
    """Demand pattern"""
    Dem_category = "Dem_category"
    """Demand category"""
    Dem_Location = "Dem_Location"
    """Address"""
    Demand = "Demand"
    """Demand [m^3/s]"""
    EstHeight = "EstHeight"
    """Estate height [m]"""
    Elevation = "Elevation"
    """Elevation [m]"""
    AssetName = "AssetName"
    """Asset Name"""
    Dem_Owner = "Dem_Owner"
    """Owner"""
    Description = "Description"
    """Description"""

class mw_DemAllocTable(BaseGeometryTable):
    """Table for mw_DemAlloc (Demand allocations)."""
    
    @property
    def columns(self) -> mw_DemAllocTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mw_DemAllocTableColumns(self)
        return self._columns