from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class mss_SnowPackTableColumns(BaseColumns):
    """Column names for mss_SnowPack (Snowpacks)."""
    MUID = "MUID"
    Description = "Description"
    Cmin1 = "Cmin1"
    Cmax1 = "Cmax1"
    Tbase1 = "Tbase1"
    Fwf1 = "Fwf1"
    Sd01 = "Sd01"
    Fw01 = "Fw01"
    Snn0 = "Snn0"
    Cmin2 = "Cmin2"
    Cmax2 = "Cmax2"
    Tbase2 = "Tbase2"
    Fwf2 = "Fwf2"
    Sd02 = "Sd02"
    Fw02 = "Fw02"
    SD1002 = "SD1002"
    Cmin3 = "Cmin3"
    Cmax3 = "Cmax3"
    Tbase3 = "Tbase3"
    Fwf3 = "Fwf3"
    Sd03 = "Sd03"
    Fw03 = "Fw03"
    SD1003 = "SD1003"
    Sdplow = "Sdplow"
    Fout = "Fout"
    Fimperv = "Fimperv"
    Fperv = "Fperv"
    Fimelt = "Fimelt"
    Fsubcatch = "Fsubcatch"
    SubCatchID = "SubCatchID"

class mss_SnowPackTable(BaseTable):
    """Table for mss_SnowPack (Snowpacks)."""
    
    @property
    def columns(self) -> mss_SnowPackTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mss_SnowPackTableColumns(self)
        return self._columns