from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class mw_RuleTableColumns(BaseColumns):
    """Column names for mw_Rule (Extended rule-based controls)."""
    MUID = "MUID"
    Sqn = "Sqn"
    Enabled = "Enabled"
    Condition = "Condition"
    Condition1 = "Condition1"
    Condition2 = "Condition2"
    Description = "Description"

class mw_RuleTable(BaseTable):
    """Table for mw_Rule (Extended rule-based controls)."""
    
    @property
    def columns(self) -> mw_RuleTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mw_RuleTableColumns(self)
        return self._columns