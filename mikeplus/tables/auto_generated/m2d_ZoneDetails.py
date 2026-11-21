from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class m2d_ZoneDetailsTableColumns(BaseColumns):
    """Column names for m2d_ZoneDetails (2D zone details)."""
    MUID = "MUID"
    """ID"""
    ZoneTypeNo = "ZoneTypeNo"
    """Zone type"""
    ZoneID = "ZoneID"
    """Zone ID"""
    IncludeNo = "IncludeNo"
    """Include"""
    TypeNo = "TypeNo"
    """Type"""
    ConstValue = "ConstValue"
    """Constant value [mm/h]"""
    TimeseriesFilePath = "TimeseriesFilePath"
    """File name"""
    TimeseriesItemName = "TimeseriesItemName"
    """Item"""
    TimeseriesItemNo = "TimeseriesItemNo"
    """TimeseriesItemNo"""
    Browse = "Browse"
    """Browse"""

class m2d_ZoneDetailsTable(BaseTable):
    """Table for m2d_ZoneDetails (2D zone details)."""
    
    @property
    def columns(self) -> m2d_ZoneDetailsTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = m2d_ZoneDetailsTableColumns(self)
        return self._columns