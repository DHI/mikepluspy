from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class msm_STPipesRoughnessLocalTableColumns(BaseColumns):
    """Column names for msm_STPipesRoughnessLocal (Pipes roughness)."""
    MUID = "MUID"
    """MUID"""
    ConnectionTypeNo = "ConnectionTypeNo"
    """Connection type no"""
    LinkID = "LinkID"
    """Entire link"""
    ListName = "ListName"
    """List"""
    LocIniManningTypeNo = "LocIniManningTypeNo"
    """Roughness type"""
    LocIniManning = "LocIniManning"
    """Manning value"""

class msm_STPipesRoughnessLocalTable(BaseTable):
    """Table for msm_STPipesRoughnessLocal (Pipes roughness)."""
    
    @property
    def columns(self) -> msm_STPipesRoughnessLocalTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = msm_STPipesRoughnessLocalTableColumns(self)
        return self._columns