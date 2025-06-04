from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class mw_ZoneDefTableColumns(BaseColumns):
    """Column names for mw_ZoneDef (Zones)."""
    MUID = "MUID"
    """ID"""
    DefTypeNo = "DefTypeNo"
    """Definition type"""
    TypeNo = "TypeNo"
    """Zone type"""
    RangeSelection = "RangeSelection"
    """Selection ID"""
    Demand = "Demand"
    """Demand [m^3/s]"""
    Population = "Population"
    """Population [person]"""
    Pressure = "Pressure"
    """Required pressure [m]"""
    Leakage = "Leakage"
    """Leakage estimate [m^3/s]"""
    WBFrom = "WBFrom"
    """From"""
    WBTo = "WBTo"
    """To"""
    UseCustomWBDt = "UseCustomWBDt"
    """Use custom time range"""
    CustomFromWBDt = "CustomFromWBDt"
    """Custom from"""
    CustomToWBDt = "CustomToWBDt"
    """Custom to"""
    Description = "Description"
    """Description"""

class mw_ZoneDefTable(BaseTable):
    """Table for mw_ZoneDef (Zones)."""
    
    @property
    def columns(self) -> mw_ZoneDefTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mw_ZoneDefTableColumns(self)
        return self._columns