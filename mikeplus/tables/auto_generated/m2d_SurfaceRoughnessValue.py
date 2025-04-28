from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class m2d_SurfaceRoughnessValueTableColumns(BaseColumns):
    """Column names for m2d_SurfaceRoughnessValue (2D surface roughness)."""
    MUID = "MUID"
    Sqn = "Sqn"
    CodeValue = "CodeValue"
    RoughnessVal = "RoughnessVal"
    FunctionOf = "FunctionOf"
    RoughnessCurveID = "RoughnessCurveID"
    DataSourceType = "DataSourceType"

class m2d_SurfaceRoughnessValueTable(BaseTable):
    """Table for m2d_SurfaceRoughnessValue (2D surface roughness)."""
    
    @property
    def columns(self) -> m2d_SurfaceRoughnessValueTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = m2d_SurfaceRoughnessValueTableColumns(self)
        return self._columns