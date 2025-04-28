from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class mw_WDOControlsTableColumns(BaseColumns):
    """Column names for mw_WDOControls (Controls)."""
    MUID = "MUID"
    ID = "ID"
    ControlType = "ControlType"
    Enabled = "Enabled"
    SensorID = "SensorID"
    SensorTable = "SensorTable"
    ModelID = "ModelID"
    Override = "Override"
    Priority = "Priority"
    Mult = "Mult"
    OffsetValue = "OffsetValue"
    Comment = "Comment"

class mw_WDOControlsTable(BaseTable):
    """Table for mw_WDOControls (Controls)."""
    
    @property
    def columns(self) -> mw_WDOControlsTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mw_WDOControlsTableColumns(self)
        return self._columns