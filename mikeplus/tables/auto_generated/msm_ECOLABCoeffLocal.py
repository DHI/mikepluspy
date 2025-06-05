from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class msm_ECOLABCoeffLocalTableColumns(BaseColumns):
    """Column names for msm_ECOLABCoeffLocal (MIKE ECO LAB constants local values)."""
    MUID = "MUID"
    """ID"""
    CoefID = "CoefID"
    """CoefID"""
    LocTypeNo = "LocTypeNo"
    """Location type"""
    ListID = "ListID"
    """List ID"""
    NodeID = "NodeID"
    """Node/Storage ID"""
    LinkID = "LinkID"
    """Link ID"""
    StartChainage = "StartChainage"
    """Start chainage [m]"""
    EndChainage = "EndChainage"
    """End chainage [m]"""
    LinkNo = "LinkNo"
    """LinkNo"""
    Value = "Value"
    """Value"""

class msm_ECOLABCoeffLocalTable(BaseTable):
    """Table for msm_ECOLABCoeffLocal (MIKE ECO LAB constants local values)."""
    
    @property
    def columns(self) -> msm_ECOLABCoeffLocalTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = msm_ECOLABCoeffLocalTableColumns(self)
        return self._columns