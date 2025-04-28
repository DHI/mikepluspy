from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class mss_PollutantTableColumns(BaseColumns):
    """Column names for mss_Pollutant (Pollutants)."""
    MUID = "MUID"
    Crain = "Crain"
    Cgw = "Cgw"
    Cii = "Cii"
    Cdwf = "Cdwf"
    Cinit = "Cinit"
    TypeNo = "TypeNo"
    Kdecay = "Kdecay"
    CoFract = "CoFract"
    CoPollut = "CoPollut"
    SnowFlag = "SnowFlag"
    Description = "Description"

class mss_PollutantTable(BaseTable):
    """Table for mss_Pollutant (Pollutants)."""
    
    @property
    def columns(self) -> mss_PollutantTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mss_PollutantTableColumns(self)
        return self._columns