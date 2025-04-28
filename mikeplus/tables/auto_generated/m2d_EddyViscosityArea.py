from mikeplus.tables.base_geometry_table import BaseGeometryTable
from mikeplus.tables.base_geometry_table import BaseColumns

class m2d_EddyViscosityAreaTableColumns(BaseColumns):
    """Column names for m2d_EddyViscosityArea (2D eddy viscosity)."""
    Sqn = "Sqn"
    ApplyNo = "ApplyNo"
    MUID = "MUID"
    EddyViscosity = "EddyViscosity"
    Description = "Description"

class m2d_EddyViscosityAreaTable(BaseGeometryTable):
    """Table for m2d_EddyViscosityArea (2D eddy viscosity)."""
    
    @property
    def columns(self) -> m2d_EddyViscosityAreaTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = m2d_EddyViscosityAreaTableColumns(self)
        return self._columns