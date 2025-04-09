from mikeplus.tables.base_geometry_table import BaseGeometryTable
from mikeplus.tables.base_geometry_table import BaseColumns

class m_StationTableColumns(BaseColumns):
    """Column names for m_Station (Measurement stations)."""
    MUID = "MUID"
    GeomX = "GeomX"
    GeomY = "GeomY"
    LocationType = "LocationType"
    LocationID = "LocationID"
    Chainage = "Chainage"
    ChainageValue = "ChainageValue"
    DataSource = "DataSource"
    AssetName = "AssetName"
    BottomLevel = "BottomLevel"
    Element_S = "Element_S"
    SubModelNo = "SubModelNo"
    NetTypeNo = "NetTypeNo"
    Description = "Description"

class m_StationTable(BaseGeometryTable):
    """Table for m_Station (Measurement stations)."""
    
    @property
    def columns(self) -> m_StationTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = m_StationTableColumns(self)
        return self._columns