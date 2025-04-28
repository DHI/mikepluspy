from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class mss_AdjustmentTableColumns(BaseColumns):
    """Column names for mss_Adjustment (Climatology adjustments)."""
    MUID = "MUID"
    Temp01 = "Temp01"
    Temp02 = "Temp02"
    Temp03 = "Temp03"
    Temp04 = "Temp04"
    Temp05 = "Temp05"
    Temp06 = "Temp06"
    Temp07 = "Temp07"
    Temp08 = "Temp08"
    Temp09 = "Temp09"
    Temp10 = "Temp10"
    Temp11 = "Temp11"
    Temp12 = "Temp12"
    Evap01 = "Evap01"
    Evap02 = "Evap02"
    Evap03 = "Evap03"
    Evap04 = "Evap04"
    Evap05 = "Evap05"
    Evap06 = "Evap06"
    Evap07 = "Evap07"
    Evap08 = "Evap08"
    Evap09 = "Evap09"
    Evap10 = "Evap10"
    Evap11 = "Evap11"
    Evap12 = "Evap12"
    Rain01 = "Rain01"
    Rain02 = "Rain02"
    Rain03 = "Rain03"
    Rain04 = "Rain04"
    Rain05 = "Rain05"
    Rain06 = "Rain06"
    Rain07 = "Rain07"
    Rain08 = "Rain08"
    Rain09 = "Rain09"
    Rain10 = "Rain10"
    Rain11 = "Rain11"
    Rain12 = "Rain12"
    Con01 = "Con01"
    Con02 = "Con02"
    Con03 = "Con03"
    Con04 = "Con04"
    Con05 = "Con05"
    Con06 = "Con06"
    Con07 = "Con07"
    Con08 = "Con08"
    Con09 = "Con09"
    Con10 = "Con10"
    Con11 = "Con11"
    Con12 = "Con12"

class mss_AdjustmentTable(BaseTable):
    """Table for mss_Adjustment (Climatology adjustments)."""
    
    @property
    def columns(self) -> mss_AdjustmentTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mss_AdjustmentTableColumns(self)
        return self._columns