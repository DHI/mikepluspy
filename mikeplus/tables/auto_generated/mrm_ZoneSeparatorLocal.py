from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class mrm_ZoneSeparatorLocalTableColumns(BaseColumns):
    """Column names for mrm_ZoneSeparatorLocal (Zones separators)."""
    MUID = "MUID"
    RiverID = "RiverID"
    Chainage = "Chainage"
    TypeNo = "TypeNo"
    Zone12 = "Zone12"
    Zone23 = "Zone23"
    Zone34 = "Zone34"
    Zone45 = "Zone45"
    Zone56 = "Zone56"
    Zone67 = "Zone67"
    Zone78 = "Zone78"
    Zone89 = "Zone89"
    Zone910 = "Zone910"

class mrm_ZoneSeparatorLocalTable(BaseTable):
    """Table for mrm_ZoneSeparatorLocal (Zones separators)."""
    
    @property
    def columns(self) -> mrm_ZoneSeparatorLocalTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mrm_ZoneSeparatorLocalTableColumns(self)
        return self._columns