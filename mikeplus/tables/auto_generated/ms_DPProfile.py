from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class ms_DPProfileTableColumns(BaseColumns):
    """Column names for ms_DPProfile (Cyclic profiles)."""
    MUID = "MUID"
    DataRelationNo = "DataRelationNo"
    InterpolationNo = "InterpolationNo"
    MultipliersScalingNo = "MultipliersScalingNo"

class ms_DPProfileTable(BaseTable):
    """Table for ms_DPProfile (Cyclic profiles)."""
    
    @property
    def columns(self) -> ms_DPProfileTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = ms_DPProfileTableColumns(self)
        return self._columns