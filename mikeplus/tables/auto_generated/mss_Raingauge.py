from mikeplus.tables.base_node_table import BaseNodeTable
from mikeplus.tables.base_node_table import BaseColumns

class mss_RaingaugeTableColumns(BaseColumns):
    """Column names for mss_Raingauge (Raingauge)."""
    MUID = "MUID"
    GeomX = "GeomX"
    GeomY = "GeomY"
    TypeNo = "TypeNo"
    FileNameSeries = "FileNameSeries"
    StationName = "StationName"
    UnitNo = "UnitNo"
    TimeSeriesID = "TimeSeriesID"
    FormNo = "FormNo"
    TimeInterval = "TimeInterval"
    Scf = "Scf"
    Description = "Description"
    Tag = "Tag"

class mss_RaingaugeTable(BaseNodeTable):
    """Table for mss_Raingauge (Raingauge)."""
    
    @property
    def columns(self) -> mss_RaingaugeTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mss_RaingaugeTableColumns(self)
        return self._columns