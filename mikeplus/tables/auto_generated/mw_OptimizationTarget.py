from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class mw_OptimizationTargetTableColumns(BaseColumns):
    """Column names for mw_OptimizationTarget (mw_OptimizationTarget)."""
    MUID = "MUID"
    """MUID"""
    OptimizationID = "OptimizationID"
    """OptimizationID"""
    TargetID = "TargetID"
    """Target ID"""
    TargetTypeNo = "TargetTypeNo"
    """Target type"""
    ObjWeight = "ObjWeight"
    """Objective weight [%]"""
    TankID = "TankID"
    """Tank ID"""
    JunctionID = "JunctionID"
    """Junction ID"""
    LinkTypeNo = "LinkTypeNo"
    """Link type"""
    LinkID = "LinkID"
    """Link ID"""
    SetpointTypeNo = "SetpointTypeNo"
    """Setpoint type"""
    TargetLevel = "TargetLevel"
    """Target level [m]"""
    EnergyCostUnitTypeNo = "EnergyCostUnitTypeNo"
    """Energy cost currency"""
    UserDefEnergyCostUnit = "UserDefEnergyCostUnit"
    """UserDefEnergyCostUnit"""
    TargetFlow = "TargetFlow"
    """Target flow [m^3/s]"""
    LocationTypeNo = "LocationTypeNo"
    """Location type"""
    LocationID = "LocationID"
    """Location ID"""
    Enabled = "Enabled"
    """Is active"""

class mw_OptimizationTargetTable(BaseTable):
    """Table for mw_OptimizationTarget (mw_OptimizationTarget)."""
    
    @property
    def columns(self) -> mw_OptimizationTargetTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mw_OptimizationTargetTableColumns(self)
        return self._columns