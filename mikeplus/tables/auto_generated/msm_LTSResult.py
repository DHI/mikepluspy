from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class msm_LTSResultTableColumns(BaseColumns):
    """Column names for msm_LTSResult (LTS Global parameters)."""
    MUID = "MUID"
    Dth = "Dth"
    Pc = "Pc"
    DtQV = "DtQV"
    DtQTn = "DtQTn"
    EmissionsNo = "EmissionsNo"
    EventLimit = "EventLimit"
    StatFrequencyNo = "StatFrequencyNo"
    DWFSaveFrequency = "DWFSaveFrequency"

class msm_LTSResultTable(BaseTable):
    """Table for msm_LTSResult (LTS Global parameters)."""
    
    @property
    def columns(self) -> msm_LTSResultTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = msm_LTSResultTableColumns(self)
        return self._columns