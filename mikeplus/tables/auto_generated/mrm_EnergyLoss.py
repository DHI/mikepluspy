from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class mrm_EnergyLossTableColumns(BaseColumns):
    """Column names for mrm_EnergyLoss (Energy losses)."""
    MUID = "MUID"
    Enabled = "Enabled"
    RiverID = "RiverID"
    Chainage = "Chainage"
    AbruptNo = "AbruptNo"
    AbruptValue = "AbruptValue"
    GradualNo = "GradualNo"
    GradualValue = "GradualValue"
    Roughness = "Roughness"
    CustomNo = "CustomNo"
    CustomPositive = "CustomPositive"
    CustomNegative = "CustomNegative"
    ContractionNo = "ContractionNo"
    ContractionPositive = "ContractionPositive"
    ContractionNegative = "ContractionNegative"
    ExpansionNo = "ExpansionNo"
    ExpansionPositive = "ExpansionPositive"
    ExpansionNegative = "ExpansionNegative"
    HeadLossCmTypeNo = "HeadLossCmTypeNo"
    DataSource = "DataSource"
    Element_S = "Element_S"
    Description = "Description"

class mrm_EnergyLossTable(BaseTable):
    """Table for mrm_EnergyLoss (Energy losses)."""
    
    @property
    def columns(self) -> mrm_EnergyLossTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mrm_EnergyLossTableColumns(self)
        return self._columns