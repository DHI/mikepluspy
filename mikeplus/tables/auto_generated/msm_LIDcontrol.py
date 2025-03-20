from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class msm_LIDcontrolTableColumns(BaseColumns):
    """Column names for msm_LIDcontrol (LID properties)."""
    MUID = "MUID"
    LIDTypeNo = "LIDTypeNo"
    StorHt = "StorHt"
    VegFrac = "VegFrac"
    FricTypeNo = "FricTypeNo"
    Rough = "Rough"
    Slope = "Slope"
    Xslope = "Xslope"
    SThick = "SThick"
    Por = "Por"
    FC = "FC"
    WP = "WP"
    SFlowCalculationNo = "SFlowCalculationNo"
    LeakageCapacity = "LeakageCapacity"
    InfiltrationCapacity = "InfiltrationCapacity"
    Ksat = "Ksat"
    Kcoeff = "Kcoeff"
    Suct = "Suct"
    PThick = "PThick"
    PVPorosity = "PVPorosity"
    FracImp = "FracImp"
    Perm = "Perm"
    PVclog = "PVclog"
    Height = "Height"
    SVPorosity = "SVPorosity"
    Filt = "Filt"
    SVclog = "SVclog"
    HOffset = "HOffset"
    Delay = "Delay"
    Expon = "Expon"
    DrainCapacityTypeNo = "DrainCapacityTypeNo"
    DrainCapacityArea = "DrainCapacityArea"
    DrainCapacityFlow = "DrainCapacityFlow"
    DMThick = "DMThick"
    DMVPorosity = "DMVPorosity"
    DMFricTypeNo = "DMFricTypeNo"
    DMRough = "DMRough"

class msm_LIDcontrolTable(BaseTable):
    """Table for msm_LIDcontrol (LID properties)."""
    
    @property
    def columns(self) -> msm_LIDcontrolTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = msm_LIDcontrolTableColumns(self)
        return self._columns