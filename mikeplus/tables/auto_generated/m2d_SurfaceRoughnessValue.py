from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class m2d_SurfaceRoughnessValueTableColumns(BaseColumns):
    """Column names for m2d_SurfaceRoughnessValue (2D surface roughness)."""
    MUID = "MUID"
    """Cover ID"""
    Sqn = "Sqn"
    """Sqn"""
    CodeValue = "CodeValue"
    """Zone value"""
    RoughnessVal = "RoughnessVal"
    """Roughness value"""
    FunctionOf = "FunctionOf"
    """Function of"""
    RoughnessCurveID = "RoughnessCurveID"
    """Roughness curve"""
    DataSourceType = "DataSourceType"
    """DataSourceType"""

class m2d_SurfaceRoughnessValueTable(BaseTable):
    """Table for m2d_SurfaceRoughnessValue (2D surface roughness)."""
    
    @property
    def columns(self) -> m2d_SurfaceRoughnessValueTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = m2d_SurfaceRoughnessValueTableColumns(self)
        return self._columns