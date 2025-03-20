from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class mw_MDemandTableColumns(BaseColumns):
    """Column names for mw_MDemand (Multiple demands)."""
    MUID = "MUID"
    JunctionID = "JunctionID"
    Demand = "Demand"
    Category = "Category"
    PatternID = "PatternID"
    Enabled = "Enabled"
    GenerateTypeNo = "GenerateTypeNo"
    DemCoeff = "DemCoeff"
    Description = "Description"

class mw_MDemandTable(BaseTable):
    """Table for mw_MDemand (Multiple demands)."""
    
    @property
    def columns(self) -> mw_MDemandTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mw_MDemandTableColumns(self)
        return self._columns