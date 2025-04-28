from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class mrm_DAPerturbationsParaTableColumns(BaseColumns):
    """Column names for mrm_DAPerturbationsPara (Perturbations parameters)."""
    MUID = "MUID"
    ApplyPerturbToNo = "ApplyPerturbToNo"
    BoundaryID = "BoundaryID"
    WQcomponentID = "WQcomponentID"
    ItemNo = "ItemNo"
    StdDevID = "StdDevID"
    CatchmentID = "CatchmentID"
    Description = "Description"

class mrm_DAPerturbationsParaTable(BaseTable):
    """Table for mrm_DAPerturbationsPara (Perturbations parameters)."""
    
    @property
    def columns(self) -> mrm_DAPerturbationsParaTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mrm_DAPerturbationsParaTableColumns(self)
        return self._columns