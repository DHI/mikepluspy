from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class msm_ECOLABForcingTableColumns(BaseColumns):
    """Column names for msm_ECOLABForcing (MIKE ECO Lab forcings)."""
    MUID = "MUID"
    """ID"""
    ECOLABTemplateID = "ECOLABTemplateID"
    """MIKE ECO Lab template"""
    ForcingID = "ForcingID"
    """Forcing"""
    ID = "ID"
    """ID"""
    TSTypeNo = "TSTypeNo"
    """TS type"""
    Value = "Value"
    """Value"""
    Unit = "Unit"
    """Unit"""
    TSFileName = "TSFileName"
    """File name"""
    TSItemNo = "TSItemNo"
    """TSItemNo"""
    TSItemID = "TSItemID"
    """Item ID"""
    DfsFileName = "DfsFileName"
    """File name"""
    DfsItemNo = "DfsItemNo"
    """DfsItemNo"""
    DfsItemID = "DfsItemID"
    """Item ID"""
    Description = "Description"
    """Description"""
    BuildinID = "BuildinID"
    """BuildinID"""
    SpatialVar = "SpatialVar"
    """SpatialVar"""

class msm_ECOLABForcingTable(BaseTable):
    """Table for msm_ECOLABForcing (MIKE ECO Lab forcings)."""
    
    @property
    def columns(self) -> msm_ECOLABForcingTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = msm_ECOLABForcingTableColumns(self)
        return self._columns