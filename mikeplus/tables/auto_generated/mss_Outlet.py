from mikeplus.tables.base_geometry_table import BaseGeometryTable
from mikeplus.tables.base_geometry_table import BaseColumns

class mss_OutletTableColumns(BaseColumns):
    """Column names for mss_Outlet (Outlets)."""
    MUID = "MUID"
    """ID"""
    Enabled = "Enabled"
    """Apply"""
    FromNodeID = "FromNodeID"
    """From node"""
    ToNodeID = "ToNodeID"
    """To node"""
    TypeNo = "TypeNo"
    """Type"""
    Height = "Height"
    """Height [m]"""
    Qcoeff = "Qcoeff"
    """Coefficient"""
    QCurveID = "QCurveID"
    """Q-curve ID"""
    Qexpon = "Qexpon"
    """Exponent"""
    FlapGateNo = "FlapGateNo"
    """Flap gate"""
    DataSource = "DataSource"
    """Data source"""
    AssetName = "AssetName"
    """Asset ID"""
    Element_S = "Element_S"
    """Status"""
    NetTypeNo = "NetTypeNo"
    """Network type"""
    Description = "Description"
    """Description"""
    Tag = "Tag"
    """Tag"""

class mss_OutletTable(BaseGeometryTable):
    """Table for mss_Outlet (Outlets)."""
    
    @property
    def columns(self) -> mss_OutletTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mss_OutletTableColumns(self)
        return self._columns