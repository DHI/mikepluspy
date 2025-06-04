from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class m_ChartBookmarkTableColumns(BaseColumns):
    """Column names for m_ChartBookmark (m_ChartBookmark)."""
    MUID = "MUID"
    """ID"""
    XIntervalFrom = "XIntervalFrom"
    """XIntervalFrom"""
    XIntervalTo = "XIntervalTo"
    """XIntervalTo"""

class m_ChartBookmarkTable(BaseTable):
    """Table for m_ChartBookmark (m_ChartBookmark)."""
    
    @property
    def columns(self) -> m_ChartBookmarkTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = m_ChartBookmarkTableColumns(self)
        return self._columns