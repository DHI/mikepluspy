from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class msm_ADDispersionLocalTableColumns(BaseColumns):
    """Column names for msm_ADDispersionLocal (AD Dispersion)."""
    MUID = "MUID"
    ConnectionTypeNo = "ConnectionTypeNo"
    LinkListFile = "LinkListFile"
    LinkID = "LinkID"
    StartChainage = "StartChainage"
    EndChainage = "EndChainage"
    DispFactor = "DispFactor"
    Exponent = "Exponent"
    MinDispCoef = "MinDispCoef"
    MaxDispCoef = "MaxDispCoef"

class msm_ADDispersionLocalTable(BaseTable):
    """Table for msm_ADDispersionLocal (AD Dispersion)."""
    
    @property
    def columns(self) -> msm_ADDispersionLocalTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = msm_ADDispersionLocalTableColumns(self)
        return self._columns