from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class m2d_ADPrecipitationDTableColumns(BaseColumns):
    """Column names for m2d_ADPrecipitationD (AD precipitation area in 2D domain)."""
    MUID = "MUID"
    PrecipID = "PrecipID"
    Sqn = "Sqn"
    ApplyNo = "ApplyNo"
    AreaID = "AreaID"
    LocalPrecip = "LocalPrecip"
    Description = "Description"

class m2d_ADPrecipitationDTable(BaseTable):
    """Table for m2d_ADPrecipitationD (AD precipitation area in 2D domain)."""
    
    @property
    def columns(self) -> m2d_ADPrecipitationDTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = m2d_ADPrecipitationDTableColumns(self)
        return self._columns