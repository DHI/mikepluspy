from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class mrm_WeirGeomTableColumns(BaseColumns):
    """Column names for mrm_WeirGeom (River weir geometry)."""
    MUID = "MUID"
    """MUID"""
    WeirID = "WeirID"
    """WeirID"""
    Sqn = "Sqn"
    """Sqn"""
    Level = "Level"
    """Level [m]"""
    Width = "Width"
    """Width [m]"""

class mrm_WeirGeomTable(BaseTable):
    """Table for mrm_WeirGeom (River weir geometry)."""
    
    @property
    def columns(self) -> mrm_WeirGeomTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mrm_WeirGeomTableColumns(self)
        return self._columns