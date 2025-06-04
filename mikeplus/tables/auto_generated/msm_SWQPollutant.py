from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class msm_SWQPollutantTableColumns(BaseColumns):
    """Column names for msm_SWQPollutant (SWQ advanced methods)."""
    MUID = "MUID"
    """ID"""
    TypeNo = "TypeNo"
    """Surface load type"""
    MethodNo = "MethodNo"
    """Method"""
    ComponentID = "ComponentID"
    """Surface load"""
    SedimentAttachNo = "SedimentAttachNo"
    """Attached pollutants"""
    MaxEMC = "MaxEMC"
    """Max. EMC [mg/l]"""
    BuildUpTypeNo = "BuildUpTypeNo"
    """Buildup method"""
    BuildUpRate = "BuildUpRate"
    """Buildup rate [kg/ha/d]"""
    MaxBuildUp = "MaxBuildUp"
    """BuildUp Max. [kg/ha]"""
    DetachRate = "DetachRate"
    """Detachment rate [kg/ha/d]"""
    WashOffExp = "WashOffExp"
    """Exponent"""

class msm_SWQPollutantTable(BaseTable):
    """Table for msm_SWQPollutant (SWQ advanced methods)."""
    
    @property
    def columns(self) -> msm_SWQPollutantTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = msm_SWQPollutantTableColumns(self)
        return self._columns