from mikeplus.tables.base_geometry_table import BaseGeometryTable
from mikeplus.tables.base_geometry_table import BaseColumns

class m_StationTableColumns(BaseColumns):
    """Column names for m_Station (Measurement stations)."""
    MUID = "MUID"
    """ID"""
    GeomX = "GeomX"
    """X [m]"""
    GeomY = "GeomY"
    """Y [m]"""
    LocationType = "LocationType"
    """Model element type"""
    LocationID = "LocationID"
    """Model element ID"""
    Chainage = "Chainage"
    """Chainage"""
    ChainageValue = "ChainageValue"
    """Chainage [m]"""
    DataSource = "DataSource"
    """Data source"""
    AssetName = "AssetName"
    """Asset ID"""
    BottomLevel = "BottomLevel"
    """Bottom level [m]"""
    Element_S = "Element_S"
    """Status"""
    SubModelNo = "SubModelNo"
    """Model"""
    NetTypeNo = "NetTypeNo"
    """Network type"""
    Description = "Description"
    """Description"""

class m_StationTable(BaseGeometryTable):
    """Table for m_Station (Measurement stations)."""
    
    @property
    def columns(self) -> m_StationTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = m_StationTableColumns(self)
        return self._columns