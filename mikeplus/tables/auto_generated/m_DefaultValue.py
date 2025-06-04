from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class m_DefaultValueTableColumns(BaseColumns):
    """Column names for m_DefaultValue (m_DefaultValue)."""
    MUID = "MUID"
    """ID"""
    TableName = "TableName"
    """Table name"""
    FieldName = "FieldName"
    """Field name"""
    Value = "Value"
    """Item MUID"""

class m_DefaultValueTable(BaseTable):
    """Table for m_DefaultValue (m_DefaultValue)."""
    
    @property
    def columns(self) -> m_DefaultValueTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = m_DefaultValueTableColumns(self)
        return self._columns