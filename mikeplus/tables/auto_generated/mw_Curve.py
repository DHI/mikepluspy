from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class mw_CurveTableColumns(BaseColumns):
    """Column names for mw_Curve (Curves and relations)."""
    MUID = "MUID"
    TypeNo = "TypeNo"
    Description = "Description"

class mw_CurveTable(BaseTable):
    """Table for mw_Curve (Curves and relations)."""
    
    @property
    def columns(self) -> mw_CurveTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mw_CurveTableColumns(self)
        return self._columns