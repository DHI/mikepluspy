from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class mrm_DAUpdateParaTableColumns(BaseColumns):
    """Column names for mrm_DAUpdatePara (Update parameters)."""
    MUID = "MUID"
    ApplyNo = "ApplyNo"
    RiverID = "RiverID"
    Chainage = "Chainage"
    UpdatedItemNo = "UpdatedItemNo"
    WQcomponent = "WQcomponent"
    FileName = "FileName"
    FileItem = "FileItem"
    DistribTypeNo = "DistribTypeNo"
    Amplitude = "Amplitude"
    MinChainage = "MinChainage"
    MaxChainage = "MaxChainage"
    IncludeConnectedNo = "IncludeConnectedNo"
    SoftStartNo = "SoftStartNo"
    IncludeErrorFrcstNo = "IncludeErrorFrcstNo"
    EquationID = "EquationID"
    StdDevTypeNo = "StdDevTypeNo"
    StdDevValue = "StdDevValue"
    StdDevFileName = "StdDevFileName"
    StdDevFileItem = "StdDevFileItem"
    StdDevApplyLowerBoxNo = "StdDevApplyLowerBoxNo"
    StdDevLowerValue = "StdDevLowerValue"
    StdDevApplyUpperBoxNo = "StdDevApplyUpperBoxNo"
    StdDevUpperValue = "StdDevUpperValue"
    Description = "Description"

class mrm_DAUpdateParaTable(BaseTable):
    """Table for mrm_DAUpdatePara (Update parameters)."""
    
    @property
    def columns(self) -> mrm_DAUpdateParaTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mrm_DAUpdateParaTableColumns(self)
        return self._columns