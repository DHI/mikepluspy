from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class m2d_CouplingEngineFaceTableColumns(BaseColumns):
    """Column names for m2d_CouplingEngineFace (Coupling engine faces)."""
    MUID = "MUID"
    FaceNo = "FaceNo"
    SurfaceGroundLevel = "SurfaceGroundLevel"

class m2d_CouplingEngineFaceTable(BaseTable):
    """Table for m2d_CouplingEngineFace (Coupling engine faces)."""
    
    @property
    def columns(self) -> m2d_CouplingEngineFaceTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = m2d_CouplingEngineFaceTableColumns(self)
        return self._columns