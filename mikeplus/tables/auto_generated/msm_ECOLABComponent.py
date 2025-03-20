from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class msm_ECOLABComponentTableColumns(BaseColumns):
    """Column names for msm_ECOLABComponent (MIKE ECO Lab state variables)."""
    MUID = "MUID"
    ECOLABTemplateID = "ECOLABTemplateID"
    StateVariableID = "StateVariableID"
    ID = "ID"
    ADComponentID = "ADComponentID"
    ConversionFactor = "ConversionFactor"
    Transport = "Transport"
    Description = "Description"
    Scope = "Scope"
    MinVal = "MinVal"
    MaxVal = "MaxVal"

class msm_ECOLABComponentTable(BaseTable):
    """Table for msm_ECOLABComponent (MIKE ECO Lab state variables)."""
    
    @property
    def columns(self) -> msm_ECOLABComponentTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = msm_ECOLABComponentTableColumns(self)
        return self._columns