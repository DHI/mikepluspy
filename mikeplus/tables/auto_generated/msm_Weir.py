from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class msm_WeirTableColumns(BaseColumns):
    """Column names for msm_Weir (Weirs)."""
    MUID = "MUID"
    Enabled = "Enabled"
    FromNodeID = "FromNodeID"
    ToNodeID = "ToNodeID"
    TypeNo = "TypeNo"
    CrestLevel = "CrestLevel"
    Coeff = "Coeff"
    CrestWidth = "CrestWidth"
    AngleNo = "AngleNo"
    QHID = "QHID"
    WeirCrestID = "WeirCrestID"
    ControlTypeNo = "ControlTypeNo"
    FlapNo = "FlapNo"
    MaxCrestLevel = "MaxCrestLevel"
    MinCrestLevel = "MinCrestLevel"
    MaxCrestLevelIncreaseSpeed = "MaxCrestLevelIncreaseSpeed"
    MaxCrestLevelDecreaseSpeed = "MaxCrestLevelDecreaseSpeed"
    InitialLevel = "InitialLevel"
    SHAPE_Length = "SHAPE_Length"
    DataSource = "DataSource"
    AssetName = "AssetName"
    Element_S = "Element_S"
    NetTypeNo = "NetTypeNo"
    Description = "Description"

class msm_WeirTable(BaseTable):
    """Table for msm_Weir (Weirs)."""
    
    @property
    def columns(self) -> msm_WeirTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = msm_WeirTableColumns(self)
        return self._columns