from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class ms_2DTabD_Bridge_USBPR_velocity_distributionTableColumns(BaseColumns):
    """Column names for ms_2DTabD_Bridge_USBPR_velocity_distribution ()."""
    MUID = "MUID"
    """MUID"""
    MasterID = "MasterID"
    """MasterID"""
    RowSqn = "RowSqn"
    """RowSqn"""
    ColSqn = "ColSqn"
    """ColSqn"""
    RowHeaderValue = "RowHeaderValue"
    """RowHeaderValue"""
    ColHeaderValue = "ColHeaderValue"
    """ColHeaderValue"""
    CellValue = "CellValue"
    """CellValue"""

class ms_2DTabD_Bridge_USBPR_velocity_distributionTable(BaseTable):
    """Table for ms_2DTabD_Bridge_USBPR_velocity_distribution ()."""
    
    @property
    def columns(self) -> ms_2DTabD_Bridge_USBPR_velocity_distributionTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = ms_2DTabD_Bridge_USBPR_velocity_distributionTableColumns(self)
        return self._columns