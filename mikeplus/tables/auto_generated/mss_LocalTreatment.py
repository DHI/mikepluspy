from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class mss_LocalTreatmentTableColumns(BaseColumns):
    """Column names for mss_LocalTreatment (Local treatment)."""
    MUID = "MUID"
    Description = "Description"
    NodeID = "NodeID"
    PollutantID = "PollutantID"
    Function = "Function"

class mss_LocalTreatmentTable(BaseTable):
    """Table for mss_LocalTreatment (Local treatment)."""
    
    @property
    def columns(self) -> mss_LocalTreatmentTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mss_LocalTreatmentTableColumns(self)
        return self._columns