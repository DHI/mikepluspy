from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class ms_2DTabD_Bridge_FHWA_WSPRO_spur_dykeIIITableColumns(BaseColumns):
    """Column names for ms_2DTabD_Bridge_FHWA_WSPRO_spur_dykeIII ()."""
    MUID = "MUID"
    """MUID"""
    MasterID = "MasterID"
    """MasterID"""
    RowSqn = "RowSqn"
    """RowSqn"""
    ColSqn = "ColSqn"
    """ColSqn"""
    RowHeaderValue = "RowHeaderValue"
    """RowHeaderValue"""
    ColHeaderValue = "ColHeaderValue"
    """ColHeaderValue"""
    CellValue = "CellValue"
    """CellValue"""

class ms_2DTabD_Bridge_FHWA_WSPRO_spur_dykeIIITable(BaseTable):
    """Table for ms_2DTabD_Bridge_FHWA_WSPRO_spur_dykeIII ()."""
    
    @property
    def columns(self) -> ms_2DTabD_Bridge_FHWA_WSPRO_spur_dykeIIITableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = ms_2DTabD_Bridge_FHWA_WSPRO_spur_dykeIIITableColumns(self)
        return self._columns