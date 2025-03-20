from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class mw_WDOSettingsTableColumns(BaseColumns):
    """Column names for mw_WDOSettings (Settings)."""
    MUID = "MUID"
    ID = "ID"
    Section = "Section"
    Keyname = "Keyname"
    KeyValue = "KeyValue"
    Comment = "Comment"

class mw_WDOSettingsTable(BaseTable):
    """Table for mw_WDOSettings (Settings)."""
    
    @property
    def columns(self) -> mw_WDOSettingsTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mw_WDOSettingsTableColumns(self)
        return self._columns