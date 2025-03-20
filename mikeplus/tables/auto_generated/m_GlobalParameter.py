from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class m_GlobalParameterTableColumns(BaseColumns):
    """Column names for m_GlobalParameter (m_GlobalParameter)."""
    MUID = "MUID"
    ModelNo = "ModelNo"
    TypeNo = "TypeNo"
    ValueInt = "ValueInt"
    ValueIntDom = "ValueIntDom"
    ValueDouble = "ValueDouble"
    ValueText = "ValueText"
    ValueDt = "ValueDt"
    Comment = "Comment"
    ControlNo = "ControlNo"
    ValueFilePath = "ValueFilePath"

class m_GlobalParameterTable(BaseTable):
    """Table for m_GlobalParameter (m_GlobalParameter)."""
    
    @property
    def columns(self) -> m_GlobalParameterTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = m_GlobalParameterTableColumns(self)
        return self._columns