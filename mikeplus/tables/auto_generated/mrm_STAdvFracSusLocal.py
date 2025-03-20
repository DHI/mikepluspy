from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class mrm_STAdvFracSusLocalTableColumns(BaseColumns):
    """Column names for mrm_STAdvFracSusLocal (mrm_STAdvFracSusLocal)."""
    MUID = "MUID"
    STFracID = "STFracID"
    LinkID = "LinkID"
    LinkNo = "LinkNo"
    Chainage = "Chainage"
    ErStress = "ErStress"
    ErCoef = "ErCoef"
    DepStress = "DepStress"

class mrm_STAdvFracSusLocalTable(BaseTable):
    """Table for mrm_STAdvFracSusLocal (mrm_STAdvFracSusLocal)."""
    
    @property
    def columns(self) -> mrm_STAdvFracSusLocalTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mrm_STAdvFracSusLocalTableColumns(self)
        return self._columns