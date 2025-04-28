from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class mw_AutocalibrationTableColumns(BaseColumns):
    """Column names for mw_Autocalibration (Autocalibration)."""
    MUID = "MUID"
    SimulationID = "SimulationID"
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

class mw_AutocalibrationTable(BaseTable):
    """Table for mw_Autocalibration (Autocalibration)."""
    
    @property
    def columns(self) -> mw_AutocalibrationTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mw_AutocalibrationTableColumns(self)
        return self._columns