from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class mss_TemperatureTableColumns(BaseColumns):
    """Column names for mss_Temperature (Climatology)."""
    MUID = "MUID"
    TypeNo = "TypeNo"
    TimeSeriesID = "TimeSeriesID"
    FileName = "FileName"
    StartNo = "StartNo"
    StartDate = "StartDate"
    WindSpeedTypeNo = "WindSpeedTypeNo"
    Value1 = "Value1"
    Value2 = "Value2"
    Value3 = "Value3"
    Value4 = "Value4"
    Value5 = "Value5"
    Value6 = "Value6"
    Value7 = "Value7"
    Value8 = "Value8"
    Value9 = "Value9"
    Value10 = "Value10"
    Value11 = "Value11"
    Value12 = "Value12"
    SnowTemp = "SnowTemp"
    Atiwt = "Atiwt"
    Rnm = "Rnm"
    Elev = "Elev"
    Lat = "Lat"
    Dtlong = "Dtlong"
    ADCNo = "ADCNo"
    AdcPerv0 = "AdcPerv0"
    AdcPerv1 = "AdcPerv1"
    AdcPerv2 = "AdcPerv2"
    AdcPerv3 = "AdcPerv3"
    AdcPerv4 = "AdcPerv4"
    AdcPerv5 = "AdcPerv5"
    AdcPerv6 = "AdcPerv6"
    AdcPerv7 = "AdcPerv7"
    AdcPerv8 = "AdcPerv8"
    AdcPerv9 = "AdcPerv9"
    AdcImPerv0 = "AdcImPerv0"
    AdcImPerv1 = "AdcImPerv1"
    AdcImPerv2 = "AdcImPerv2"
    AdcImPerv3 = "AdcImPerv3"
    AdcImPerv4 = "AdcImPerv4"
    AdcImPerv5 = "AdcImPerv5"
    AdcImPerv6 = "AdcImPerv6"
    AdcImPerv7 = "AdcImPerv7"
    AdcImPerv8 = "AdcImPerv8"
    AdcImPerv9 = "AdcImPerv9"

class mss_TemperatureTable(BaseTable):
    """Table for mss_Temperature (Climatology)."""
    
    @property
    def columns(self) -> mss_TemperatureTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mss_TemperatureTableColumns(self)
        return self._columns