from mikeplus.tables.base_geometry_table import BaseGeometryTable
from mikeplus.tables.base_geometry_table import BaseColumns

class mrm_TabulatedTableColumns(BaseColumns):
    """Column names for mrm_Tabulated (Tabulated)."""
    MUID = "MUID"
    """ID"""
    Enabled = "Enabled"
    """Apply"""
    RiverID = "RiverID"
    """River ID"""
    Chainage = "Chainage"
    """Chainage [m]"""
    CalculationTypeNo = "CalculationTypeNo"
    """Calculation mode"""
    QHID = "QHID"
    """Q-h table"""
    DischargeFactor = "DischargeFactor"
    """Discharge factor [()]"""
    Datum = "Datum"
    """Water level datum [m]"""
    DataSource = "DataSource"
    """Data source"""
    Element_S = "Element_S"
    """Status"""
    Description = "Description"
    """Description"""

class mrm_TabulatedTable(BaseGeometryTable):
    """Table for mrm_Tabulated (Tabulated)."""
    
    @property
    def columns(self) -> mrm_TabulatedTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mrm_TabulatedTableColumns(self)
        return self._columns