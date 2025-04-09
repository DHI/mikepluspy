from mikeplus.tables.base_geometry_table import BaseGeometryTable
from mikeplus.tables.base_geometry_table import BaseColumns

class mw_TurbineTableColumns(BaseColumns):
    """Column names for mw_Turbine (Turbines)."""
    MUID = "MUID"
    FromNodeID = "FromNodeID"
    ToNodeID = "ToNodeID"
    TypeNo = "TypeNo"
    Diameter = "Diameter"
    HlossCurveID = "HlossCurveID"
    RelativeSpeed = "RelativeSpeed"
    ZoneID = "ZoneID"
    StatusNo = "StatusNo"
    Enabled = "Enabled"
    EPrice = "EPrice"
    EPatternID = "EPatternID"
    EfCurveID = "EfCurveID"
    DataSource = "DataSource"
    AssetName = "AssetName"
    Element_S = "Element_S"
    StreetName = "StreetName"
    Description = "Description"
    Note = "Note"

class mw_TurbineTable(BaseGeometryTable):
    """Table for mw_Turbine (Turbines)."""
    
    @property
    def columns(self) -> mw_TurbineTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mw_TurbineTableColumns(self)
        return self._columns