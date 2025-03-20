from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class mss_LIDusageTableColumns(BaseColumns):
    """Column names for mss_LIDusage (LID deployment)."""
    MUID = "MUID"
    CatchID = "CatchID"
    LidID = "LidID"
    ReplicateNumber = "ReplicateNumber"
    Area = "Area"
    Width = "Width"
    InitSat = "InitSat"
    FromImp = "FromImp"
    FromPerv = "FromPerv"
    ToPervNo = "ToPervNo"
    RptFileNo = "RptFileNo"
    RptFileName = "RptFileName"
    DrainTo = "DrainTo"

class mss_LIDusageTable(BaseTable):
    """Table for mss_LIDusage (LID deployment)."""
    
    @property
    def columns(self) -> mss_LIDusageTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mss_LIDusageTableColumns(self)
        return self._columns