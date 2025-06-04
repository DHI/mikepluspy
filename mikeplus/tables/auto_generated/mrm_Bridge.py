from mikeplus.tables.base_geometry_table import BaseGeometryTable
from mikeplus.tables.base_geometry_table import BaseColumns

class mrm_BridgeTableColumns(BaseColumns):
    """Column names for mrm_Bridge (Bridges)."""
    MUID = "MUID"
    """ID"""
    Enabled = "Enabled"
    """Apply"""
    RiverID = "RiverID"
    """River ID"""
    Chainage = "Chainage"
    """Chainage [m]"""
    ApplyFactorNo = "ApplyFactorNo"
    """Apply flow factor"""
    FactorValue = "FactorValue"
    """Factor value"""
    HeadLossCmTypeNo = "HeadLossCmTypeNo"
    """Computational method"""
    DataSource = "DataSource"
    """Data source"""
    Element_S = "Element_S"
    """Status"""
    Description = "Description"
    """Description"""

class mrm_BridgeTable(BaseGeometryTable):
    """Table for mrm_Bridge (Bridges)."""
    
    @property
    def columns(self) -> mrm_BridgeTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mrm_BridgeTableColumns(self)
        return self._columns