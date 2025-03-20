from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class mw_FireFlowTableColumns(BaseColumns):
    """Column names for mw_FireFlow (Fire flow analysis)."""
    MUID = "MUID"
    UseHydNo = "UseHydNo"
    SimStartTime = "SimStartTime"
    Duration = "Duration"
    SelNodeTypeNo = "SelNodeTypeNo"
    NodeSelectionList = "NodeSelectionList"
    TypeNo = "TypeNo"
    DesignPressure = "DesignPressure"
    DesignFlow = "DesignFlow"
    NodeDemMult = "NodeDemMult"
    UseNodeDemMultNo = "UseNodeDemMultNo"
    UseSimultaneousNo = "UseSimultaneousNo"
    ReportCriPreNo = "ReportCriPreNo"
    ReportCriVelNo = "ReportCriVelNo"
    UseCriNodePreNo = "UseCriNodePreNo"
    UseCriFlowLimitNo = "UseCriFlowLimitNo"
    UseNodeBelResPreNo = "UseNodeBelResPreNo"
    CriNodePre = "CriNodePre"
    CriFlowLimit = "CriFlowLimit"
    SimFirHydNo = "SimFirHydNo"
    FirHydMinorLoss = "FirHydMinorLoss"
    FirHydPipeDiameter = "FirHydPipeDiameter"
    FirHydPipeLength = "FirHydPipeLength"
    FirHydPipeRough = "FirHydPipeRough"
    UseCriNodeRadiusNo = "UseCriNodeRadiusNo"
    CriNodeRadius = "CriNodeRadius"
    SearchZoneTypeNo = "SearchZoneTypeNo"
    HydLayer = "HydLayer"
    HydInputField = "HydInputField"
    HydOutField = "HydOutField"
    SelHydTypeNo = "SelHydTypeNo"
    HydSnapTolerance = "HydSnapTolerance"

class mw_FireFlowTable(BaseTable):
    """Table for mw_FireFlow (Fire flow analysis)."""
    
    @property
    def columns(self) -> mw_FireFlowTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mw_FireFlowTableColumns(self)
        return self._columns