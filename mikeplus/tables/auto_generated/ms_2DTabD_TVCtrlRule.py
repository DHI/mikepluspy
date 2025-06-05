from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class ms_2DTabD_TVCtrlRuleTableColumns(BaseColumns):
    """Column names for ms_2DTabD_TVCtrlRule (Time varying control rule)."""
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

class ms_2DTabD_TVCtrlRuleTable(BaseTable):
    """Table for ms_2DTabD_TVCtrlRule (Time varying control rule)."""
    
    @property
    def columns(self) -> ms_2DTabD_TVCtrlRuleTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = ms_2DTabD_TVCtrlRuleTableColumns(self)
        return self._columns