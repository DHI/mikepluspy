from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class mrm_DAErrorForecastEquationsTableColumns(BaseColumns):
    """Column names for mrm_DAErrorForecastEquations (Error forecast equations)."""
    MUID = "MUID"
    Description = "Description"
    Equation = "Equation"
    PeriodFrom = "PeriodFrom"
    PeriodTo = "PeriodTo"

class mrm_DAErrorForecastEquationsTable(BaseTable):
    """Table for mrm_DAErrorForecastEquations (Error forecast equations)."""
    
    @property
    def columns(self) -> mrm_DAErrorForecastEquationsTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mrm_DAErrorForecastEquationsTableColumns(self)
        return self._columns