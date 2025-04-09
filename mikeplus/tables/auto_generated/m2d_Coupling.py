from mikeplus.tables.base_geometry_table import BaseGeometryTable
from mikeplus.tables.base_geometry_table import BaseColumns

class m2d_CouplingTableColumns(BaseColumns):
    """Column names for m2d_Coupling (1D-2D couplings)."""
    MUID = "MUID"
    TypeNo = "TypeNo"
    CoupleModelNo = "CoupleModelNo"
    ApplyNo = "ApplyNo"
    ItemID = "ItemID"
    RecalculationCoordinateNo = "RecalculationCoordinateNo"
    Uschainage = "Uschainage"
    Dschainage = "Dschainage"
    SideNo = "SideNo"
    SquareWidth = "SquareWidth"
    RiverEndNo = "RiverEndNo"
    FlowDistributionNo = "FlowDistributionNo"
    RiverStruID = "RiverStruID"
    NodeID = "NodeID"
    RiverDistance = "RiverDistance"
    DeltaDepth = "DeltaDepth"
    Smoothing = "Smoothing"
    WeirTypeNo = "WeirTypeNo"
    WeirCoef = "WeirCoef"
    CrestSourceNo = "CrestSourceNo"
    CrestTable = "CrestTable"
    FilePath = "FilePath"
    FileItemName = "FileItemName"
    MaxQcheckNo = "MaxQcheckNo"
    MaxQvalue = "MaxQvalue"
    FlowMethodNo = "FlowMethodNo"
    DischCoef = "DischCoef"
    InletArea = "InletArea"
    CrestWidth = "CrestWidth"
    Coefficient = "Coefficient"
    Exponent = "Exponent"
    Freeboard = "Freeboard"
    DQRelationID = "DQRelationID"

class m2d_CouplingTable(BaseGeometryTable):
    """Table for m2d_Coupling (1D-2D couplings)."""
    
    @property
    def columns(self) -> m2d_CouplingTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = m2d_CouplingTableColumns(self)
        return self._columns