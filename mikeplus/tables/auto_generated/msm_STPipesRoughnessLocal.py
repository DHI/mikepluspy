from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class msm_STPipesRoughnessLocalTableColumns(BaseColumns):
    """Column names for msm_STPipesRoughnessLocal (Pipes roughness)."""
    MUID = "MUID"
    ConnectionTypeNo = "ConnectionTypeNo"
    LinkID = "LinkID"
    ListName = "ListName"
    LocIniManningTypeNo = "LocIniManningTypeNo"
    LocIniManning = "LocIniManning"

class msm_STPipesRoughnessLocalTable(BaseTable):
    """Table for msm_STPipesRoughnessLocal (Pipes roughness)."""
    
    @property
    def columns(self) -> msm_STPipesRoughnessLocalTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = msm_STPipesRoughnessLocalTableColumns(self)
        return self._columns