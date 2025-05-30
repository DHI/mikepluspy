from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class msm_ADDispersionTableColumns(BaseColumns):
    """Column names for msm_ADDispersion (msm_ADDispersion)."""
    MUID = "MUID"
    DispFactor = "DispFactor"
    Exponent = "Exponent"
    MinDispCoef = "MinDispCoef"
    MaxDispCoef = "MaxDispCoef"

class msm_ADDispersionTable(BaseTable):
    """Table for msm_ADDispersion (msm_ADDispersion)."""
    
    @property
    def columns(self) -> msm_ADDispersionTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = msm_ADDispersionTableColumns(self)
        return self._columns