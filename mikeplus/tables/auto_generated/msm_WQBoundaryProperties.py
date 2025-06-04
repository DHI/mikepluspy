from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class msm_WQBoundaryPropertiesTableColumns(BaseColumns):
    """Column names for msm_WQBoundaryProperties (WQ boundary properties)."""
    MUID = "MUID"
    """ID"""
    Enabled = "Enabled"
    """Apply"""
    BoundaryID = "BoundaryID"
    """Boundary ID"""
    WQBoundaryTypeNo = "WQBoundaryTypeNo"
    """Type"""
    TrapComponentID = "TrapComponentID"
    """WQ component"""
    TrapFractionID = "TrapFractionID"
    """Sediment fraction"""
    VariationNo = "VariationNo"
    """Variation No"""
    ConstantValue = "ConstantValue"
    """Constant value"""
    Unit = "Unit"
    """Unit"""
    StartupNo = "StartupNo"
    """Gradual start up"""
    StartupTime = "StartupTime"
    """Time [min]"""
    StartupValue = "StartupValue"
    """From"""
    CyclicValue = "CyclicValue"
    """Cyclic value"""
    DPProfileID = "DPProfileID"
    """Pattern"""
    TSConnection = "TSConnection"
    """File name"""
    TimeseriesName = "TimeseriesName"
    """Time series ID"""
    SWQ_TableID = "SWQ_TableID"
    """Table ID"""
    SWQ_SetupID = "SWQ_SetupID"
    """SWQ ID"""
    DataTypeName = "DataTypeName"
    """Data type"""
    Fraction = "Fraction"
    """Scale factor"""
    THalving = "THalving"
    """Halving time [h]"""
    Description = "Description"
    """Description"""

class msm_WQBoundaryPropertiesTable(BaseTable):
    """Table for msm_WQBoundaryProperties (WQ boundary properties)."""
    
    @property
    def columns(self) -> msm_WQBoundaryPropertiesTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = msm_WQBoundaryPropertiesTableColumns(self)
        return self._columns