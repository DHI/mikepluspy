from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class m2d_ADInitalConditionTableColumns(BaseColumns):
    """Column names for m2d_ADInitalCondition (2D AD initial conditions)."""
    MUID = "MUID"
    ComponentID = "ComponentID"
    ComponentTypeNo = "ComponentTypeNo"
    TypeNo = "TypeNo"
    SourceTypeNo = "SourceTypeNo"
    UniformValue = "UniformValue"
    DefaultValue = "DefaultValue"
    Layer = "Layer"
    LayerItem = "LayerItem"
    LayerUnitNo = "LayerUnitNo"
    FileName = "FileName"
    ItemName = "ItemName"
    ItemNo = "ItemNo"
    ExportFile = "ExportFile"
    ExportItemName = "ExportItemName"
    ExportItemNo = "ExportItemNo"
    Unit = "Unit"

class m2d_ADInitalConditionTable(BaseTable):
    """Table for m2d_ADInitalCondition (2D AD initial conditions)."""
    
    @property
    def columns(self) -> m2d_ADInitalConditionTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = m2d_ADInitalConditionTableColumns(self)
        return self._columns