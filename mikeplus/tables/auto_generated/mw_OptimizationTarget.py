from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class mw_OptimizationTargetTableColumns(BaseColumns):
    """Column names for mw_OptimizationTarget (mw_OptimizationTarget)."""
    MUID = "MUID"
    OptimizationID = "OptimizationID"
    TargetID = "TargetID"
    TargetTypeNo = "TargetTypeNo"
    ObjWeight = "ObjWeight"
    TankID = "TankID"
    JunctionID = "JunctionID"
    LinkTypeNo = "LinkTypeNo"
    LinkID = "LinkID"
    SetpointTypeNo = "SetpointTypeNo"
    TargetLevel = "TargetLevel"
    EnergyCostUnitTypeNo = "EnergyCostUnitTypeNo"
    UserDefEnergyCostUnit = "UserDefEnergyCostUnit"
    TargetFlow = "TargetFlow"
    LocationTypeNo = "LocationTypeNo"
    LocationID = "LocationID"
    Enabled = "Enabled"

class mw_OptimizationTargetTable(BaseTable):
    """Table for mw_OptimizationTarget (mw_OptimizationTarget)."""
    
    @property
    def columns(self) -> mw_OptimizationTargetTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mw_OptimizationTargetTableColumns(self)
        return self._columns