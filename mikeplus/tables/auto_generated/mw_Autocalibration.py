from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class mw_AutocalibrationTableColumns(BaseColumns):
    """Column names for mw_Autocalibration (Autocalibration)."""
    MUID = "MUID"
    """ID"""
    SimulationID = "SimulationID"
    """Simulation ID"""
    AlgorithmTypeNo = "AlgorithmTypeNo"
    """Optimization algorithm"""
    MaxCallsNo = "MaxCallsNo"
    """Maximum number of calls"""
    DDSseed = "DDSseed"
    """Optimizer seed"""
    DDStargetObj = "DDStargetObj"
    """Target objective"""
    SCEcomplex = "SCEcomplex"
    """Number of complexes"""
    SCEpntInComplex = "SCEpntInComplex"
    """Number of points in each complex"""
    SCEMinNumComplex = "SCEMinNumComplex"
    """Minimum number of complexes"""
    SCEevlStep = "SCEevlStep"
    """Number of evolution steps"""
    SCEpntInSubcomplex = "SCEpntInSubcomplex"
    """Number of points in each sub-complex"""
    SCEseed = "SCEseed"
    """Optimizer seed"""
    SCEtargetObj = "SCEtargetObj"
    """Target objective"""
    SCEmaxLpConvgc = "SCEmaxLpConvgc"
    """Maximum loops of convergence"""
    SCEminRelChg = "SCEminRelChg"
    """Min. relative change in objective function"""
    SCEUseHSFileNo = "SCEUseHSFileNo"
    """Use hotstart file"""
    SCEHSFile = "SCEHSFile"
    """Hotstart file"""
    UseMaxTimePerSimNo = "UseMaxTimePerSimNo"
    """Use max. run time per  simulation"""
    MaxTimePerSim = "MaxTimePerSim"
    """Max. run time per  simulation [sec]"""
    UseMaxInvSolNo = "UseMaxInvSolNo"
    """Use max. no of invalid solutions per simulation"""
    MaxInvSol = "MaxInvSol"
    """Max. no of invalid solutions per simulation"""

class mw_AutocalibrationTable(BaseTable):
    """Table for mw_Autocalibration (Autocalibration)."""
    
    @property
    def columns(self) -> mw_AutocalibrationTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mw_AutocalibrationTableColumns(self)
        return self._columns