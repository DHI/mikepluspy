from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class mss_OrificeTableColumns(BaseColumns):
    """Column names for mss_Orifice (Orifices)."""
    MUID = "MUID"
    Enabled = "Enabled"
    FromNodeID = "FromNodeID"
    ToNodeID = "ToNodeID"
    TypeNo = "TypeNo"
    ShapeTypeNo = "ShapeTypeNo"
    Height = "Height"
    Width = "Width"
    CrestHeight = "CrestHeight"
    CrestElev = "CrestElev"
    TimeToOpenClose = "TimeToOpenClose"
    DischargeCoeff = "DischargeCoeff"
    FlapGateNo = "FlapGateNo"
    DataSource = "DataSource"
    AssetName = "AssetName"
    Element_S = "Element_S"
    NetTypeNo = "NetTypeNo"
    Description = "Description"
    Tag = "Tag"

class mss_OrificeTable(BaseTable):
    """Table for mss_Orifice (Orifices)."""
    
    @property
    def columns(self) -> mss_OrificeTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mss_OrificeTableColumns(self)
        return self._columns