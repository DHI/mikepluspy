from mikeplus.tables.base_geometry_table import BaseGeometryTable
from mikeplus.tables.base_geometry_table import BaseColumns

class m2d_CouplingEngineConnTableColumns(BaseColumns):
    """Column names for m2d_CouplingEngineConn (Coupling engine connections)."""
    MUID = "MUID"
    """ID"""
    Chainage = "Chainage"
    """Chainage [m]"""
    QWeight = "QWeight"
    """Q Weight [%]"""
    FaceNo = "FaceNo"
    """Face No."""
    CouplingCrestLevel = "CouplingCrestLevel"
    """Coupling crest level [m]"""

class m2d_CouplingEngineConnTable(BaseGeometryTable):
    """Table for m2d_CouplingEngineConn (Coupling engine connections)."""
    
    @property
    def columns(self) -> m2d_CouplingEngineConnTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = m2d_CouplingEngineConnTableColumns(self)
        return self._columns