from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class msm_ECOLABTemplateTableColumns(BaseColumns):
    """Column names for msm_ECOLABTemplate (MIKE ECO Lab templates)."""
    MUID = "MUID"
    ApplyNo = "ApplyNo"
    TemplateNo = "TemplateNo"
    TemplateFilename = "TemplateFilename"
    TypeNo = "TypeNo"
    ConnectionTypeNo = "ConnectionTypeNo"
    ListID = "ListID"
    NodeID = "NodeID"
    LinkID = "LinkID"
    Description = "Description"

class msm_ECOLABTemplateTable(BaseTable):
    """Table for msm_ECOLABTemplate (MIKE ECO Lab templates)."""
    
    @property
    def columns(self) -> msm_ECOLABTemplateTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = msm_ECOLABTemplateTableColumns(self)
        return self._columns