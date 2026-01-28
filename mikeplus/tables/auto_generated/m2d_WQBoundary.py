from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class m2d_WQBoundaryTableColumns(BaseColumns):
    """Column names for m2d_WQBoundary (2D WQ boundaries)."""
    MUID = "MUID"
    """ID"""
    TypeNo = "TypeNo"
    """Type"""
    BndTypeNo = "BndTypeNo"
    """Type"""
    BoundaryID = "BoundaryID"
    """2D boundary ID"""
    ComponentID = "ComponentID"
    """Component ID"""
    TimeTypeNo = "TimeTypeNo"
    """HD type"""
    ConstValue = "ConstValue"
    """Constant value"""
    ConstStartupNo = "ConstStartupNo"
    """Gradual start up, constant"""
    ConstStartValue = "ConstStartValue"
    """From, constant"""
    ConstTimeInterval = "ConstTimeInterval"
    """Time, constant [sec]"""
    VarStartupNo = "VarStartupNo"
    """Gradual start up, varying"""
    VarStartValue = "VarStartValue"
    """From, varying"""
    VarTimeInterval = "VarTimeInterval"
    """Time, varying [sec]"""
    WaterFilePath = "WaterFilePath"
    """File"""
    WaterItemNo = "WaterItemNo"
    """WaterItemNo"""
    WaterItemName = "WaterItemName"
    """Item"""
    InterpolationTypeNo = "InterpolationTypeNo"
    """Interpolation type in time"""
    SpatialOrderNo = "SpatialOrderNo"
    """Spatial order along boundary"""
    Description = "Description"
    """Description"""
    Unit = "Unit"
    """Unit"""

class m2d_WQBoundaryTable(BaseTable):
    """Table for m2d_WQBoundary (2D WQ boundaries)."""
    
    @property
    def columns(self) -> m2d_WQBoundaryTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = m2d_WQBoundaryTableColumns(self)
        return self._columns