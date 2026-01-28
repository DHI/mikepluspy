from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class msm_HDInitialConditionLocalTableColumns(BaseColumns):
    """Column names for msm_HDInitialConditionLocal (Local values)."""
    MUID = "MUID"
    """ID"""
    InitCondID = "InitCondID"
    """InitCondID"""
    Sqn = "Sqn"
    """Sqn"""
    Description = "Description"
    """Description"""
    LocationTypeNo = "LocationTypeNo"
    """Location type"""
    ListID = "ListID"
    """List ID"""
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
    LevelDepthTypeNo = "LevelDepthTypeNo"
    """Level type"""
    LevelDepth = "LevelDepth"
    """Level depth [m]"""
    DischargeTypeNo = "DischargeTypeNo"
    """Discharge type"""
    Discharge = "Discharge"
    """Discharge [m^3/s]"""

class msm_HDInitialConditionLocalTable(BaseTable):
    """Table for msm_HDInitialConditionLocal (Local values)."""
    
    @property
    def columns(self) -> msm_HDInitialConditionLocalTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = msm_HDInitialConditionLocalTableColumns(self)
        return self._columns