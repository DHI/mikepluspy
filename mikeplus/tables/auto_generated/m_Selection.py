from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class m_SelectionTableColumns(BaseColumns):
    """Column names for m_Selection (m_Selection)."""
    MUID = "MUID"
    SelectionID = "SelectionID"
    TableName = "TableName"
    ItemMUID = "ItemMUID"

class m_SelectionTable(BaseTable):
    """Table for m_Selection (m_Selection)."""
    
    @property
    def columns(self) -> m_SelectionTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = m_SelectionTableColumns(self)
        return self._columns