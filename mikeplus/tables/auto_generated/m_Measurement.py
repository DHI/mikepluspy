from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class m_MeasurementTableColumns(BaseColumns):
    """Column names for m_Measurement (Plots and statistics)."""
    MUID = "MUID"
    """ID"""
    MeasurementStationID = "MeasurementStationID"
    """Measurement station ID"""
    TSFileName = "TSFileName"
    """Measurement file"""
    TSItemName = "TSItemName"
    """Measurement item"""
    ResFileName = "ResFileName"
    """Result file"""
    ResItemName = "ResItemName"
    """Result item name"""
    PeriodSetting = "PeriodSetting"
    """Period settings"""

class m_MeasurementTable(BaseTable):
    """Table for m_Measurement (Plots and statistics)."""
    
    @property
    def columns(self) -> m_MeasurementTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = m_MeasurementTableColumns(self)
        return self._columns