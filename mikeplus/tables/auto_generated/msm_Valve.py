from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class msm_ValveTableColumns(BaseColumns):
    """Column names for msm_Valve (Valves)."""
    MUID = "MUID"
    Enabled = "Enabled"
    FromNodeID = "FromNodeID"
    ToNodeID = "ToNodeID"
    InvertLevel = "InvertLevel"
    Area = "Area"
    Diameter = "Diameter"
    Opening = "Opening"
    RatingCurveID = "RatingCurveID"
    ControlTypeNo = "ControlTypeNo"
    FlapNo = "FlapNo"
    MaxValveOpening = "MaxValveOpening"
    MinValveOpening = "MinValveOpening"
    MaxValveSpeed = "MaxValveSpeed"
    DataSource = "DataSource"
    AssetName = "AssetName"
    Element_S = "Element_S"
    NetTypeNo = "NetTypeNo"
    Description = "Description"

class msm_ValveTable(BaseTable):
    """Table for msm_Valve (Valves)."""
    
    @property
    def columns(self) -> msm_ValveTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = msm_ValveTableColumns(self)
        return self._columns