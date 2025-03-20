from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class msm_ProjectOutputTableColumns(BaseColumns):
    """Column names for msm_ProjectOutput (Project outputs)."""
    MUID = "MUID"
    SimulationID = "SimulationID"
    OutputID = "OutputID"
    ContentsTypeNo = "ContentsTypeNo"
    FormatNo = "FormatNo"
    DtSave = "DtSave"
    DtSaveUnitNo = "DtSaveUnitNo"
    DefaultSavePeriodNo = "DefaultSavePeriodNo"
    SaveStartDate = "SaveStartDate"
    SaveEndDate = "SaveEndDate"

class msm_ProjectOutputTable(BaseTable):
    """Table for msm_ProjectOutput (Project outputs)."""
    
    @property
    def columns(self) -> msm_ProjectOutputTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = msm_ProjectOutputTableColumns(self)
        return self._columns