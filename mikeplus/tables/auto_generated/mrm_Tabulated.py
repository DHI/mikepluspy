from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class mrm_TabulatedTableColumns(BaseColumns):
    """Column names for mrm_Tabulated (Tabulated)."""
    MUID = "MUID"
    Enabled = "Enabled"
    RiverID = "RiverID"
    Chainage = "Chainage"
    CalculationTypeNo = "CalculationTypeNo"
    QHID = "QHID"
    DischargeFactor = "DischargeFactor"
    Datum = "Datum"
    DataSource = "DataSource"
    Element_S = "Element_S"
    Description = "Description"

class mrm_TabulatedTable(BaseTable):
    """Table for mrm_Tabulated (Tabulated)."""
    
    @property
    def columns(self) -> mrm_TabulatedTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mrm_TabulatedTableColumns(self)
        return self._columns