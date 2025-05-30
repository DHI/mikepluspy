from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class ms_2DTabD_Bridge_FHWA_WSPRO_PilesTableColumns(BaseColumns):
    """Column names for ms_2DTabD_Bridge_FHWA_WSPRO_Piles ()."""
    MUID = "MUID"
    MasterID = "MasterID"
    RowSqn = "RowSqn"
    ColSqn = "ColSqn"
    RowHeaderValue = "RowHeaderValue"
    ColHeaderValue = "ColHeaderValue"
    CellValue = "CellValue"

class ms_2DTabD_Bridge_FHWA_WSPRO_PilesTable(BaseTable):
    """Table for ms_2DTabD_Bridge_FHWA_WSPRO_Piles ()."""
    
    @property
    def columns(self) -> ms_2DTabD_Bridge_FHWA_WSPRO_PilesTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = ms_2DTabD_Bridge_FHWA_WSPRO_PilesTableColumns(self)
        return self._columns