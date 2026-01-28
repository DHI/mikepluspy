from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class mw_PipeRelTableColumns(BaseColumns):
    """Column names for mw_PipeRel (Network vulnerability)."""
    MUID = "MUID"
    """ID"""
    SimPeriodNo = "SimPeriodNo"
    """Time level"""
    TimeHrs = "TimeHrs"
    """Selected time level [h]"""
    MinPre = "MinPre"
    """Minimum service pressure [m]"""
    UseGlobal = "UseGlobal"
    """Use whole network"""
    ZoneIDList = "ZoneIDList"
    """Zone list"""
    UserCriteriaNo = "UserCriteriaNo"
    """Use user criteria"""
    UserCriteriaField = "UserCriteriaField"
    """User criteria"""

class mw_PipeRelTable(BaseTable):
    """Table for mw_PipeRel (Network vulnerability)."""
    
    @property
    def columns(self) -> mw_PipeRelTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mw_PipeRelTableColumns(self)
        return self._columns