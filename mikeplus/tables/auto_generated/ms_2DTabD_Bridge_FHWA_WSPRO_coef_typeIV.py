from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class ms_2DTabD_Bridge_FHWA_WSPRO_coef_typeIVTableColumns(BaseColumns):
    """Column names for ms_2DTabD_Bridge_FHWA_WSPRO_coef_typeIV ()."""
    MUID = "MUID"
    MasterID = "MasterID"
    RowSqn = "RowSqn"
    ColSqn = "ColSqn"
    RowHeaderValue = "RowHeaderValue"
    ColHeaderValue = "ColHeaderValue"
    CellValue = "CellValue"

class ms_2DTabD_Bridge_FHWA_WSPRO_coef_typeIVTable(BaseTable):
    """Table for ms_2DTabD_Bridge_FHWA_WSPRO_coef_typeIV ()."""
    
    @property
    def columns(self) -> ms_2DTabD_Bridge_FHWA_WSPRO_coef_typeIVTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = ms_2DTabD_Bridge_FHWA_WSPRO_coef_typeIVTableColumns(self)
        return self._columns