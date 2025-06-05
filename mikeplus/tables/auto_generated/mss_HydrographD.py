from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class mss_HydrographDTableColumns(BaseColumns):
    """Column names for mss_HydrographD (MssHydrographDTable)."""
    MUID = "MUID"
    """MUID"""
    HydrographID = "HydrographID"
    """HydrographID"""
    Sqn = "Sqn"
    """Sqn"""
    MonthNo = "MonthNo"
    """MonthNo"""
    R1 = "R1"
    """R1"""
    R2 = "R2"
    """R2"""
    R3 = "R3"
    """R3"""
    T1 = "T1"
    """T1 [h]"""
    T2 = "T2"
    """T2 [h]"""
    T3 = "T3"
    """T3"""
    K1 = "K1"
    """K1"""
    K2 = "K2"
    """K2"""
    K3 = "K3"
    """K3 [h]"""
    IA_Max1 = "IA_Max1"
    """IA_Max1 [mm]"""
    IA_Rec1 = "IA_Rec1"
    """IA_Rec1 [mm/d]"""
    IA_Init1 = "IA_Init1"
    """IA_Init1 [mm]"""
    IA_Max2 = "IA_Max2"
    """IA_Max2 [mm]"""
    IA_Rec2 = "IA_Rec2"
    """IA_Rec2 [mm/d]"""
    IA_Init2 = "IA_Init2"
    """IA_Init2 [mm]"""
    IA_Max3 = "IA_Max3"
    """IA_Max3 [mm]"""
    IA_Rec3 = "IA_Rec3"
    """IA_Rec3 [mm/d]"""
    IA_Init3 = "IA_Init3"
    """IA_Init3 [mm]"""

class mss_HydrographDTable(BaseTable):
    """Table for mss_HydrographD (MssHydrographDTable)."""
    
    @property
    def columns(self) -> mss_HydrographDTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mss_HydrographDTableColumns(self)
        return self._columns