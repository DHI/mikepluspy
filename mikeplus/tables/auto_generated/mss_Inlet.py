from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class mss_InletTableColumns(BaseColumns):
    """Column names for mss_Inlet (Inlets)."""
    MUID = "MUID"
    """ID"""
    TypeNo = "TypeNo"
    """Inlet type"""
    GrateTypeNo = "GrateTypeNo"
    """Grate type"""
    GrateLength = "GrateLength"
    """Grate length [m]"""
    GrateWidth = "GrateWidth"
    """Grate width [m]"""
    GrateOpenFraction = "GrateOpenFraction"
    """Open fraction [()]"""
    GrateSplashVelocity = "GrateSplashVelocity"
    """Splash velocity [m/s]"""
    CurbLength = "CurbLength"
    """Curb opening length [m]"""
    CurbHeight = "CurbHeight"
    """Curb opening height [m]"""
    CurbThroatAngleNo = "CurbThroatAngleNo"
    """Throat angle"""
    SDrainLength = "SDrainLength"
    """Slotted drain length [m]"""
    SDrainWidth = "SDrainWidth"
    """Slotted drain width [m]"""
    CurveTypeNo = "CurveTypeNo"
    """Curve type"""
    CurveID = "CurveID"
    """Curve ID"""
    Description = "Description"
    """Description"""

class mss_InletTable(BaseTable):
    """Table for mss_Inlet (Inlets)."""
    
    @property
    def columns(self) -> mss_InletTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mss_InletTableColumns(self)
        return self._columns