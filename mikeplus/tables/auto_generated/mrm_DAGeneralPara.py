from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class mrm_DAGeneralParaTableColumns(BaseColumns):
    """Column names for mrm_DAGeneralPara (General parameters)."""
    MUID = "MUID"
    """ID"""
    ModeNo = "ModeNo"
    """Mode"""
    FirstTSNo = "FirstTSNo"
    """First updating time step"""
    EnsembleSize = "EnsembleSize"
    """Ensemble size"""
    ToF = "ToF"
    """Time of forecast"""
    ForecastTypeNo = "ForecastTypeNo"
    """Forecast type"""

class mrm_DAGeneralParaTable(BaseTable):
    """Table for mrm_DAGeneralPara (General parameters)."""
    
    @property
    def columns(self) -> mrm_DAGeneralParaTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mrm_DAGeneralParaTableColumns(self)
        return self._columns