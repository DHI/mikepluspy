from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class msm_HParAutoCaliRDIITableColumns(BaseColumns):
    """Column names for msm_HParAutoCaliRDII (RDI autocalibration)."""
    MUID = "MUID"
    """MUID"""
    ParRdiiID = "ParRdiiID"
    """ParRdiiID"""
    Parameter = "Parameter"
    """Parameter"""
    FitNo = "FitNo"
    """Fit"""
    InitialValue = "InitialValue"
    """Initial Value"""
    LowerBound = "LowerBound"
    """Lower Bound"""
    UpperBound = "UpperBound"
    """Upper Bound"""
    UnitCtrlNo = "UnitCtrlNo"
    """Fit"""

class msm_HParAutoCaliRDIITable(BaseTable):
    """Table for msm_HParAutoCaliRDII (RDI autocalibration)."""
    
    @property
    def columns(self) -> msm_HParAutoCaliRDIITableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = msm_HParAutoCaliRDIITableColumns(self)
        return self._columns