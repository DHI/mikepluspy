from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class mw_PumpStationTableColumns(BaseColumns):
    """Column names for mw_PumpStation (Pump stations)."""
    MUID = "MUID"
    GeomCentroidX = "GeomCentroidX"
    GeomCentroidY = "GeomCentroidY"
    GeomArea = "GeomArea"
    Comment = "Comment"
    Picture = "Picture"
    Description = "Description"
    Note = "Note"

class mw_PumpStationTable(BaseTable):
    """Table for mw_PumpStation (Pump stations)."""
    
    @property
    def columns(self) -> mw_PumpStationTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mw_PumpStationTableColumns(self)
        return self._columns