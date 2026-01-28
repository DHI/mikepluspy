from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class msm_ECOLABComponentTableColumns(BaseColumns):
    """Column names for msm_ECOLABComponent (MIKE ECO Lab state variables)."""
    MUID = "MUID"
    """ID"""
    ECOLABTemplateID = "ECOLABTemplateID"
    """MIKE ECO Lab template"""
    StateVariableID = "StateVariableID"
    """State variable"""
    ID = "ID"
    """ID"""
    ADComponentID = "ADComponentID"
    """WQ component"""
    ConversionFactor = "ConversionFactor"
    """Conversion factor"""
    Transport = "Transport"
    """Transport"""
    Description = "Description"
    """Description"""
    Scope = "Scope"
    """Scope"""
    MinVal = "MinVal"
    """MinVal"""
    MaxVal = "MaxVal"
    """MaxVal"""

class msm_ECOLABComponentTable(BaseTable):
    """Table for msm_ECOLABComponent (MIKE ECO Lab state variables)."""
    
    @property
    def columns(self) -> msm_ECOLABComponentTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = msm_ECOLABComponentTableColumns(self)
        return self._columns