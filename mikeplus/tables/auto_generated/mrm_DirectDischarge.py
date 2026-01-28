from mikeplus.tables.base_geometry_table import BaseGeometryTable
from mikeplus.tables.base_geometry_table import BaseColumns

class mrm_DirectDischargeTableColumns(BaseColumns):
    """Column names for mrm_DirectDischarge (Direct discharges)."""
    MUID = "MUID"
    """ID"""
    Enabled = "Enabled"
    """Apply"""
    RiverID = "RiverID"
    """River ID"""
    Chainage = "Chainage"
    """Chainage [m]"""
    InitialDischarge = "InitialDischarge"
    """Initial discharge [m^3/s]"""
    MaxChange = "MaxChange"
    """Maximum discharge change [m^3/s^2]"""
    StructureNo = "StructureNo"
    """Number of structures"""
    MaxDischarge = "MaxDischarge"
    """Max. discharge [m^3/s]"""
    DataSource = "DataSource"
    """Data source"""
    Element_S = "Element_S"
    """Status"""
    Description = "Description"
    """Description"""

class mrm_DirectDischargeTable(BaseGeometryTable):
    """Table for mrm_DirectDischarge (Direct discharges)."""
    
    @property
    def columns(self) -> mrm_DirectDischargeTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mrm_DirectDischargeTableColumns(self)
        return self._columns