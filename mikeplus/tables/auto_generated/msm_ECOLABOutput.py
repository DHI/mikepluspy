from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class msm_ECOLABOutputTableColumns(BaseColumns):
    """Column names for msm_ECOLABOutput (ECOLAB Output)."""
    MUID = "MUID"
    ECOLabTemplateID = "ECOLabTemplateID"
    ECOLabTypeNo = "ECOLabTypeNo"
    ECOLabOutputNo = "ECOLabOutputNo"
    ECOLabOutputText = "ECOLabOutputText"
    ECOLabOutputSymbol = "ECOLabOutputSymbol"
    ECOLabDimNo = "ECOLabDimNo"
    ECOLabUnit = "ECOLabUnit"
    ECOLabEUMUnit = "ECOLabEUMUnit"

class msm_ECOLABOutputTable(BaseTable):
    """Table for msm_ECOLABOutput (ECOLAB Output)."""
    
    @property
    def columns(self) -> msm_ECOLABOutputTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = msm_ECOLABOutputTableColumns(self)
        return self._columns