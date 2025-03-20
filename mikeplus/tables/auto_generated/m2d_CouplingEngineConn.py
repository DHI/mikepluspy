from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class m2d_CouplingEngineConnTableColumns(BaseColumns):
    """Column names for m2d_CouplingEngineConn (Coupling engine connections)."""
    MUID = "MUID"
    Chainage = "Chainage"
    QWeight = "QWeight"
    FaceNo = "FaceNo"
    CouplingCrestLevel = "CouplingCrestLevel"

class m2d_CouplingEngineConnTable(BaseTable):
    """Table for m2d_CouplingEngineConn (Coupling engine connections)."""
    
    @property
    def columns(self) -> m2d_CouplingEngineConnTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = m2d_CouplingEngineConnTableColumns(self)
        return self._columns