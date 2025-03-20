from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class mss_LIDControlTableColumns(BaseColumns):
    """Column names for mss_LIDControl (LID properties)."""
    MUID = "MUID"
    LIDType = "LIDType"
    StorHt = "StorHt"
    VegFrac = "VegFrac"
    Rough = "Rough"
    Slope = "Slope"
    Xslope = "Xslope"
    SThick = "SThick"
    Por = "Por"
    FC = "FC"
    WP = "WP"
    Ksat = "Ksat"
    Kcoeff = "Kcoeff"
    Suct = "Suct"
    PThick = "PThick"
    PVratio = "PVratio"
    FracImp = "FracImp"
    Perm = "Perm"
    PVclog = "PVclog"
    PRegInterval = "PRegInterval"
    PRegFraction = "PRegFraction"
    Height = "Height"
    SVratio = "SVratio"
    Filt = "Filt"
    SVclog = "SVclog"
    Coeff = "Coeff"
    Expon = "Expon"
    _Offset = "_Offset"
    Delay = "Delay"
    OpenLev = "OpenLev"
    ClosedLev = "ClosedLev"
    ControlCurveID = "ControlCurveID"
    DMThick = "DMThick"
    DMVFraction = "DMVFraction"
    DMRough = "DMRough"
    RDFlowCap = "RDFlowCap"

class mss_LIDControlTable(BaseTable):
    """Table for mss_LIDControl (LID properties)."""
    
    @property
    def columns(self) -> mss_LIDControlTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mss_LIDControlTableColumns(self)
        return self._columns