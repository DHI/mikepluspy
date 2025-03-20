from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class msm_LTSDwfTsTableColumns(BaseColumns):
    """Column names for msm_LTSDwfTs (LTS Continuous TS output)."""
    MUID = "MUID"
    ApplyNo = "ApplyNo"
    LinkID = "LinkID"
    SelectionID = "SelectionID"

class msm_LTSDwfTsTable(BaseTable):
    """Table for msm_LTSDwfTs (LTS Continuous TS output)."""
    
    @property
    def columns(self) -> msm_LTSDwfTsTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = msm_LTSDwfTsTableColumns(self)
        return self._columns