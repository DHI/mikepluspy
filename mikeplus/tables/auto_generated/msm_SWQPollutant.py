from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class msm_SWQPollutantTableColumns(BaseColumns):
    """Column names for msm_SWQPollutant (SWQ advanced methods)."""
    MUID = "MUID"
    TypeNo = "TypeNo"
    MethodNo = "MethodNo"
    ComponentID = "ComponentID"
    SedimentAttachNo = "SedimentAttachNo"
    MaxEMC = "MaxEMC"
    BuildUpTypeNo = "BuildUpTypeNo"
    BuildUpRate = "BuildUpRate"
    MaxBuildUp = "MaxBuildUp"
    DetachRate = "DetachRate"
    WashOffExp = "WashOffExp"

class msm_SWQPollutantTable(BaseTable):
    """Table for msm_SWQPollutant (SWQ advanced methods)."""
    
    @property
    def columns(self) -> msm_SWQPollutantTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = msm_SWQPollutantTableColumns(self)
        return self._columns