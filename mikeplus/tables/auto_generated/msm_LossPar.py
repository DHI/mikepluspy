from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class msm_LossParTableColumns(BaseColumns):
    """Column names for msm_LossPar (Outlet head loss)."""
    MUID = "MUID"
    """ID"""
    OutletShapeNo = "OutletShapeNo"
    """Method"""
    CoeffNo = "CoeffNo"
    """Coefficient type"""
    Coeff = "Coeff"
    """Loss coefficient"""
    EffAreaNo = "EffAreaNo"
    """Effective node area"""
    LimitNo = "LimitNo"
    """LimitNo"""

class msm_LossParTable(BaseTable):
    """Table for msm_LossPar (Outlet head loss)."""
    
    @property
    def columns(self) -> msm_LossParTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = msm_LossParTableColumns(self)
        return self._columns