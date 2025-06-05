from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class m_CustomConfigTableColumns(BaseColumns):
    """Column names for m_CustomConfig (Custom configuration)."""
    MUID = "MUID"
    """ID"""
    Name = "Name"
    """Option name"""
    ApplyNo = "ApplyNo"
    """Apply option"""
    ValueTypeNo = "ValueTypeNo"
    """Value type"""
    ValueText = "ValueText"
    """Value text/boolea"""
    ValueInt = "ValueInt"
    """Value int"""
    ValueDouble = "ValueDouble"
    """Value double"""
    ValueDate = "ValueDate"
    """Value datetime"""
    ApplySimNo = "ApplySimNo"
    """Apply only to following Simulation IDs"""
    SimSections = "SimSections"
    """Target simulations"""
    Description = "Description"
    """Description"""

class m_CustomConfigTable(BaseTable):
    """Table for m_CustomConfig (Custom configuration)."""
    
    @property
    def columns(self) -> m_CustomConfigTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = m_CustomConfigTableColumns(self)
        return self._columns