from mikeplus.tables.base_geometry_table import BaseGeometryTable
from mikeplus.tables.base_geometry_table import BaseColumns

class m2d_BoundaryTableColumns(BaseColumns):
    """Column names for m2d_Boundary (2D boundary conditions)."""
    MUID = "MUID"
    ApplyNo = "ApplyNo"
    BndTypeNo = "BndTypeNo"
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
    ConstInitVelApplyNo = "ConstInitVelApplyNo"
    Discharge = "Discharge"
    UVelocity = "UVelocity"
    VVelocity = "VVelocity"
    VarInitVelApplyNo = "VarInitVelApplyNo"
    SourceFilePath = "SourceFilePath"
    SrcDisItemName = "SrcDisItemName"
    SrcUVelItemName = "SrcUVelItemName"
    SrcVVelItemName = "SrcVVelItemName"
    QhDisFilePath = "QhDisFilePath"
    QhDisItemNo = "QhDisItemNo"
    QhDisItemName = "QhDisItemName"
    QhVelocityFilePath = "QhVelocityFilePath"
    QhUVelItemNo = "QhUVelItemNo"
    QhUVelItemName = "QhUVelItemName"
    QhVVelItemNo = "QhVVelItemNo"
    QhVVelItemName = "QhVVelItemName"
    QHStartupNo = "QHStartupNo"
    QHStartValue = "QHStartValue"
    QHTimeInterval = "QHTimeInterval"
    VelDefTypeNo = "VelDefTypeNo"
    InterpolationTypeNo = "InterpolationTypeNo"
    SpatialOrderNo = "SpatialOrderNo"
    SourceTypeNo = "SourceTypeNo"
    Source1X = "Source1X"
    Source1Y = "Source1Y"
    Source2X = "Source2X"
    Source2Y = "Source2Y"
    Description = "Description"
    BndGeomLine = "BndGeomLine"
    SrcDisItemNo = "SrcDisItemNo"
    SrcUVelItemNo = "SrcUVelItemNo"
    SrcVVelItemNo = "SrcVVelItemNo"

class m2d_BoundaryTable(BaseGeometryTable):
    """Table for m2d_Boundary (2D boundary conditions)."""
    
    @property
    def columns(self) -> m2d_BoundaryTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = m2d_BoundaryTableColumns(self)
        return self._columns