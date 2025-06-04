from mikeplus.tables.base_geometry_table import BaseGeometryTable
from mikeplus.tables.base_geometry_table import BaseColumns

class msm_CatchConTableColumns(BaseColumns):
    """Column names for msm_CatchCon (Catchment connections)."""
    MUID = "MUID"
    """ID"""
    CatchID = "CatchID"
    """Catchment ID"""
    TypeNo = "TypeNo"
    """Type"""
    NodeID = "NodeID"
    """Node/Storage ID"""
    LinkID = "LinkID"
    """Link ID"""
    LinkNo = "LinkNo"
    """LinkNo"""
    StartChainage = "StartChainage"
    """Start chainage [m]"""
    EndChainage = "EndChainage"
    """End chainage [m]"""
    LoadTypeNo = "LoadTypeNo"
    """Load type"""
    RRFraction = "RRFraction"
    """Fraction of catchment runoff [%]"""
    PEFraction = "PEFraction"
    """Fraction of catchment discharge [%]"""
    RoutingTypeNo = "RoutingTypeNo"
    """Method"""
    RoutingDelay = "RoutingDelay"
    """Delay parameter [min]"""
    RoutingShape = "RoutingShape"
    """Shape parameter [()]"""
    Description = "Description"
    """Description"""

class msm_CatchConTable(BaseGeometryTable):
    """Table for msm_CatchCon (Catchment connections)."""
    
    @property
    def columns(self) -> msm_CatchConTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = msm_CatchConTableColumns(self)
        return self._columns