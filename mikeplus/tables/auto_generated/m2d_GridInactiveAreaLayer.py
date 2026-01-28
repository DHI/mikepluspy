from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class m2d_GridInactiveAreaLayerTableColumns(BaseColumns):
    """Column names for m2d_GridInactiveAreaLayer (Grid inactive area layer)."""
    MUID = "MUID"
    FilePath = "FilePath"
    ApplyNo = "ApplyNo"

class m2d_GridInactiveAreaLayerTable(BaseTable):
    """Table for m2d_GridInactiveAreaLayer (Grid inactive area layer)."""
    
    @property
    def columns(self) -> m2d_GridInactiveAreaLayerTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = m2d_GridInactiveAreaLayerTableColumns(self)
        return self._columns