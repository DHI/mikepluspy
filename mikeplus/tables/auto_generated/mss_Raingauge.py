from mikeplus.tables.base_node_table import BaseNodeTable
from mikeplus.tables.base_node_table import BaseColumns

class mss_RaingaugeTableColumns(BaseColumns):
    """Column names for mss_Raingauge (Raingauge)."""
    MUID = "MUID"
    """ID"""
    GeomX = "GeomX"
    """X coordinate [m]"""
    GeomY = "GeomY"
    """Y coordinate [m]"""
    TypeNo = "TypeNo"
    """Source data format"""
    FileNameSeries = "FileNameSeries"
    """File"""
    StationName = "StationName"
    """Station name"""
    UnitNo = "UnitNo"
    """Unit type"""
    TimeSeriesID = "TimeSeriesID"
    """TimeSeries ID"""
    FormNo = "FormNo"
    """Format"""
    TimeInterval = "TimeInterval"
    """Time interval [h]"""
    Scf = "Scf"
    """Snow catch deficiency correction factor, SCF"""
    Description = "Description"
    """Description"""
    Tag = "Tag"
    """Tag"""

class mss_RaingaugeTable(BaseNodeTable):
    """Table for mss_Raingauge (Raingauge)."""
    
    @property
    def columns(self) -> mss_RaingaugeTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mss_RaingaugeTableColumns(self)
        return self._columns