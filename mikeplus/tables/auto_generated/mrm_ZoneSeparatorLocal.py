from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class mrm_ZoneSeparatorLocalTableColumns(BaseColumns):
    """Column names for mrm_ZoneSeparatorLocal (Zones separators)."""
    MUID = "MUID"
    """ID"""
    RiverID = "RiverID"
    """River ID"""
    Chainage = "Chainage"
    """Chainage [m]"""
    TypeNo = "TypeNo"
    """Zones separators defined as"""
    Zone12 = "Zone12"
    """Zone 1-2"""
    Zone23 = "Zone23"
    """Zone 2-3"""
    Zone34 = "Zone34"
    """Zone 3-4"""
    Zone45 = "Zone45"
    """Zone 4-5"""
    Zone56 = "Zone56"
    """Zone 5-6"""
    Zone67 = "Zone67"
    """Zone 6-7"""
    Zone78 = "Zone78"
    """Zone 7-8"""
    Zone89 = "Zone89"
    """Zone 8-9"""
    Zone910 = "Zone910"
    """Zone 9-10"""

class mrm_ZoneSeparatorLocalTable(BaseTable):
    """Table for mrm_ZoneSeparatorLocal (Zones separators)."""
    
    @property
    def columns(self) -> mrm_ZoneSeparatorLocalTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mrm_ZoneSeparatorLocalTableColumns(self)
        return self._columns