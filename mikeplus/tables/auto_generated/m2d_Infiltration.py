from mikeplus.tables.base_geometry_table import BaseGeometryTable
from mikeplus.tables.base_geometry_table import BaseColumns

class m2d_InfiltrationTableColumns(BaseColumns):
    """Column names for m2d_Infiltration (2D infiltration)."""
    Sqn = "Sqn"
    ApplyNo = "ApplyNo"
    MUID = "MUID"
    Infiltration = "Infiltration"
    Leakage = "Leakage"
    DepthLevel = "DepthLevel"
    Porosity = "Porosity"
    Initial = "Initial"
    Description = "Description"

class m2d_InfiltrationTable(BaseGeometryTable):
    """Table for m2d_Infiltration (2D infiltration)."""
    
    @property
    def columns(self) -> m2d_InfiltrationTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = m2d_InfiltrationTableColumns(self)
        return self._columns