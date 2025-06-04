from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class mrm_BranchRoughnessLocalTableColumns(BaseColumns):
    """Column names for mrm_BranchRoughnessLocal (Bed roughness)."""
    MUID = "MUID"
    """ID"""
    BranchID = "BranchID"
    """River ID"""
    Chainage = "Chainage"
    """Chainage [m]"""
    Roughness = "Roughness"
    """Roughness"""
    Zone1 = "Zone1"
    """Zone 1 (lowest)"""
    Zone2 = "Zone2"
    """Zone 2"""
    Zone3 = "Zone3"
    """Zone 3"""
    Zone4 = "Zone4"
    """Zone 4"""
    Zone5 = "Zone5"
    """Zone 5"""
    Zone6 = "Zone6"
    """Zone 6"""
    Zone7 = "Zone7"
    """Zone 7"""
    Zone8 = "Zone8"
    """Zone 8"""
    Zone9 = "Zone9"
    """Zone 9"""
    Zone10 = "Zone10"
    """Zone 10"""

class mrm_BranchRoughnessLocalTable(BaseTable):
    """Table for mrm_BranchRoughnessLocal (Bed roughness)."""
    
    @property
    def columns(self) -> mrm_BranchRoughnessLocalTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mrm_BranchRoughnessLocalTableColumns(self)
        return self._columns