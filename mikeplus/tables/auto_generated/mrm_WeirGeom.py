from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class mrm_WeirGeomTableColumns(BaseColumns):
    """Column names for mrm_WeirGeom (River weir geometry)."""
    MUID = "MUID"
    WeirID = "WeirID"
    Sqn = "Sqn"
    Level = "Level"
    Width = "Width"

class mrm_WeirGeomTable(BaseTable):
    """Table for mrm_WeirGeom (River weir geometry)."""
    
    @property
    def columns(self) -> mrm_WeirGeomTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mrm_WeirGeomTableColumns(self)
        return self._columns