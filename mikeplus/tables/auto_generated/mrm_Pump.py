from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class mrm_PumpTableColumns(BaseColumns):
    """Column names for mrm_Pump (Pumps)."""
    MUID = "MUID"
    Enabled = "Enabled"
    RiverID = "RiverID"
    Chainage = "Chainage"
    TypeNo = "TypeNo"
    StartLevel = "StartLevel"
    StopLevel = "StopLevel"
    AccTime = "AccTime"
    DecTime = "DecTime"
    ConstFlow = "ConstFlow"
    QdHTable = "QdHTable"
    DataSource = "DataSource"
    Element_S = "Element_S"
    Description = "Description"

class mrm_PumpTable(BaseTable):
    """Table for mrm_Pump (Pumps)."""
    
    @property
    def columns(self) -> mrm_PumpTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mrm_PumpTableColumns(self)
        return self._columns