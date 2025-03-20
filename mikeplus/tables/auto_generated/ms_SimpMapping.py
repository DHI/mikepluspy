from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class ms_SimpMappingTableColumns(BaseColumns):
    """Column names for ms_SimpMapping (ms_SimpMapping)."""
    MUID = "MUID"
    SettingID = "SettingID"
    TargetSimpID = "TargetSimpID"
    SourceInfo = "SourceInfo"

class ms_SimpMappingTable(BaseTable):
    """Table for ms_SimpMapping (ms_SimpMapping)."""
    
    @property
    def columns(self) -> ms_SimpMappingTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = ms_SimpMappingTableColumns(self)
        return self._columns