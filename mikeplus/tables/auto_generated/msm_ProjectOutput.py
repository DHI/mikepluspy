from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class msm_ProjectOutputTableColumns(BaseColumns):
    """Column names for msm_ProjectOutput (Project outputs)."""
    MUID = "MUID"
    """MUID"""
    SimulationID = "SimulationID"
    """SimulationID"""
    OutputID = "OutputID"
    """ID"""
    ContentsTypeNo = "ContentsTypeNo"
    """Type"""
    FormatNo = "FormatNo"
    """Format"""
    DtSave = "DtSave"
    """Save every"""
    DtSaveUnitNo = "DtSaveUnitNo"
    """DtSaveUnitNo"""
    DefaultSavePeriodNo = "DefaultSavePeriodNo"
    """Default save period"""
    SaveStartDate = "SaveStartDate"
    """Start saving"""
    SaveEndDate = "SaveEndDate"
    """End saving"""

class msm_ProjectOutputTable(BaseTable):
    """Table for msm_ProjectOutput (Project outputs)."""
    
    @property
    def columns(self) -> msm_ProjectOutputTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = msm_ProjectOutputTableColumns(self)
        return self._columns