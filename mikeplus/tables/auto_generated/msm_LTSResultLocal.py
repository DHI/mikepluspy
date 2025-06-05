from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class msm_LTSResultLocalTableColumns(BaseColumns):
    """Column names for msm_LTSResultLocal (Statistics specifications)."""
    MUID = "MUID"
    """MUID"""
    ElementTypeNo = "ElementTypeNo"
    """Element type"""
    ResultNo = "ResultNo"
    """Result type"""
    StatLocationNo = "StatLocationNo"
    """Location type"""
    StatLocation = "StatLocation"
    """Location"""
    SaveNo = "SaveNo"
    """Save type"""
    EventLimit = "EventLimit"
    """Limit"""

class msm_LTSResultLocalTable(BaseTable):
    """Table for msm_LTSResultLocal (Statistics specifications)."""
    
    @property
    def columns(self) -> msm_LTSResultLocalTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = msm_LTSResultLocalTableColumns(self)
        return self._columns