from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class m2d_ADPrecipitationTableColumns(BaseColumns):
    """Column names for m2d_ADPrecipitation (2D WQ precipitation)."""
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
    """Precipitation concentration value"""
    DefaultValue = "DefaultValue"
    """Default precipitation concentration"""
    SoftStartInterval = "SoftStartInterval"
    """Start up  interval [sec]"""
    Layer = "Layer"
    """Layer"""
    LayerItem = "LayerItem"
    """Layer precipitation concentration item"""
    LayerUnitNo = "LayerUnitNo"
    """Layer unit"""
    FileName = "FileName"
    """File"""
    ItemName = "ItemName"
    """Precipitation concentration item"""
    ItemNo = "ItemNo"
    """Item no"""
    ExportFile = "ExportFile"
    """Export file"""
    ExportItemName = "ExportItemName"
    """Export item name"""
    ExportItemNo = "ExportItemNo"
    """Export item no"""

class m2d_ADPrecipitationTable(BaseTable):
    """Table for m2d_ADPrecipitation (2D WQ precipitation)."""
    
    @property
    def columns(self) -> m2d_ADPrecipitationTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = m2d_ADPrecipitationTableColumns(self)
        return self._columns