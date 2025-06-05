from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class ms_2DTabD_GenericCtrlRuleTableColumns(BaseColumns):
    """Column names for ms_2DTabD_GenericCtrlRule ()."""
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

class ms_2DTabD_GenericCtrlRuleTable(BaseTable):
    """Table for ms_2DTabD_GenericCtrlRule ()."""
    
    @property
    def columns(self) -> ms_2DTabD_GenericCtrlRuleTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = ms_2DTabD_GenericCtrlRuleTableColumns(self)
        return self._columns