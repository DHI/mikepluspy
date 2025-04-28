from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class msm_HParAutoCaliRDIITableColumns(BaseColumns):
    """Column names for msm_HParAutoCaliRDII (RDI autocalibration)."""
    MUID = "MUID"
    ParRdiiID = "ParRdiiID"
    Parameter = "Parameter"
    FitNo = "FitNo"
    InitialValue = "InitialValue"
    LowerBound = "LowerBound"
    UpperBound = "UpperBound"
    UnitCtrlNo = "UnitCtrlNo"

class msm_HParAutoCaliRDIITable(BaseTable):
    """Table for msm_HParAutoCaliRDII (RDI autocalibration)."""
    
    @property
    def columns(self) -> msm_HParAutoCaliRDIITableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = msm_HParAutoCaliRDIITableColumns(self)
        return self._columns