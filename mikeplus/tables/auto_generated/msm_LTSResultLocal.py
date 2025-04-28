from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class msm_LTSResultLocalTableColumns(BaseColumns):
    """Column names for msm_LTSResultLocal (Statistics specifications)."""
    MUID = "MUID"
    ElementTypeNo = "ElementTypeNo"
    ResultNo = "ResultNo"
    StatLocationNo = "StatLocationNo"
    StatLocation = "StatLocation"
    SaveNo = "SaveNo"
    EventLimit = "EventLimit"

class msm_LTSResultLocalTable(BaseTable):
    """Table for msm_LTSResultLocal (Statistics specifications)."""
    
    @property
    def columns(self) -> msm_LTSResultLocalTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = msm_LTSResultLocalTableColumns(self)
        return self._columns