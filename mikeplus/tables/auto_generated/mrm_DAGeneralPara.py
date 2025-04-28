from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class mrm_DAGeneralParaTableColumns(BaseColumns):
    """Column names for mrm_DAGeneralPara (General parameters)."""
    MUID = "MUID"
    ModeNo = "ModeNo"
    FirstTSNo = "FirstTSNo"
    EnsembleSize = "EnsembleSize"
    ToF = "ToF"
    ForecastTypeNo = "ForecastTypeNo"

class mrm_DAGeneralParaTable(BaseTable):
    """Table for mrm_DAGeneralPara (General parameters)."""
    
    @property
    def columns(self) -> mrm_DAGeneralParaTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mrm_DAGeneralParaTableColumns(self)
        return self._columns