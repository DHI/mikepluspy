from mikeplus.tables.base_geometry_table import BaseGeometryTable
from mikeplus.tables.base_geometry_table import BaseColumns

class mw_TurbineTableColumns(BaseColumns):
    """Column names for mw_Turbine (Turbines)."""
    MUID = "MUID"
    """ID"""
    FromNodeID = "FromNodeID"
    """From node"""
    ToNodeID = "ToNodeID"
    """To node"""
    TypeNo = "TypeNo"
    """Type"""
    Diameter = "Diameter"
    """Diameter [mm]"""
    HlossCurveID = "HlossCurveID"
    """Headloss curve"""
    RelativeSpeed = "RelativeSpeed"
    """Relative speed"""
    ZoneID = "ZoneID"
    """Zone ID"""
    StatusNo = "StatusNo"
    """Closed"""
    Enabled = "Enabled"
    """Is active"""
    EPrice = "EPrice"
    """Energy price"""
    EPatternID = "EPatternID"
    """Energy price pattern"""
    EfCurveID = "EfCurveID"
    """Efficiency curve"""
    DataSource = "DataSource"
    """Data source"""
    AssetName = "AssetName"
    """Asset ID"""
    Element_S = "Element_S"
    """Status"""
    StreetName = "StreetName"
    """Street name"""
    Description = "Description"
    """Description"""
    Note = "Note"
    """Note"""

class mw_TurbineTable(BaseGeometryTable):
    """Table for mw_Turbine (Turbines)."""
    
    @property
    def columns(self) -> mw_TurbineTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mw_TurbineTableColumns(self)
        return self._columns