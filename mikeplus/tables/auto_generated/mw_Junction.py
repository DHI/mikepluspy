from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class mw_JunctionTableColumns(BaseColumns):
    """Column names for mw_Junction (Junctions)."""
    MUID = "MUID"
    GeomX = "GeomX"
    GeomY = "GeomY"
    TypeNo = "TypeNo"
    Elev = "Elev"
    EstHeight = "EstHeight"
    Z = "Z"
    DemCoeff = "DemCoeff"
    MinPre = "MinPre"
    ZoneID = "ZoneID"
    Enabled = "Enabled"
    Em_FlowCoeff = "Em_FlowCoeff"
    Init_Quality_Concentration = "Init_Quality_Concentration"
    Init_Quality_Percentage = "Init_Quality_Percentage"
    Init_Quality_Hour = "Init_Quality_Hour"
    AV_Diameter = "AV_Diameter"
    AV_Kapa = "AV_Kapa"
    AV_ValveCurveID = "AV_ValveCurveID"
    DataSource = "DataSource"
    AssetName = "AssetName"
    Element_S = "Element_S"
    Description = "Description"
    Note = "Note"
    FFPREREQ = "FFPREREQ"
    FFFLOREQ = "FFFLOREQ"
    gF = "gF"
    smF = "smF"

class mw_JunctionTable(BaseTable):
    """Table for mw_Junction (Junctions)."""
    
    @property
    def columns(self) -> mw_JunctionTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mw_JunctionTableColumns(self)
        return self._columns