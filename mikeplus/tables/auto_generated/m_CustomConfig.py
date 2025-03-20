from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class m_CustomConfigTableColumns(BaseColumns):
    """Column names for m_CustomConfig (Custom configuration)."""
    MUID = "MUID"
    Name = "Name"
    ApplyNo = "ApplyNo"
    ValueTypeNo = "ValueTypeNo"
    ValueText = "ValueText"
    ValueInt = "ValueInt"
    ValueDouble = "ValueDouble"
    ValueDate = "ValueDate"
    ApplySimNo = "ApplySimNo"
    SimSections = "SimSections"
    Description = "Description"

class m_CustomConfigTable(BaseTable):
    """Table for m_CustomConfig (Custom configuration)."""
    
    @property
    def columns(self) -> m_CustomConfigTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = m_CustomConfigTableColumns(self)
        return self._columns