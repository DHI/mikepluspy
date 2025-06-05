from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class m2d_ADInitalConditionTableColumns(BaseColumns):
    """Column names for m2d_ADInitalCondition (2D AD initial conditions)."""
    MUID = "MUID"
    """MUID"""
    ComponentID = "ComponentID"
    """Component"""
    ComponentTypeNo = "ComponentTypeNo"
    """Component type"""
    TypeNo = "TypeNo"
    """Type"""
    SourceTypeNo = "SourceTypeNo"
    """Source"""
    UniformValue = "UniformValue"
    """Initial condition"""
    DefaultValue = "DefaultValue"
    """Default initial condition"""
    Layer = "Layer"
    """Layer"""
    LayerItem = "LayerItem"
    """Layer initial condition item"""
    LayerUnitNo = "LayerUnitNo"
    """Layer unit"""
    FileName = "FileName"
    """File"""
    ItemName = "ItemName"
    """Initial condition item"""
    ItemNo = "ItemNo"
    """Item no"""
    ExportFile = "ExportFile"
    """Export file"""
    ExportItemName = "ExportItemName"
    """Export item name"""
    ExportItemNo = "ExportItemNo"
    """Export item no"""
    Unit = "Unit"
    """Unit"""

class m2d_ADInitalConditionTable(BaseTable):
    """Table for m2d_ADInitalCondition (2D AD initial conditions)."""
    
    @property
    def columns(self) -> m2d_ADInitalConditionTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = m2d_ADInitalConditionTableColumns(self)
        return self._columns