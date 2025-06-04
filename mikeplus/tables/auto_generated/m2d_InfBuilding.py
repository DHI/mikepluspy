from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class m2d_InfBuildingTableColumns(BaseColumns):
    """Column names for m2d_InfBuilding (Building)."""
    MUID = "MUID"
    """ZoneID"""
    CodeValue = "CodeValue"
    """Zone value"""
    IncludeNo = "IncludeNo"
    """Include"""
    UniformHeight = "UniformHeight"
    """Uniform height"""
    UniformElevation = "UniformElevation"
    """Uniform elevation"""
    DischargeCoeff = "DischargeCoeff"
    """Discharge coefficient [()]"""

class m2d_InfBuildingTable(BaseTable):
    """Table for m2d_InfBuilding (Building)."""
    
    @property
    def columns(self) -> m2d_InfBuildingTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = m2d_InfBuildingTableColumns(self)
        return self._columns