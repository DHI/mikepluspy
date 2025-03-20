from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class mss_EvaporationTableColumns(BaseColumns):
    """Column names for mss_Evaporation (Evaporation)."""
    MUID = "MUID"
    TypeNo = "TypeNo"
    ConstValue = "ConstValue"
    Value1 = "Value1"
    Value2 = "Value2"
    Value3 = "Value3"
    Value4 = "Value4"
    Value5 = "Value5"
    Value6 = "Value6"
    Value7 = "Value7"
    Value8 = "Value8"
    Value9 = "Value9"
    Value10 = "Value10"
    Value11 = "Value11"
    Value12 = "Value12"
    TimeSeriesID = "TimeSeriesID"
    Pan1 = "Pan1"
    Pan2 = "Pan2"
    Pan3 = "Pan3"
    Pan4 = "Pan4"
    Pan5 = "Pan5"
    Pan6 = "Pan6"
    Pan7 = "Pan7"
    Pan8 = "Pan8"
    Pan9 = "Pan9"
    Pan10 = "Pan10"
    Pan11 = "Pan11"
    Pan12 = "Pan12"
    SoilRecoveryPatternID = "SoilRecoveryPatternID"
    DryOnlyNo = "DryOnlyNo"

class mss_EvaporationTable(BaseTable):
    """Table for mss_Evaporation (Evaporation)."""
    
    @property
    def columns(self) -> mss_EvaporationTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mss_EvaporationTableColumns(self)
        return self._columns