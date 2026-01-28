from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class ms_SimpSettingTableColumns(BaseColumns):
    """Column names for ms_SimpSetting (ms_SimpSetting)."""
    MUID = "MUID"
    """ID"""
    Sqn = "Sqn"
    """Sqn"""
    ModelNo = "ModelNo"
    """Model no"""
    ToolTypeNo = "ToolTypeNo"
    """ToolTypeNo"""
    ParamSettings = "ParamSettings"
    """ParamSettings"""

class ms_SimpSettingTable(BaseTable):
    """Table for ms_SimpSetting (ms_SimpSetting)."""
    
    @property
    def columns(self) -> ms_SimpSettingTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = ms_SimpSettingTableColumns(self)
        return self._columns