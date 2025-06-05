from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class mrm_DAErrorForecastParaTableColumns(BaseColumns):
    """Column names for mrm_DAErrorForecastPara (Error forecast equations parameter)."""
    MUID = "MUID"
    """ID"""
    EquationsID = "EquationsID"
    """ID"""
    TypeNo = "TypeNo"
    """Type"""
    ConstValue = "ConstValue"
    """Value [()]"""
    MinValue = "MinValue"
    """Min. Value [()]"""
    MaxValue = "MaxValue"
    """Max. Value [()]"""
    FileName = "FileName"
    """File name"""
    ItemID = "ItemID"
    """Item ID"""
    ItemNo = "ItemNo"
    """Item no"""
    RiverID = "RiverID"
    """River ID"""
    Chainage = "Chainage"
    """Chainage [m]"""
    StateVariableItemNo = "StateVariableItemNo"
    """Item"""
    WQcomponentID = "WQcomponentID"
    """WQ component"""

class mrm_DAErrorForecastParaTable(BaseTable):
    """Table for mrm_DAErrorForecastPara (Error forecast equations parameter)."""
    
    @property
    def columns(self) -> mrm_DAErrorForecastParaTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mrm_DAErrorForecastParaTableColumns(self)
        return self._columns