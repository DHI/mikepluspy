from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class mss_LIDusageTableColumns(BaseColumns):
    """Column names for mss_LIDusage (LID deployment)."""
    MUID = "MUID"
    """ID"""
    CatchID = "CatchID"
    """Catchment ID"""
    LidID = "LidID"
    """LID ID"""
    ReplicateNumber = "ReplicateNumber"
    """Number of units"""
    Area = "Area"
    """Area of unit [m^2]"""
    Width = "Width"
    """Overland flow width [m]"""
    InitSat = "InitSat"
    """Initial saturation [%]"""
    FromImp = "FromImp"
    """Impervious area treated [%]"""
    FromPerv = "FromPerv"
    """Pervious area treated [%]"""
    ToPervNo = "ToPervNo"
    """Send outflow to"""
    RptFileNo = "RptFileNo"
    """Result file"""
    RptFileName = "RptFileName"
    """Result file"""
    DrainTo = "DrainTo"
    """Send drain flow to"""

class mss_LIDusageTable(BaseTable):
    """Table for mss_LIDusage (LID deployment)."""
    
    @property
    def columns(self) -> mss_LIDusageTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mss_LIDusageTableColumns(self)
        return self._columns