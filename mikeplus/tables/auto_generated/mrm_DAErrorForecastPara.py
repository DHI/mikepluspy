from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class mrm_DAErrorForecastParaTableColumns(BaseColumns):
    """Column names for mrm_DAErrorForecastPara (Error forecast equations parameter)."""
    MUID = "MUID"
    EquationsID = "EquationsID"
    TypeNo = "TypeNo"
    ConstValue = "ConstValue"
    MinValue = "MinValue"
    MaxValue = "MaxValue"
    FileName = "FileName"
    ItemID = "ItemID"
    ItemNo = "ItemNo"
    RiverID = "RiverID"
    Chainage = "Chainage"
    StateVariableItemNo = "StateVariableItemNo"
    WQcomponentID = "WQcomponentID"

class mrm_DAErrorForecastParaTable(BaseTable):
    """Table for mrm_DAErrorForecastPara (Error forecast equations parameter)."""
    
    @property
    def columns(self) -> mrm_DAErrorForecastParaTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mrm_DAErrorForecastParaTableColumns(self)
        return self._columns