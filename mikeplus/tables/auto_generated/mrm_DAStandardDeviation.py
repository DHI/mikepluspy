from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class mrm_DAStandardDeviationTableColumns(BaseColumns):
    """Column names for mrm_DAStandardDeviation (Standard deviation)."""
    MUID = "MUID"
    DataTypeNo = "DataTypeNo"
    TypeNo = "TypeNo"
    Value = "Value"
    FileName = "FileName"
    ItemName = "ItemName"
    ItemNo = "ItemNo"
    TimeCstBefore = "TimeCstBefore"
    TimeCstAfter = "TimeCstAfter"
    ApplyLowerBox = "ApplyLowerBox"
    LowerValue = "LowerValue"
    ApplyUpperBox = "ApplyUpperBox"
    UpperValue = "UpperValue"
    Description = "Description"

class mrm_DAStandardDeviationTable(BaseTable):
    """Table for mrm_DAStandardDeviation (Standard deviation)."""
    
    @property
    def columns(self) -> mrm_DAStandardDeviationTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mrm_DAStandardDeviationTableColumns(self)
        return self._columns