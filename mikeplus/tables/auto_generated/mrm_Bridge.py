from mikeplus.tables.base_geometry_table import BaseGeometryTable
from mikeplus.tables.base_geometry_table import BaseColumns

class mrm_BridgeTableColumns(BaseColumns):
    """Column names for mrm_Bridge (Bridges)."""
    MUID = "MUID"
    Enabled = "Enabled"
    RiverID = "RiverID"
    Chainage = "Chainage"
    ApplyFactorNo = "ApplyFactorNo"
    FactorValue = "FactorValue"
    HeadLossCmTypeNo = "HeadLossCmTypeNo"
    DataSource = "DataSource"
    Element_S = "Element_S"
    Description = "Description"

class mrm_BridgeTable(BaseGeometryTable):
    """Table for mrm_Bridge (Bridges)."""
    
    @property
    def columns(self) -> mrm_BridgeTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mrm_BridgeTableColumns(self)
        return self._columns