from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class m2d_InfiltrationLandCoverTableColumns(BaseColumns):
    """Column names for m2d_InfiltrationLandCover (2D infiltration)."""
    MUID = "MUID"
    """Cover ID"""
    CodeValue = "CodeValue"
    """Zone value"""
    Sqn = "Sqn"
    """Sqn"""
    TypeNo = "TypeNo"
    """TypeNo"""
    InfRate = "InfRate"
    """Infiltration rate [mm/h]"""
    InfCurve = "InfCurve"
    """Infiltration curve"""
    LeakRate = "LeakRate"
    """Leakage rate [mm/h]"""
    LevelDepth = "LevelDepth"
    """Infiltration depth"""
    Porosity = "Porosity"
    """Porosity [()]"""
    Percentage = "Percentage"
    """Initial percentage"""

class m2d_InfiltrationLandCoverTable(BaseTable):
    """Table for m2d_InfiltrationLandCover (2D infiltration)."""
    
    @property
    def columns(self) -> m2d_InfiltrationLandCoverTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = m2d_InfiltrationLandCoverTableColumns(self)
        return self._columns