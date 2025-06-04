from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class msm_RTCPIDTableColumns(BaseColumns):
    """Column names for msm_RTCPID (PID parameters)."""
    MUID = "MUID"
    """ID"""
    PFactor = "PFactor"
    """Proportionality factor K [()]"""
    ITime = "ITime"
    """Integration time Ti [sec]"""
    DTime = "DTime"
    """Derivation time Td [sec]"""
    Alpha1 = "Alpha1"
    """Alpha 1 - weight time n"""
    Alpha2 = "Alpha2"
    """Alpha 2 - weight time n-1"""
    Alpha3 = "Alpha3"
    """Alpha 3 - weight time n-2"""

class msm_RTCPIDTable(BaseTable):
    """Table for msm_RTCPID (PID parameters)."""
    
    @property
    def columns(self) -> msm_RTCPIDTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = msm_RTCPIDTableColumns(self)
        return self._columns