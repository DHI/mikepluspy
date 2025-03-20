from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class msm_ResultSelectionQuantityTableColumns(BaseColumns):
    """Column names for msm_ResultSelectionQuantity (msm_ResultSelectionQuantity)."""
    MUID = "MUID"
    ResultSelectionID = "ResultSelectionID"
    QuantityID = "QuantityID"

class msm_ResultSelectionQuantityTable(BaseTable):
    """Table for msm_ResultSelectionQuantity (msm_ResultSelectionQuantity)."""
    
    @property
    def columns(self) -> msm_ResultSelectionQuantityTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = msm_ResultSelectionQuantityTableColumns(self)
        return self._columns