from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class m21_pfsParamTableColumns(BaseColumns):
    """Column names for m21_pfsParam (m21_pfsParam)."""
    MUID = "MUID"
    """ID"""
    ParentID = "ParentID"
    """ParentID"""
    Sqn = "Sqn"
    """Sqn"""
    Type = "Type"
    """Type"""
    Value = "Value"
    """Value"""

class m21_pfsParamTable(BaseTable):
    """Table for m21_pfsParam (m21_pfsParam)."""
    
    @property
    def columns(self) -> m21_pfsParamTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = m21_pfsParamTableColumns(self)
        return self._columns