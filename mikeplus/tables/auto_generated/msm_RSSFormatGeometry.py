from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class msm_RSSFormatGeometryTableColumns(BaseColumns):
    """Column names for msm_RSSFormatGeometry (Result selection geometry)."""
    MUID = "MUID"
    """ID"""
    SelectionID = "SelectionID"
    """SelectionID"""
    Sqn = "Sqn"
    """Sqn"""
    LinkID = "LinkID"
    """Link ID"""
    UpStreamChainage = "UpStreamChainage"
    """Upstream chainage [m]"""
    DownStreamChainage = "DownStreamChainage"
    """Downstream chainage [m]"""

class msm_RSSFormatGeometryTable(BaseTable):
    """Table for msm_RSSFormatGeometry (Result selection geometry)."""
    
    @property
    def columns(self) -> msm_RSSFormatGeometryTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = msm_RSSFormatGeometryTableColumns(self)
        return self._columns