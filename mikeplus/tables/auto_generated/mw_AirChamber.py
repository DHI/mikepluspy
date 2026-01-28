from mikeplus.tables.base_node_table import BaseNodeTable
from mikeplus.tables.base_node_table import BaseColumns

class mw_AirChamberTableColumns(BaseColumns):
    """Column names for mw_AirChamber (Air-chambers)."""
    MUID = "MUID"
    """ID"""
    GeomX = "GeomX"
    """X [m]"""
    GeomY = "GeomY"
    """Y [m]"""
    Elev = "Elev"
    """Base elevation [m]"""
    ZoneID = "ZoneID"
    """Zone ID"""
    Enabled = "Enabled"
    """Is active"""
    av_kapa = "av_kapa"
<<<<<<< HEAD
    """Polytropical expansion"""
=======
    InletFlowCoeff = "InletFlowCoeff"
    OutletFlowCoeff = "OutletFlowCoeff"
>>>>>>> bc29183 (Update auto generated tables for MIKE+ 2026)
    TypeNo = "TypeNo"
    """Tank Geometry"""
    VolCurveID = "VolCurveID"
    """Tank geometry ID"""
    Width = "Width"
    """Width [m]"""
    Length = "Length"
    """Length [m]"""
    Diameter = "Diameter"
    """Diameter [m]"""
    MinLevel = "MinLevel"
    """Minimum level [m]"""
    MinLevel_HGL = "MinLevel_HGL"
    """- [m]"""
    InitLevel = "InitLevel"
    """Initial level [m]"""
    InitLevel_HGL = "InitLevel_HGL"
    """ -  [m]"""
    MaxLevel = "MaxLevel"
    """Maximum level [m]"""
    MaxLevel_HGL = "MaxLevel_HGL"
    """ -  [m]"""
    OperationalVolume = "OperationalVolume"
    """Operational volume [m^3]"""
    DataSource = "DataSource"
    """Data source"""
    AssetName = "AssetName"
    """Asset ID"""
    Element_S = "Element_S"
    """Status"""
    Description = "Description"
    """Description"""
    Note = "Note"
    """Note"""

class mw_AirChamberTable(BaseNodeTable):
    """Table for mw_AirChamber (Air-chambers)."""
    
    @property
    def columns(self) -> mw_AirChamberTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mw_AirChamberTableColumns(self)
        return self._columns