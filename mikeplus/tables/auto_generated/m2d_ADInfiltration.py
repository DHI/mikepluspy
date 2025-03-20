from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class m2d_ADInfiltrationTableColumns(BaseColumns):
    """Column names for m2d_ADInfiltration (2D WQ infiltration)."""
    MUID = "MUID"
    ComponentID = "ComponentID"
    ComponentTypeNo = "ComponentTypeNo"
    TypeNo = "TypeNo"
    SourceTypeNo = "SourceTypeNo"
    UniformValue = "UniformValue"
    DefaultValue = "DefaultValue"
    SoftStartInterval = "SoftStartInterval"
    Layer = "Layer"
    LayerItem = "LayerItem"
    LayerUnitNo = "LayerUnitNo"
    FileName = "FileName"
    ItemName = "ItemName"
    ItemNo = "ItemNo"
    ExportFile = "ExportFile"
    ExportItemName = "ExportItemName"
    ExportItemNo = "ExportItemNo"

class m2d_ADInfiltrationTable(BaseTable):
    """Table for m2d_ADInfiltration (2D WQ infiltration)."""
    
    @property
    def columns(self) -> m2d_ADInfiltrationTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = m2d_ADInfiltrationTableColumns(self)
        return self._columns