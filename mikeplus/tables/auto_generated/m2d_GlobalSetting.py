from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class m2d_GlobalSettingTableColumns(BaseColumns):
    """Column names for m2d_GlobalSetting (m2d_GlobalSetting)."""
    MUID = "MUID"
    TypeNo = "TypeNo"
    ValueInt = "ValueInt"
    ValueIntDom = "ValueIntDom"
    ValueDouble = "ValueDouble"
    ValueText = "ValueText"
    ValueDt = "ValueDt"
    PfsRoute = "PfsRoute"
    Comment = "Comment"
    ControlNo = "ControlNo"
    ValueFilePath = "ValueFilePath"

class m2d_GlobalSettingTable(BaseTable):
    """Table for m2d_GlobalSetting (m2d_GlobalSetting)."""
    
    @property
    def columns(self) -> m2d_GlobalSettingTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = m2d_GlobalSettingTableColumns(self)
        return self._columns