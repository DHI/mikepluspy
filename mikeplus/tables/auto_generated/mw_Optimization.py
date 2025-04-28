from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class mw_OptimizationTableColumns(BaseColumns):
    """Column names for mw_Optimization (Optimization)."""
    MUID = "MUID"
    AlgorithmTypeNo = "AlgorithmTypeNo"
    MaxCallsNo = "MaxCallsNo"
    DDSseed = "DDSseed"
    DDStargetObj = "DDStargetObj"
    SCEcomplex = "SCEcomplex"
    SCEpntInComplex = "SCEpntInComplex"
    SCEMinNumComplex = "SCEMinNumComplex"
    SCEevlStep = "SCEevlStep"
    SCEpntInSubcomplex = "SCEpntInSubcomplex"
    SCEseed = "SCEseed"
    SCEtargetObj = "SCEtargetObj"
    SCEmaxLpConvgc = "SCEmaxLpConvgc"
    SCEminRelChg = "SCEminRelChg"
    SCEUseHSFileNo = "SCEUseHSFileNo"
    SCEHSFile = "SCEHSFile"
    UseMaxTimePerSimNo = "UseMaxTimePerSimNo"
    MaxTimePerSim = "MaxTimePerSim"
    UseMaxInvSolNo = "UseMaxInvSolNo"
    MaxInvSol = "MaxInvSol"

class mw_OptimizationTable(BaseTable):
    """Table for mw_Optimization (Optimization)."""
    
    @property
    def columns(self) -> mw_OptimizationTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mw_OptimizationTableColumns(self)
        return self._columns