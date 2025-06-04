from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class msm_CulvertQHFlowTableColumns(BaseColumns):
    """Column names for msm_CulvertQHFlow (Q/h relations)."""
    MUID = "MUID"
    """MUID"""
    CulvertID = "CulvertID"
    """CulvertID"""
    Sqn = "Sqn"
    """Sqn"""
    y = "y"
    """y [m]"""
    Qc = "Qc"
    """Qc [m^3/s]"""
    TypeNo = "TypeNo"
    """Type"""
    Direction = "Direction"
    """Direction"""

class msm_CulvertQHFlowTable(BaseTable):
    """Table for msm_CulvertQHFlow (Q/h relations)."""
    
    @property
    def columns(self) -> msm_CulvertQHFlowTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = msm_CulvertQHFlowTableColumns(self)
        return self._columns