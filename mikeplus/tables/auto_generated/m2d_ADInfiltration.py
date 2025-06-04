from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class m2d_ADInfiltrationTableColumns(BaseColumns):
    """Column names for m2d_ADInfiltration (2D WQ infiltration)."""
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
    """Infiltration concentration value"""
    DefaultValue = "DefaultValue"
    """Default infiltration concentration"""
    SoftStartInterval = "SoftStartInterval"
    """Start up  interval [sec]"""
    Layer = "Layer"
    """Layer"""
    LayerItem = "LayerItem"
    """Layer infiltration concentration item"""
    LayerUnitNo = "LayerUnitNo"
    """Layer unit"""
    FileName = "FileName"
    """File"""
    ItemName = "ItemName"
    """Infiltration concentration item"""
    ItemNo = "ItemNo"
    """Item no"""
    ExportFile = "ExportFile"
    """Export file"""
    ExportItemName = "ExportItemName"
    """Export item name"""
    ExportItemNo = "ExportItemNo"
    """Export item no"""

class m2d_ADInfiltrationTable(BaseTable):
    """Table for m2d_ADInfiltration (2D WQ infiltration)."""
    
    @property
    def columns(self) -> m2d_ADInfiltrationTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = m2d_ADInfiltrationTableColumns(self)
        return self._columns