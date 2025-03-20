from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class m_MediaTableColumns(BaseColumns):
    """Column names for m_Media (m_Media)."""
    MUID = "MUID"
    TableName = "TableName"
    ItemMUID = "ItemMUID"
    FilePath = "FilePath"
    Format = "Format"

class m_MediaTable(BaseTable):
    """Table for m_Media (m_Media)."""
    
    @property
    def columns(self) -> m_MediaTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = m_MediaTableColumns(self)
        return self._columns