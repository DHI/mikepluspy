from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class msm_BBoundaryTableColumns(BaseColumns):
    """Column names for msm_BBoundary (Boundary conditions)."""
    MUID = "MUID"
    TypeNo = "TypeNo"
    GroupNo = "GroupNo"
    GridTypeNo = "GridTypeNo"
    ApplyBoundaryNo = "ApplyBoundaryNo"
    LoadTypeNo = "LoadTypeNo"
    FlowTypeNo = "FlowTypeNo"
    ConnectionTypeNo = "ConnectionTypeNo"
    ListName = "ListName"
    LoadCategoryNo = "LoadCategoryNo"
    SourceLocationNo = "SourceLocationNo"
    SourceXCoor = "SourceXCoor"
    SourceYCoor = "SourceYCoor"
    CatchID = "CatchID"
    NodeID = "NodeID"
    LinkID = "LinkID"
    RiverMuid = "RiverMuid"
    Chainage = "Chainage"
    StorageID = "StorageID"
    RiverLocationNo = "RiverLocationNo"
    RiverSrcTypeNo = "RiverSrcTypeNo"
    RiverSrcUSChainage = "RiverSrcUSChainage"
    RiverSrcDSChainage = "RiverSrcDSChainage"
    Distance = "Distance"
    DistributeNo = "DistributeNo"
    CatchLoadNo = "CatchLoadNo"
    VariationNo = "VariationNo"
    ConstantValue = "ConstantValue"
    StartupNo = "StartupNo"
    StartupTime = "StartupTime"
    StartupValue = "StartupValue"
    CyclicValue = "CyclicValue"
    DPProfileID = "DPProfileID"
    TSConnection = "TSConnection"
    TimeseriesName = "TimeseriesName"
    DataTypeName = "DataTypeName"
    TSConnTypeNo = "TSConnTypeNo"
    VariationDicrctionNo = "VariationDicrctionNo"
    ConstantDicrctionValue = "ConstantDicrctionValue"
    TSConnectionDicrction = "TSConnectionDicrction"
    TimeseriesNameDicrction = "TimeseriesNameDicrction"
    DataTypeNameDicrction = "DataTypeNameDicrction"
    ValidityIntervalNo = "ValidityIntervalNo"
    ValidityBegin = "ValidityBegin"
    ValidityEnd = "ValidityEnd"
    Fraction = "Fraction"
    RiverQHRelation = "RiverQHRelation"
    Description = "Description"

class msm_BBoundaryTable(BaseTable):
    """Table for msm_BBoundary (Boundary conditions)."""
    
    @property
    def columns(self) -> msm_BBoundaryTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = msm_BBoundaryTableColumns(self)
        return self._columns