from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class m2d_ADEvaporationTableColumns(BaseColumns):
    """Column names for m2d_ADEvaporation (2D WQ evaporation)."""
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

class m2d_ADEvaporationTable(BaseTable):
    """Table for m2d_ADEvaporation (2D WQ evaporation)."""
    
    @property
    def columns(self) -> m2d_ADEvaporationTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = m2d_ADEvaporationTableColumns(self)
        return self._columns