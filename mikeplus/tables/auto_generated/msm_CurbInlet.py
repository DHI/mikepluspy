from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class msm_CurbInletTableColumns(BaseColumns):
    """Column names for msm_CurbInlet (Curb inlets)."""
    MUID = "MUID"
    Enabled = "Enabled"
    FromNodeID = "FromNodeID"
    ToNodeID = "ToNodeID"
    NoOfCurbInlets = "NoOfCurbInlets"
    TypeNo = "TypeNo"
    OriWidth = "OriWidth"
    OriHeight = "OriHeight"
    InvertLevel = "InvertLevel"
    CalculatedInvertLevel = "CalculatedInvertLevel"
    Freeboard = "Freeboard"
    SlopeNo = "SlopeNo"
    Slope = "Slope"
    CalculatedSlope = "CalculatedSlope"
    BlockageNo = "BlockageNo"
    Blockage = "Blockage"
    DQrelationID = "DQrelationID"
    CaptureID = "CaptureID"
    Description = "Description"
    Element_S = "Element_S"
    NetTypeNo = "NetTypeNo"
    AssetName = "AssetName"
    DataSource = "DataSource"

class msm_CurbInletTable(BaseTable):
    """Table for msm_CurbInlet (Curb inlets)."""
    
    @property
    def columns(self) -> msm_CurbInletTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = msm_CurbInletTableColumns(self)
        return self._columns