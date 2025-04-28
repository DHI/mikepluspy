from mikeplus.tables.base_geometry_table import BaseGeometryTable
from mikeplus.tables.base_geometry_table import BaseColumns

class mss_OutletTableColumns(BaseColumns):
    """Column names for mss_Outlet (Outlets)."""
    MUID = "MUID"
    Enabled = "Enabled"
    FromNodeID = "FromNodeID"
    ToNodeID = "ToNodeID"
    TypeNo = "TypeNo"
    Height = "Height"
    Qcoeff = "Qcoeff"
    QCurveID = "QCurveID"
    Qexpon = "Qexpon"
    FlapGateNo = "FlapGateNo"
    DataSource = "DataSource"
    AssetName = "AssetName"
    Element_S = "Element_S"
    NetTypeNo = "NetTypeNo"
    Description = "Description"
    Tag = "Tag"

class mss_OutletTable(BaseGeometryTable):
    """Table for mss_Outlet (Outlets)."""
    
    @property
    def columns(self) -> mss_OutletTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mss_OutletTableColumns(self)
        return self._columns