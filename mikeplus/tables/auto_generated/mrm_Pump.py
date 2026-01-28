from mikeplus.tables.base_geometry_table import BaseGeometryTable
from mikeplus.tables.base_geometry_table import BaseColumns

class mrm_PumpTableColumns(BaseColumns):
    """Column names for mrm_Pump (Pumps)."""
    MUID = "MUID"
    """ID"""
    Enabled = "Enabled"
    """Apply"""
    RiverID = "RiverID"
    """River ID"""
    Chainage = "Chainage"
    """Chainage [m]"""
    TypeNo = "TypeNo"
    """Pump type"""
    StartLevel = "StartLevel"
    """Start level [m]"""
    StopLevel = "StopLevel"
    """Stop level [m]"""
    AccTime = "AccTime"
    """Acceleration Time [sec]"""
    DecTime = "DecTime"
    """Deceleration Time [sec]"""
    ConstFlow = "ConstFlow"
    """Constant flow [m^3/s]"""
    QdHTable = "QdHTable"
    """Q-dH table"""
    DataSource = "DataSource"
    """Data source"""
    Element_S = "Element_S"
    """Status"""
    Description = "Description"
    """Description"""

class mrm_PumpTable(BaseGeometryTable):
    """Table for mrm_Pump (Pumps)."""
    
    @property
    def columns(self) -> mrm_PumpTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mrm_PumpTableColumns(self)
        return self._columns