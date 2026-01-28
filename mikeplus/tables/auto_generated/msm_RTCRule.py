from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class msm_RTCRuleTableColumns(BaseColumns):
    """Column names for msm_RTCRule (Control rules)."""
    MUID = "MUID"
    """ID"""
    RTCMUID = "RTCMUID"
    """RTCMUID"""
    Sqn = "Sqn"
    """Sqn"""
    Condition = "Condition"
    """Condition"""
    ActionID = "ActionID"
    """Action ID"""
    BlockTime = "BlockTime"
    """Block time [min]"""
    Description = "Description"
    """Description"""

class msm_RTCRuleTable(BaseTable):
    """Table for msm_RTCRule (Control rules)."""
    
    @property
    def columns(self) -> msm_RTCRuleTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = msm_RTCRuleTableColumns(self)
        return self._columns