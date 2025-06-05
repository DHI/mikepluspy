from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class m_ConfigurationTableColumns(BaseColumns):
    """Column names for m_Configuration (MIKE 1D engine configuration)."""
    MUID = "MUID"
    """ID"""
    Section = "Section"
    """Section"""
    Comment = "Comment"
    """Comment"""
    ValueInt = "ValueInt"
    """Value int"""
    ValueDouble = "ValueDouble"
    """Value double"""
    ValueText = "ValueText"
    """Value text"""

class m_ConfigurationTable(BaseTable):
    """Table for m_Configuration (MIKE 1D engine configuration)."""
    
    @property
    def columns(self) -> m_ConfigurationTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = m_ConfigurationTableColumns(self)
        return self._columns