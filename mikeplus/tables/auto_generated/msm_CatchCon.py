from mikeplus.tables.base_geometry_table import BaseGeometryTable
from mikeplus.tables.base_geometry_table import BaseColumns

class msm_CatchConTableColumns(BaseColumns):
    """Column names for msm_CatchCon (Catchment connections)."""
    MUID = "MUID"
    CatchID = "CatchID"
    TypeNo = "TypeNo"
    NodeID = "NodeID"
    LinkID = "LinkID"
    LinkNo = "LinkNo"
    StartChainage = "StartChainage"
    EndChainage = "EndChainage"
    LoadTypeNo = "LoadTypeNo"
    RRFraction = "RRFraction"
    PEFraction = "PEFraction"
    RoutingTypeNo = "RoutingTypeNo"
    RoutingDelay = "RoutingDelay"
    RoutingShape = "RoutingShape"
    Description = "Description"

class msm_CatchConTable(BaseGeometryTable):
    """Table for msm_CatchCon (Catchment connections)."""
    
    @property
    def columns(self) -> msm_CatchConTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = msm_CatchConTableColumns(self)
        return self._columns