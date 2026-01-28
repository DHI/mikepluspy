from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class msm_SWQAttachedPollutantTableColumns(BaseColumns):
    """Column names for msm_SWQAttachedPollutant (Attached pollutant)."""
    MUID = "MUID"
    """ID"""
    SWQID = "SWQID"
    """SWQ ID"""
    PollutantID = "PollutantID"
    """Pollutant ID"""
    PSRatio = "PSRatio"
    """PS ratio [%]"""

class msm_SWQAttachedPollutantTable(BaseTable):
    """Table for msm_SWQAttachedPollutant (Attached pollutant)."""
    
    @property
    def columns(self) -> msm_SWQAttachedPollutantTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = msm_SWQAttachedPollutantTableColumns(self)
        return self._columns