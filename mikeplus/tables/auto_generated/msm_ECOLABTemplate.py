from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class msm_ECOLABTemplateTableColumns(BaseColumns):
    """Column names for msm_ECOLABTemplate (MIKE ECO Lab templates)."""
    MUID = "MUID"
    """ID"""
    ApplyNo = "ApplyNo"
    """Apply"""
    TemplateNo = "TemplateNo"
    """Template"""
    TemplateFilename = "TemplateFilename"
    """File name"""
    TypeNo = "TypeNo"
    """Type"""
    ConnectionTypeNo = "ConnectionTypeNo"
    """Connection type"""
    ListID = "ListID"
    """List ID"""
    NodeID = "NodeID"
    """Node ID"""
    LinkID = "LinkID"
    """Link ID"""
    Description = "Description"
    """Description"""

class msm_ECOLABTemplateTable(BaseTable):
    """Table for msm_ECOLABTemplate (MIKE ECO Lab templates)."""
    
    @property
    def columns(self) -> msm_ECOLABTemplateTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = msm_ECOLABTemplateTableColumns(self)
        return self._columns