from mikeplus.tables.base_geometry_table import BaseGeometryTable
from mikeplus.tables.base_geometry_table import BaseColumns

class mrm_DirectDischargeTableColumns(BaseColumns):
    """Column names for mrm_DirectDischarge (Direct discharges)."""
    MUID = "MUID"
    Enabled = "Enabled"
    RiverID = "RiverID"
    Chainage = "Chainage"
    InitialDischarge = "InitialDischarge"
    MaxChange = "MaxChange"
    StructureNo = "StructureNo"
    MaxDischarge = "MaxDischarge"
    DataSource = "DataSource"
    Element_S = "Element_S"
    Description = "Description"

class mrm_DirectDischargeTable(BaseGeometryTable):
    """Table for mrm_DirectDischarge (Direct discharges)."""
    
    @property
    def columns(self) -> mrm_DirectDischargeTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mrm_DirectDischargeTableColumns(self)
        return self._columns