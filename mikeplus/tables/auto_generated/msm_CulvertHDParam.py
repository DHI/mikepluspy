from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class msm_CulvertHDParamTableColumns(BaseColumns):
    """Column names for msm_CulvertHDParam (Hydraulic parameters)."""
    MUID = "MUID"
    """MUID"""
    CulvertID = "CulvertID"
    """CulvertID"""
    Sqn = "Sqn"
    """Sqn"""
    y = "y"
    """y [m]"""
    Area = "Area"
    """Area [m^2]"""
    Radius = "Radius"
    """Radius [m]"""
    Conveyance = "Conveyance"
    """Conveyance [m^3/s]"""

class msm_CulvertHDParamTable(BaseTable):
    """Table for msm_CulvertHDParam (Hydraulic parameters)."""
    
    @property
    def columns(self) -> msm_CulvertHDParamTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = msm_CulvertHDParamTableColumns(self)
        return self._columns