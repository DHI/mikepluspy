from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class mw_PipeRelTableColumns(BaseColumns):
    """Column names for mw_PipeRel (Network vulnerability)."""
    MUID = "MUID"
    SimPeriodNo = "SimPeriodNo"
    TimeHrs = "TimeHrs"
    MinPre = "MinPre"
    UseGlobal = "UseGlobal"
    ZoneIDList = "ZoneIDList"
    UserCriteriaNo = "UserCriteriaNo"
    UserCriteriaField = "UserCriteriaField"

class mw_PipeRelTable(BaseTable):
    """Table for mw_PipeRel (Network vulnerability)."""
    
    @property
    def columns(self) -> mw_PipeRelTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mw_PipeRelTableColumns(self)
        return self._columns