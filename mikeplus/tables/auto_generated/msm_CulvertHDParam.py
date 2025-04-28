from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class msm_CulvertHDParamTableColumns(BaseColumns):
    """Column names for msm_CulvertHDParam (Hydraulic parameters)."""
    MUID = "MUID"
    CulvertID = "CulvertID"
    Sqn = "Sqn"
    y = "y"
    Area = "Area"
    Radius = "Radius"
    Conveyance = "Conveyance"

class msm_CulvertHDParamTable(BaseTable):
    """Table for msm_CulvertHDParam (Hydraulic parameters)."""
    
    @property
    def columns(self) -> msm_CulvertHDParamTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = msm_CulvertHDParamTableColumns(self)
        return self._columns