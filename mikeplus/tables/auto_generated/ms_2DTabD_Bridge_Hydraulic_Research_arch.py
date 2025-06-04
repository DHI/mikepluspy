from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class ms_2DTabD_Bridge_Hydraulic_Research_archTableColumns(BaseColumns):
    """Column names for ms_2DTabD_Bridge_Hydraulic_Research_arch ()."""
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

class ms_2DTabD_Bridge_Hydraulic_Research_archTable(BaseTable):
    """Table for ms_2DTabD_Bridge_Hydraulic_Research_arch ()."""
    
    @property
    def columns(self) -> ms_2DTabD_Bridge_Hydraulic_Research_archTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = ms_2DTabD_Bridge_Hydraulic_Research_archTableColumns(self)
        return self._columns