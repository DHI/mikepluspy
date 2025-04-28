from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class msm_ECOLABCoeffTableColumns(BaseColumns):
    """Column names for msm_ECOLABCoeff (MIKE ECO Lab constants)."""
    MUID = "MUID"
    ECOLABTemplateID = "ECOLABTemplateID"
    CoeffID = "CoeffID"
    ID = "ID"
    ConstantTypeNo = "ConstantTypeNo"
    Value = "Value"
    FileName = "FileName"
    FileItem = "FileItem"
    FileItemNo = "FileItemNo"
    Description = "Description"
    BuildinID = "BuildinID"
    SpatialVar = "SpatialVar"
    InterpolateNo = "InterpolateNo"

class msm_ECOLABCoeffTable(BaseTable):
    """Table for msm_ECOLABCoeff (MIKE ECO Lab constants)."""
    
    @property
    def columns(self) -> msm_ECOLABCoeffTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = msm_ECOLABCoeffTableColumns(self)
        return self._columns