from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class mss_HydrographDTableColumns(BaseColumns):
    """Column names for mss_HydrographD (MssHydrographDTable)."""
    MUID = "MUID"
    HydrographID = "HydrographID"
    Sqn = "Sqn"
    MonthNo = "MonthNo"
    R1 = "R1"
    R2 = "R2"
    R3 = "R3"
    T1 = "T1"
    T2 = "T2"
    T3 = "T3"
    K1 = "K1"
    K2 = "K2"
    K3 = "K3"
    IA_Max1 = "IA_Max1"
    IA_Rec1 = "IA_Rec1"
    IA_Init1 = "IA_Init1"
    IA_Max2 = "IA_Max2"
    IA_Rec2 = "IA_Rec2"
    IA_Init2 = "IA_Init2"
    IA_Max3 = "IA_Max3"
    IA_Rec3 = "IA_Rec3"
    IA_Init3 = "IA_Init3"

class mss_HydrographDTable(BaseTable):
    """Table for mss_HydrographD (MssHydrographDTable)."""
    
    @property
    def columns(self) -> mss_HydrographDTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mss_HydrographDTableColumns(self)
        return self._columns