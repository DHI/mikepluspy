from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class msm_RTCPIDTableColumns(BaseColumns):
    """Column names for msm_RTCPID (PID parameters)."""
    MUID = "MUID"
    PFactor = "PFactor"
    ITime = "ITime"
    DTime = "DTime"
    Alpha1 = "Alpha1"
    Alpha2 = "Alpha2"
    Alpha3 = "Alpha3"

class msm_RTCPIDTable(BaseTable):
    """Table for msm_RTCPID (PID parameters)."""
    
    @property
    def columns(self) -> msm_RTCPIDTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = msm_RTCPIDTableColumns(self)
        return self._columns