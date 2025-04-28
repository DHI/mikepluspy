from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class msm_ECOLABForcingTableColumns(BaseColumns):
    """Column names for msm_ECOLABForcing (MIKE ECO Lab forcings)."""
    MUID = "MUID"
    ECOLABTemplateID = "ECOLABTemplateID"
    ForcingID = "ForcingID"
    ID = "ID"
    TSTypeNo = "TSTypeNo"
    Value = "Value"
    Unit = "Unit"
    TSFileName = "TSFileName"
    TSItemNo = "TSItemNo"
    TSItemID = "TSItemID"
    DfsFileName = "DfsFileName"
    DfsItemNo = "DfsItemNo"
    DfsItemID = "DfsItemID"
    Description = "Description"
    BuildinID = "BuildinID"
    SpatialVar = "SpatialVar"

class msm_ECOLABForcingTable(BaseTable):
    """Table for msm_ECOLABForcing (MIKE ECO Lab forcings)."""
    
    @property
    def columns(self) -> msm_ECOLABForcingTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = msm_ECOLABForcingTableColumns(self)
        return self._columns