from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class msm_CulvertOrificeFlowCoeffTableColumns(BaseColumns):
    """Column names for msm_CulvertOrificeFlowCoeff (Orifice flow coefficients)."""
    MUID = "MUID"
    CulvertID = "CulvertID"
    Sqn = "Sqn"
    yD = "yD"
    Co = "Co"
    Direction = "Direction"

class msm_CulvertOrificeFlowCoeffTable(BaseTable):
    """Table for msm_CulvertOrificeFlowCoeff (Orifice flow coefficients)."""
    
    @property
    def columns(self) -> msm_CulvertOrificeFlowCoeffTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = msm_CulvertOrificeFlowCoeffTableColumns(self)
        return self._columns