from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class msm_LTSResultTableColumns(BaseColumns):
    """Column names for msm_LTSResult (LTS Global parameters)."""
    MUID = "MUID"
    """ID"""
    Dth = "Dth"
    """Dth interevent dT [min]"""
    Pc = "Pc"
    """Interevent p"""
    DtQV = "DtQV"
    """DtQV interevent dT [min]"""
    DtQTn = "DtQTn"
    """DtQTn interevent dT [min]"""
    EmissionsNo = "EmissionsNo"
    """Emissions No"""
    EventLimit = "EventLimit"
    """Number of events to save"""
    StatFrequencyNo = "StatFrequencyNo"
    """Discharge and emissions statistics frequency"""
    DWFSaveFrequency = "DWFSaveFrequency"
    """Continuous DWF TS save frequency [min]"""

class msm_LTSResultTable(BaseTable):
    """Table for msm_LTSResult (LTS Global parameters)."""
    
    @property
    def columns(self) -> msm_LTSResultTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = msm_LTSResultTableColumns(self)
        return self._columns