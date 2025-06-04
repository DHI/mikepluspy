from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class mrm_DAStandardDeviationTableColumns(BaseColumns):
    """Column names for mrm_DAStandardDeviation (Standard deviation)."""
    MUID = "MUID"
    """ID"""
    DataTypeNo = "DataTypeNo"
    """Data type"""
    TypeNo = "TypeNo"
    """Type"""
    Value = "Value"
    """Value"""
    FileName = "FileName"
    """File name"""
    ItemName = "ItemName"
    """Item ID"""
    ItemNo = "ItemNo"
    """Item no"""
    TimeCstBefore = "TimeCstBefore"
    """Time constant before TOF [h]"""
    TimeCstAfter = "TimeCstAfter"
    """Time constant after TOF [h]"""
    ApplyLowerBox = "ApplyLowerBox"
    """Apply lower limit"""
    LowerValue = "LowerValue"
    """Lower value"""
    ApplyUpperBox = "ApplyUpperBox"
    """Apply upper limit"""
    UpperValue = "UpperValue"
    """Upper value"""
    Description = "Description"
    """Description"""

class mrm_DAStandardDeviationTable(BaseTable):
    """Table for mrm_DAStandardDeviation (Standard deviation)."""
    
    @property
    def columns(self) -> mrm_DAStandardDeviationTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mrm_DAStandardDeviationTableColumns(self)
        return self._columns