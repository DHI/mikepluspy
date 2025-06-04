from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class msm_RSTableColumns(BaseColumns):
    """Column names for msm_RS (Result files)."""
    MUID = "MUID"
    """ID"""
    ModelTypeNo = "ModelTypeNo"
    """Model type"""
    ContentTypeNo = "ContentTypeNo"
    """Content type"""
    FormatNo = "FormatNo"
    """Format"""
    DefaultNo = "DefaultNo"
    """DefaultNo"""

class msm_RSTable(BaseTable):
    """Table for msm_RS (Result files)."""
    
    @property
    def columns(self) -> msm_RSTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = msm_RSTableColumns(self)
        return self._columns