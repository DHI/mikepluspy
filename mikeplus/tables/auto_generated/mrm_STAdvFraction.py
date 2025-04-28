from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class mrm_STAdvFractionTableColumns(BaseColumns):
    """Column names for mrm_STAdvFraction (Sediment fractions)."""
    MUID = "MUID"
    SedTypeNo = "SedTypeNo"
    Porosity = "Porosity"
    RelDensity = "RelDensity"
    Shields = "Shields"
    FallDefNo = "FallDefNo"
    FallVal = "FallVal"
    DefaultSize = "DefaultSize"
    IncludeTypeNo = "IncludeTypeNo"
    BedModelNo = "BedModelNo"
    BedFactor = "BedFactor"
    BedD90d30 = "BedD90d30"
    BedAngle = "BedAngle"
    BedSlopeNo = "BedSlopeNo"
    BedShieldsNo = "BedShieldsNo"
    Beda1 = "Beda1"
    Beda2 = "Beda2"
    Beda3 = "Beda3"
    Beda4 = "Beda4"
    Beda5 = "Beda5"
    Beda6 = "Beda6"
    Beda7 = "Beda7"
    Beda8 = "Beda8"
    SusModelNo = "SusModelNo"
    SusFactor = "SusFactor"
    SusD90d30 = "SusD90d30"
    SusAngle = "SusAngle"
    SusSlopeNo = "SusSlopeNo"
    SusShieldsNo = "SusShieldsNo"
    Susa1 = "Susa1"
    Susa2 = "Susa2"
    Susa3 = "Susa3"
    Susa4 = "Susa4"
    Susa5 = "Susa5"
    Susa6 = "Susa6"
    Susa7 = "Susa7"
    Susa8 = "Susa8"
    CohExp = "CohExp"
    CohErShear = "CohErShear"
    CohErCoef = "CohErCoef"
    CohDepShear = "CohDepShear"

class mrm_STAdvFractionTable(BaseTable):
    """Table for mrm_STAdvFraction (Sediment fractions)."""
    
    @property
    def columns(self) -> mrm_STAdvFractionTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mrm_STAdvFractionTableColumns(self)
        return self._columns