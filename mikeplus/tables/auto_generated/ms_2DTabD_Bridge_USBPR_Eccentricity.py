from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class ms_2DTabD_Bridge_USBPR_EccentricityTableColumns(BaseColumns):
    """Column names for ms_2DTabD_Bridge_USBPR_Eccentricity ()."""
    MUID = "MUID"
    MasterID = "MasterID"
    RowSqn = "RowSqn"
    ColSqn = "ColSqn"
    RowHeaderValue = "RowHeaderValue"
    ColHeaderValue = "ColHeaderValue"
    CellValue = "CellValue"

class ms_2DTabD_Bridge_USBPR_EccentricityTable(BaseTable):
    """Table for ms_2DTabD_Bridge_USBPR_Eccentricity ()."""
    
    @property
    def columns(self) -> ms_2DTabD_Bridge_USBPR_EccentricityTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = ms_2DTabD_Bridge_USBPR_EccentricityTableColumns(self)
        return self._columns