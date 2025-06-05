from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class mw_AutocaliTargetsTableColumns(BaseColumns):
    """Column names for mw_AutocaliTargets (mw_AutocaliTargets)."""
    MUID = "MUID"
    """Target ID"""
    AutoCaliID = "AutoCaliID"
    """AutoCaliID"""
    Enable = "Enable"
    """Is active"""
    TargetTypeNo = "TargetTypeNo"
    """Target data type"""
    MeasuredTypeNo = "MeasuredTypeNo"
    """Measured data type"""
    ConstValue = "ConstValue"
    """Constant value"""
    PlotID = "PlotID"
    """Plot ID"""
    EvalTypeNo = "EvalTypeNo"
    """Evaluation type"""
    LinkTypeNo = "LinkTypeNo"
    """Link type"""
    LinkID = "LinkID"
    """Link ID"""
    ObjWeight = "ObjWeight"
    """Objective weight [%]"""
    TankID = "TankID"
    """Tank ID"""
    JunctionID = "JunctionID"
    """Junction ID"""
    LocationTypeNo = "LocationTypeNo"
    """Location type"""
    LocationID = "LocationID"
    """Location ID"""

class mw_AutocaliTargetsTable(BaseTable):
    """Table for mw_AutocaliTargets (mw_AutocaliTargets)."""
    
    @property
    def columns(self) -> mw_AutocaliTargetsTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mw_AutocaliTargetsTableColumns(self)
        return self._columns