from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class msm_RSSGeomTableColumns(BaseColumns):
    """Column names for msm_RSSGeom (Result selection geometry)."""
    MUID = "MUID"
    SelectionID = "SelectionID"
    Sqn = "Sqn"
    X = "X"
    Y = "Y"
    ElemID = "ElemID"

class msm_RSSGeomTable(BaseTable):
    """Table for msm_RSSGeom (Result selection geometry)."""
    
    @property
    def columns(self) -> msm_RSSGeomTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = msm_RSSGeomTableColumns(self)
        return self._columns