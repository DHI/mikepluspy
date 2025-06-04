from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class msm_ADInitialConditionLocalTableColumns(BaseColumns):
    """Column names for msm_ADInitialConditionLocal (Local values)."""
    MUID = "MUID"
    """ID"""
    ADInitCondID = "ADInitCondID"
    """ADInitCondID"""
    Sqn = "Sqn"
    """Sqn"""
    Description = "Description"
    """Description"""
    LocationTypeNo = "LocationTypeNo"
    """Location type"""
    ListID = "ListID"
    """List ID"""
    NodeID = "NodeID"
    """Node ID"""
    LinkID = "LinkID"
    """Link ID"""
    LinkNo = "LinkNo"
    """LinkNo"""
    StartChainage = "StartChainage"
    """Start chainage [m]"""
    EndChainage = "EndChainage"
    """End chainage [m]"""

class msm_ADInitialConditionLocalTable(BaseTable):
    """Table for msm_ADInitialConditionLocal (Local values)."""
    
    @property
    def columns(self) -> msm_ADInitialConditionLocalTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = msm_ADInitialConditionLocalTableColumns(self)
        return self._columns