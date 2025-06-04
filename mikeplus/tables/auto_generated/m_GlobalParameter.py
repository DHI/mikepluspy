from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class m_GlobalParameterTableColumns(BaseColumns):
    """Column names for m_GlobalParameter (m_GlobalParameter)."""
    MUID = "MUID"
    """ID"""
    ModelNo = "ModelNo"
    """Value int"""
    TypeNo = "TypeNo"
    """Value int"""
    ValueInt = "ValueInt"
    """Value int"""
    ValueIntDom = "ValueIntDom"
    """Value int"""
    ValueDouble = "ValueDouble"
    """Value double"""
    ValueText = "ValueText"
    """Value text"""
    ValueDt = "ValueDt"
    """Value datetime"""
    Comment = "Comment"
    """Comment"""
    ControlNo = "ControlNo"
    """ControlNo"""
    ValueFilePath = "ValueFilePath"
    """ValueFilePath"""

class m_GlobalParameterTable(BaseTable):
    """Table for m_GlobalParameter (m_GlobalParameter)."""
    
    @property
    def columns(self) -> m_GlobalParameterTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = m_GlobalParameterTableColumns(self)
        return self._columns