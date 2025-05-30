from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class m_StatusTableColumns(BaseColumns):
    """Column names for m_Status (m_Status)."""
    MUID = "MUID"
    TableName = "TableName"
    FieldName = "FieldName"
    ItemMUID = "ItemMUID"
    StatusText = "StatusText"

class m_StatusTable(BaseTable):
    """Table for m_Status (m_Status)."""
    
    @property
    def columns(self) -> m_StatusTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = m_StatusTableColumns(self)
        return self._columns