from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class m_StatusCodeTableColumns(BaseColumns):
    """Column names for m_StatusCode (Status code)."""
    MUID = "MUID"
    """MUID"""
    StatusCodeTypeNo = "StatusCodeTypeNo"
    """StatusCodeTypeNo"""
    StatusCodeNo = "StatusCodeNo"
    """Code"""
    StatusCodeName = "StatusCodeName"
    """Code name"""

class m_StatusCodeTable(BaseTable):
    """Table for m_StatusCode (Status code)."""
    
    @property
    def columns(self) -> m_StatusCodeTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = m_StatusCodeTableColumns(self)
        return self._columns