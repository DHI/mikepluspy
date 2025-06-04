from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class m2d_ADDecayTableColumns(BaseColumns):
    """Column names for m2d_ADDecay (2D decay)."""
    MUID = "MUID"
    """MUID"""
    ComponentID = "ComponentID"
    """Component"""
    TypeNo = "TypeNo"
    """Type"""
    ConstantDecay = "ConstantDecay"
    """Decay factor [/h]"""
    FilePath = "FilePath"
    """File"""
    ItemName = "ItemName"
    """Decay factor item"""
    ItemNo = "ItemNo"
    """Item no"""

class m2d_ADDecayTable(BaseTable):
    """Table for m2d_ADDecay (2D decay)."""
    
    @property
    def columns(self) -> m2d_ADDecayTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = m2d_ADDecayTableColumns(self)
        return self._columns