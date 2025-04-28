from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class m2d_WQBoundaryTableColumns(BaseColumns):
    """Column names for m2d_WQBoundary (2D WQ boundaries)."""
    MUID = "MUID"
    TypeNo = "TypeNo"
    BndTypeNo = "BndTypeNo"
    BoundaryID = "BoundaryID"
    ComponentID = "ComponentID"
    TimeTypeNo = "TimeTypeNo"
    ConstValue = "ConstValue"
    ConstStartupNo = "ConstStartupNo"
    ConstStartValue = "ConstStartValue"
    ConstTimeInterval = "ConstTimeInterval"
    VarStartupNo = "VarStartupNo"
    VarStartValue = "VarStartValue"
    VarTimeInterval = "VarTimeInterval"
    WaterFilePath = "WaterFilePath"
    WaterItemNo = "WaterItemNo"
    WaterItemName = "WaterItemName"
    InterpolationTypeNo = "InterpolationTypeNo"
    SpatialOrderNo = "SpatialOrderNo"
    Description = "Description"
    Unit = "Unit"

class m2d_WQBoundaryTable(BaseTable):
    """Table for m2d_WQBoundary (2D WQ boundaries)."""
    
    @property
    def columns(self) -> m2d_WQBoundaryTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = m2d_WQBoundaryTableColumns(self)
        return self._columns