from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class m2d_ADEvaporationTableColumns(BaseColumns):
    """Column names for m2d_ADEvaporation (2D WQ evaporation)."""
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
    """Evaporation concentration value"""
    DefaultValue = "DefaultValue"
    """Default evaporation concentration"""
    SoftStartInterval = "SoftStartInterval"
    """Soft start interval [sec]"""
    Layer = "Layer"
    """Layer"""
    LayerItem = "LayerItem"
    """Layer evaporation concentration item"""
    LayerUnitNo = "LayerUnitNo"
    """Layer unit"""
    FileName = "FileName"
    """File"""
    ItemName = "ItemName"
    """Evaporation concentration item"""
    ItemNo = "ItemNo"
    """Item no"""
    ExportFile = "ExportFile"
    """Export file"""
    ExportItemName = "ExportItemName"
    """Export item name"""
    ExportItemNo = "ExportItemNo"
    """Export item no"""

class m2d_ADEvaporationTable(BaseTable):
    """Table for m2d_ADEvaporation (2D WQ evaporation)."""
    
    @property
    def columns(self) -> m2d_ADEvaporationTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = m2d_ADEvaporationTableColumns(self)
        return self._columns