from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class mss_RuleTableColumns(BaseColumns):
    """Column names for mss_Rule (Controls)."""
    MUID = "MUID"
    Sqn = "Sqn"
    Enabled = "Enabled"
    Description = "Description"
    Condition = "Condition"

class mss_RuleTable(BaseTable):
    """Table for mss_Rule (Controls)."""
    
    @property
    def columns(self) -> mss_RuleTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mss_RuleTableColumns(self)
        return self._columns