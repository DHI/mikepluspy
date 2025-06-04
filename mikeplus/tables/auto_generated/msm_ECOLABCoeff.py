from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class msm_ECOLABCoeffTableColumns(BaseColumns):
    """Column names for msm_ECOLABCoeff (MIKE ECO Lab constants)."""
    MUID = "MUID"
    """ID"""
    ECOLABTemplateID = "ECOLABTemplateID"
    """MIKE ECO Lab template"""
    CoeffID = "CoeffID"
    """Constant ID"""
    ID = "ID"
    """ID"""
    ConstantTypeNo = "ConstantTypeNo"
    """Constant type"""
    Value = "Value"
    """Global value"""
    FileName = "FileName"
    """File name"""
    FileItem = "FileItem"
    """Item ID"""
    FileItemNo = "FileItemNo"
    """FileItemNo"""
    Description = "Description"
    """Description"""
    BuildinID = "BuildinID"
    """BuildinID"""
    SpatialVar = "SpatialVar"
    """SpatialVar"""
    InterpolateNo = "InterpolateNo"
    """Interpolate this constant between local values"""

class msm_ECOLABCoeffTable(BaseTable):
    """Table for msm_ECOLABCoeff (MIKE ECO Lab constants)."""
    
    @property
    def columns(self) -> msm_ECOLABCoeffTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = msm_ECOLABCoeffTableColumns(self)
        return self._columns