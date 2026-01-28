from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class m21_pfsSectionTableColumns(BaseColumns):
    """Column names for m21_pfsSection (m21_pfsSection)."""
    MUID = "MUID"
    """ID"""
    ParentID = "ParentID"
    """ParentID"""
    SectionName = "SectionName"
    """SectionName"""
    Sqn = "Sqn"
    """Sqn"""

class m21_pfsSectionTable(BaseTable):
    """Table for m21_pfsSection (m21_pfsSection)."""
    
    @property
    def columns(self) -> m21_pfsSectionTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = m21_pfsSectionTableColumns(self)
        return self._columns