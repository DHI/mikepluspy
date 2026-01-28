from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class mss_PollutantTableColumns(BaseColumns):
    """Column names for mss_Pollutant (Pollutants)."""
    MUID = "MUID"
    """ID"""
    Crain = "Crain"
    """Rain"""
    Cgw = "Cgw"
    """Ground water"""
    Cii = "Cii"
    """Infiltration and inflow flows"""
    Cdwf = "Cdwf"
    """Dry water flow"""
    Cinit = "Cinit"
    """Initial"""
    TypeNo = "TypeNo"
    """Unit"""
    Kdecay = "Kdecay"
    """First order decay coefficient [/d]"""
    CoFract = "CoFract"
    """Co-pollutant fraction"""
    CoPollut = "CoPollut"
    """Co-pollutant ID"""
    SnowFlag = "SnowFlag"
    """Build up during snow fall only"""
    Description = "Description"
    """Description"""

class mss_PollutantTable(BaseTable):
    """Table for mss_Pollutant (Pollutants)."""
    
    @property
    def columns(self) -> mss_PollutantTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mss_PollutantTableColumns(self)
        return self._columns