from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class msm_ECOLABOutputTableColumns(BaseColumns):
    """Column names for msm_ECOLABOutput (ECOLAB Output)."""
    MUID = "MUID"
    """MUID"""
    ECOLabTemplateID = "ECOLabTemplateID"
    """ECOLabTemplateID"""
    ECOLabTypeNo = "ECOLabTypeNo"
    """ECOLabTypeNo"""
    ECOLabOutputNo = "ECOLabOutputNo"
    """ECOLabOutputNo"""
    ECOLabOutputText = "ECOLabOutputText"
    """ECOLabOutputText"""
    ECOLabOutputSymbol = "ECOLabOutputSymbol"
    """ECOLabOutputSymbol"""
    ECOLabDimNo = "ECOLabDimNo"
    """ECOLabDimNo"""
    ECOLabUnit = "ECOLabUnit"
    """ECOLabUnit"""
    ECOLabEUMUnit = "ECOLabEUMUnit"
    """ECOLabEUMUnit"""

class msm_ECOLABOutputTable(BaseTable):
    """Table for msm_ECOLABOutput (ECOLAB Output)."""
    
    @property
    def columns(self) -> msm_ECOLABOutputTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = msm_ECOLABOutputTableColumns(self)
        return self._columns