from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class ms_2DTabD_Tabulated_QHTableColumns(BaseColumns):
    """Column names for ms_2DTabD_Tabulated_QH ()."""
    MUID = "MUID"
    MasterID = "MasterID"
    RowSqn = "RowSqn"
    ColSqn = "ColSqn"
    RowHeaderValue = "RowHeaderValue"
    ColHeaderValue = "ColHeaderValue"
    CellValue = "CellValue"

class ms_2DTabD_Tabulated_QHTable(BaseTable):
    """Table for ms_2DTabD_Tabulated_QH ()."""
    
    @property
    def columns(self) -> ms_2DTabD_Tabulated_QHTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = ms_2DTabD_Tabulated_QHTableColumns(self)
        return self._columns