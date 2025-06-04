from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class m21_pfsKeywordTableColumns(BaseColumns):
    """Column names for m21_pfsKeyword (m21_pfsKeyword)."""
    MUID = "MUID"
    """ID"""
    ParentID = "ParentID"
    """ParentID"""
    KeywordName = "KeywordName"
    """KeywordName"""
    Sqn = "Sqn"
    """Sqn"""

class m21_pfsKeywordTable(BaseTable):
    """Table for m21_pfsKeyword (m21_pfsKeyword)."""
    
    @property
    def columns(self) -> m21_pfsKeywordTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = m21_pfsKeywordTableColumns(self)
        return self._columns