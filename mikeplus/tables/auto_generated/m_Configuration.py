from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class m_ConfigurationTableColumns(BaseColumns):
    """Column names for m_Configuration (MIKE 1D engine configuration)."""
    MUID = "MUID"
    Section = "Section"
    Comment = "Comment"
    ValueInt = "ValueInt"
    ValueDouble = "ValueDouble"
    ValueText = "ValueText"

class m_ConfigurationTable(BaseTable):
    """Table for m_Configuration (MIKE 1D engine configuration)."""
    
    @property
    def columns(self) -> m_ConfigurationTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = m_ConfigurationTableColumns(self)
        return self._columns