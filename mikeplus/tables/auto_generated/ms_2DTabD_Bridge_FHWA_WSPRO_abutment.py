from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class ms_2DTabD_Bridge_FHWA_WSPRO_abutmentTableColumns(BaseColumns):
    """Column names for ms_2DTabD_Bridge_FHWA_WSPRO_abutment ()."""
    MUID = "MUID"
    MasterID = "MasterID"
    RowSqn = "RowSqn"
    ColSqn = "ColSqn"
    RowHeaderValue = "RowHeaderValue"
    ColHeaderValue = "ColHeaderValue"
    CellValue = "CellValue"

class ms_2DTabD_Bridge_FHWA_WSPRO_abutmentTable(BaseTable):
    """Table for ms_2DTabD_Bridge_FHWA_WSPRO_abutment ()."""
    
    @property
    def columns(self) -> ms_2DTabD_Bridge_FHWA_WSPRO_abutmentTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = ms_2DTabD_Bridge_FHWA_WSPRO_abutmentTableColumns(self)
        return self._columns