from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class mss_InletTableColumns(BaseColumns):
    """Column names for mss_Inlet (Inlets)."""
    MUID = "MUID"
    TypeNo = "TypeNo"
    GrateTypeNo = "GrateTypeNo"
    GrateLength = "GrateLength"
    GrateWidth = "GrateWidth"
    GrateOpenFraction = "GrateOpenFraction"
    GrateSplashVelocity = "GrateSplashVelocity"
    CurbLength = "CurbLength"
    CurbHeight = "CurbHeight"
    CurbThroatAngleNo = "CurbThroatAngleNo"
    SDrainLength = "SDrainLength"
    SDrainWidth = "SDrainWidth"
    CurveTypeNo = "CurveTypeNo"
    CurveID = "CurveID"
    Description = "Description"

class mss_InletTable(BaseTable):
    """Table for mss_Inlet (Inlets)."""
    
    @property
    def columns(self) -> mss_InletTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mss_InletTableColumns(self)
        return self._columns