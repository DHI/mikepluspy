from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class ms_DPSpecDayTableColumns(BaseColumns):
    """Column names for ms_DPSpecDay (Special days)."""
    MUID = "MUID"
    TypeNo = "TypeNo"
    DPWeekDayNo = "DPWeekDayNo"
    DPDate = "DPDate"

class ms_DPSpecDayTable(BaseTable):
    """Table for ms_DPSpecDay (Special days)."""
    
    @property
    def columns(self) -> ms_DPSpecDayTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = ms_DPSpecDayTableColumns(self)
        return self._columns