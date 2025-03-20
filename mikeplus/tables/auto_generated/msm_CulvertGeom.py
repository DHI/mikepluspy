from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class msm_CulvertGeomTableColumns(BaseColumns):
    """Column names for msm_CulvertGeom (Culvert geometry)."""
    MUID = "MUID"
    CulvertID = "CulvertID"
    Sqn = "Sqn"
    Level = "Level"
    Width = "Width"

class msm_CulvertGeomTable(BaseTable):
    """Table for msm_CulvertGeom (Culvert geometry)."""
    
    @property
    def columns(self) -> msm_CulvertGeomTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = msm_CulvertGeomTableColumns(self)
        return self._columns