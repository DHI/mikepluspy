from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class mw_ZoneDefTableColumns(BaseColumns):
    """Column names for mw_ZoneDef (Zones)."""
    MUID = "MUID"
    DefTypeNo = "DefTypeNo"
    TypeNo = "TypeNo"
    RangeSelection = "RangeSelection"
    Demand = "Demand"
    Population = "Population"
    Pressure = "Pressure"
    Leakage = "Leakage"
    WBFrom = "WBFrom"
    WBTo = "WBTo"
    UseCustomWBDt = "UseCustomWBDt"
    CustomFromWBDt = "CustomFromWBDt"
    CustomToWBDt = "CustomToWBDt"
    Description = "Description"

class mw_ZoneDefTable(BaseTable):
    """Table for mw_ZoneDef (Zones)."""
    
    @property
    def columns(self) -> mw_ZoneDefTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mw_ZoneDefTableColumns(self)
        return self._columns