from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class m2d_ADDispersionTableColumns(BaseColumns):
    """Column names for m2d_ADDispersion (2D AD dispersion)."""
    MUID = "MUID"
    """MUID"""
    ComponentID = "ComponentID"
    """Component"""
    FormulationNo = "FormulationNo"
    """Resistance formulation"""
    TypeNo = "TypeNo"
    """Type"""
    SourceTypeNo = "SourceTypeNo"
    """Source"""
    UniformValue = "UniformValue"
    """Uniform value"""
    DefaultValue = "DefaultValue"
    """Default value"""
    Layer = "Layer"
    """Layer"""
    LayerItem = "LayerItem"
    """Layer item"""
    LayerUnitNo = "LayerUnitNo"
    """Layer unit"""
    FileName = "FileName"
    """File"""
    ItemName = "ItemName"
    """Item name"""
    ItemNo = "ItemNo"
    """Item no"""
    ExportFile = "ExportFile"
    """Export file"""
    ExportItemName = "ExportItemName"
    """Export item name"""
    ExportItemNo = "ExportItemNo"
    """Export item no"""

class m2d_ADDispersionTable(BaseTable):
    """Table for m2d_ADDispersion (2D AD dispersion)."""
    
    @property
    def columns(self) -> m2d_ADDispersionTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = m2d_ADDispersionTableColumns(self)
        return self._columns