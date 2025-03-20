from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class m2d_ADDispersionTableColumns(BaseColumns):
    """Column names for m2d_ADDispersion (2D AD dispersion)."""
    MUID = "MUID"
    ComponentID = "ComponentID"
    FormulationNo = "FormulationNo"
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

class m2d_ADDispersionTable(BaseTable):
    """Table for m2d_ADDispersion (2D AD dispersion)."""
    
    @property
    def columns(self) -> m2d_ADDispersionTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = m2d_ADDispersionTableColumns(self)
        return self._columns