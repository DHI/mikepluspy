from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class mw_AutocaliTargetsTableColumns(BaseColumns):
    """Column names for mw_AutocaliTargets (mw_AutocaliTargets)."""
    MUID = "MUID"
    AutoCaliID = "AutoCaliID"
    Enable = "Enable"
    TargetTypeNo = "TargetTypeNo"
    MeasuredTypeNo = "MeasuredTypeNo"
    ConstValue = "ConstValue"
    PlotID = "PlotID"
    EvalTypeNo = "EvalTypeNo"
    LinkTypeNo = "LinkTypeNo"
    LinkID = "LinkID"
    ObjWeight = "ObjWeight"
    TankID = "TankID"
    JunctionID = "JunctionID"
    LocationTypeNo = "LocationTypeNo"
    LocationID = "LocationID"

class mw_AutocaliTargetsTable(BaseTable):
    """Table for mw_AutocaliTargets (mw_AutocaliTargets)."""
    
    @property
    def columns(self) -> mw_AutocaliTargetsTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mw_AutocaliTargetsTableColumns(self)
        return self._columns