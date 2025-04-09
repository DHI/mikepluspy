from mikeplus.tables.base_geometry_table import BaseGeometryTable
from mikeplus.tables.base_geometry_table import BaseColumns

class mw_AirChamberTableColumns(BaseColumns):
    """Column names for mw_AirChamber (Air-chambers)."""
    MUID = "MUID"
    GeomX = "GeomX"
    GeomY = "GeomY"
    Elev = "Elev"
    ZoneID = "ZoneID"
    Enabled = "Enabled"
    av_kapa = "av_kapa"
    TypeNo = "TypeNo"
    VolCurveID = "VolCurveID"
    Width = "Width"
    Length = "Length"
    Diameter = "Diameter"
    MinLevel = "MinLevel"
    MinLevel_HGL = "MinLevel_HGL"
    InitLevel = "InitLevel"
    InitLevel_HGL = "InitLevel_HGL"
    MaxLevel = "MaxLevel"
    MaxLevel_HGL = "MaxLevel_HGL"
    OperationalVolume = "OperationalVolume"
    DataSource = "DataSource"
    AssetName = "AssetName"
    Element_S = "Element_S"
    Description = "Description"
    Note = "Note"

class mw_AirChamberTable(BaseGeometryTable):
    """Table for mw_AirChamber (Air-chambers)."""
    
    @property
    def columns(self) -> mw_AirChamberTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mw_AirChamberTableColumns(self)
        return self._columns