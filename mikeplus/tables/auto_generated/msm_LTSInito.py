from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class msm_LTSInitoTableColumns(BaseColumns):
    """Column names for msm_LTSInito (msm_LTSInito)."""
    MUID = "MUID"
    InitCondNo = "InitCondNo"

class msm_LTSInitoTable(BaseTable):
    """Table for msm_LTSInito (msm_LTSInito)."""
    
    @property
    def columns(self) -> msm_LTSInitoTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = msm_LTSInitoTableColumns(self)
        return self._columns