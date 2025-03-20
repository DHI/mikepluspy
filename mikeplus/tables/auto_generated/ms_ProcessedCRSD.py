from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class ms_ProcessedCRSDTableColumns(BaseColumns):
    """Column names for ms_ProcessedCRSD (Processed data)."""
    MUID = "MUID"
    CrsID = "CrsID"
    Sqn = "Sqn"
    Level = "Level"
    FlowArea = "FlowArea"
    Radii = "Radii"
    StorageWidth = "StorageWidth"
    AdditionalSurfaceArea = "AdditionalSurfaceArea"
    ResistanceFactor = "ResistanceFactor"
    Conveyence = "Conveyence"

class ms_ProcessedCRSDTable(BaseTable):
    """Table for ms_ProcessedCRSD (Processed data)."""
    
    @property
    def columns(self) -> ms_ProcessedCRSDTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = ms_ProcessedCRSDTableColumns(self)
        return self._columns