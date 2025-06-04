from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class ms_ProcessedCRSDTableColumns(BaseColumns):
    """Column names for ms_ProcessedCRSD (Processed data)."""
    MUID = "MUID"
    """MUID"""
    CrsID = "CrsID"
    """CrsID"""
    Sqn = "Sqn"
    """Sqn"""
    Level = "Level"
    """Level [m]"""
    FlowArea = "FlowArea"
    """Cross section area [m^2]"""
    Radii = "Radii"
    """Radius [m]"""
    StorageWidth = "StorageWidth"
    """Storage width [m]"""
    AdditionalSurfaceArea = "AdditionalSurfaceArea"
    """Add. storage area [m^2]"""
    ResistanceFactor = "ResistanceFactor"
    """Resistance [()]"""
    Conveyence = "Conveyence"
    """Conveyance [m^3/s]"""

class ms_ProcessedCRSDTable(BaseTable):
    """Table for ms_ProcessedCRSD (Processed data)."""
    
    @property
    def columns(self) -> ms_ProcessedCRSDTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = ms_ProcessedCRSDTableColumns(self)
        return self._columns