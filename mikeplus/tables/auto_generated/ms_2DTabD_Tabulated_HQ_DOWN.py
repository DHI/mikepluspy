from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class ms_2DTabD_Tabulated_HQ_DOWNTableColumns(BaseColumns):
    """Column names for ms_2DTabD_Tabulated_HQ_DOWN ()."""
    MUID = "MUID"
    MasterID = "MasterID"
    RowSqn = "RowSqn"
    ColSqn = "ColSqn"
    RowHeaderValue = "RowHeaderValue"
    ColHeaderValue = "ColHeaderValue"
    CellValue = "CellValue"

class ms_2DTabD_Tabulated_HQ_DOWNTable(BaseTable):
    """Table for ms_2DTabD_Tabulated_HQ_DOWN ()."""
    
    @property
    def columns(self) -> ms_2DTabD_Tabulated_HQ_DOWNTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = ms_2DTabD_Tabulated_HQ_DOWNTableColumns(self)
        return self._columns