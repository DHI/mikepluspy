from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class mss_GroundwaterTableColumns(BaseColumns):
    """Column names for mss_Groundwater (Ground water)."""
    MUID = "MUID"
    SubCatchID = "SubCatchID"
    AquiferID = "AquiferID"
    NodeID = "NodeID"
    SurfElev = "SurfElev"
    A1 = "A1"
    B1 = "B1"
    A2 = "A2"
    B2 = "B2"
    A3 = "A3"
    Description = "Description"
    LateralFlowNo = "LateralFlowNo"
    DeepFlowNo = "DeepFlowNo"
    LateralFlowEquation = "LateralFlowEquation"
    DeepFlowEquation = "DeepFlowEquation"
    Hsw = "Hsw"
    Hcb = "Hcb"
    BottomElev = "BottomElev"
    WTElev = "WTElev"
    UZoneMoisture = "UZoneMoisture"

class mss_GroundwaterTable(BaseTable):
    """Table for mss_Groundwater (Ground water)."""
    
    @property
    def columns(self) -> mss_GroundwaterTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mss_GroundwaterTableColumns(self)
        return self._columns