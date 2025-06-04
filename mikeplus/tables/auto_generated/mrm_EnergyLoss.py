from mikeplus.tables.base_geometry_table import BaseGeometryTable
from mikeplus.tables.base_geometry_table import BaseColumns

class mrm_EnergyLossTableColumns(BaseColumns):
    """Column names for mrm_EnergyLoss (Energy losses)."""
    MUID = "MUID"
    """ID"""
    Enabled = "Enabled"
    """Apply"""
    RiverID = "RiverID"
    """River ID"""
    Chainage = "Chainage"
    """Chainage [m]"""
    AbruptNo = "AbruptNo"
    """Abrupt change in alignment"""
    AbruptValue = "AbruptValue"
    """Abrupt change in alignment [deg]"""
    GradualNo = "GradualNo"
    """Gradual change in alignment"""
    GradualValue = "GradualValue"
    """Gradual change in alignment [deg]"""
    Roughness = "Roughness"
    """Roughness value [()]"""
    CustomNo = "CustomNo"
    """Custom loss"""
    CustomPositive = "CustomPositive"
    """Positive flow [()]"""
    CustomNegative = "CustomNegative"
    """Negative flow [()]"""
    ContractionNo = "ContractionNo"
    """Contraction loss"""
    ContractionPositive = "ContractionPositive"
    """Positive flow [()]"""
    ContractionNegative = "ContractionNegative"
    """Negative flow [()]"""
    ExpansionNo = "ExpansionNo"
    """Expansion loss"""
    ExpansionPositive = "ExpansionPositive"
    """Positive flow [()]"""
    ExpansionNegative = "ExpansionNegative"
    """Negative flow [()]"""
    HeadLossCmTypeNo = "HeadLossCmTypeNo"
    """Computational method"""
    DataSource = "DataSource"
    """Data source"""
    Element_S = "Element_S"
    """Status"""
    Description = "Description"
    """Description"""

class mrm_EnergyLossTable(BaseGeometryTable):
    """Table for mrm_EnergyLoss (Energy losses)."""
    
    @property
    def columns(self) -> mrm_EnergyLossTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mrm_EnergyLossTableColumns(self)
        return self._columns