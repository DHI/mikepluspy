from mikeplus.tables.base_geometry_table import BaseGeometryTable
from mikeplus.tables.base_geometry_table import BaseColumns

class m2d_MeshArcTableColumns(BaseColumns):
    """Column names for m2d_MeshArc (Mesh arc)."""
    MUID = "MUID"
    IsClosedNo = "IsClosedNo"
    Attribute = "Attribute"
    FromInactiveAreaNo = "FromInactiveAreaNo"

class m2d_MeshArcTable(BaseGeometryTable):
    """Table for m2d_MeshArc (Mesh arc)."""
    
    @property
    def columns(self) -> m2d_MeshArcTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = m2d_MeshArcTableColumns(self)
        return self._columns