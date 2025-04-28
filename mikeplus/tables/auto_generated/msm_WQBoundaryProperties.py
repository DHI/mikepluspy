from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class msm_WQBoundaryPropertiesTableColumns(BaseColumns):
    """Column names for msm_WQBoundaryProperties (WQ boundary properties)."""
    MUID = "MUID"
    Enabled = "Enabled"
    BoundaryID = "BoundaryID"
    WQBoundaryTypeNo = "WQBoundaryTypeNo"
    TrapComponentID = "TrapComponentID"
    TrapFractionID = "TrapFractionID"
    VariationNo = "VariationNo"
    ConstantValue = "ConstantValue"
    Unit = "Unit"
    StartupNo = "StartupNo"
    StartupTime = "StartupTime"
    StartupValue = "StartupValue"
    CyclicValue = "CyclicValue"
    DPProfileID = "DPProfileID"
    TSConnection = "TSConnection"
    TimeseriesName = "TimeseriesName"
    SWQ_TableID = "SWQ_TableID"
    SWQ_SetupID = "SWQ_SetupID"
    DataTypeName = "DataTypeName"
    Fraction = "Fraction"
    THalving = "THalving"
    Description = "Description"

class msm_WQBoundaryPropertiesTable(BaseTable):
    """Table for msm_WQBoundaryProperties (WQ boundary properties)."""
    
    @property
    def columns(self) -> msm_WQBoundaryPropertiesTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = msm_WQBoundaryPropertiesTableColumns(self)
        return self._columns