from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class m_ModelSettingTableColumns(BaseColumns):
    """Column names for m_ModelSetting (Model type)."""
    MUID = "MUID"
    ModelNo = "ModelNo"
    UBGNo = "UBGNo"
    Enable_Catchment = "Enable_Catchment"
    Enable_CS = "Enable_CS"
    Enable_River = "Enable_River"
    Enable_2DOverland = "Enable_2DOverland"
    Enable_RR = "Enable_RR"
    Enable_HD = "Enable_HD"
    Enable_RTC = "Enable_RTC"
    Enable_LTS = "Enable_LTS"
    Enable_AD = "Enable_AD"
    Enable_ECOLAB = "Enable_ECOLAB"
    Enable_ST = "Enable_ST"
    Enable_MHRiver_Coupling = "Enable_MHRiver_Coupling"
    Enable_M21FM_Coupling = "Enable_M21FM_Coupling"
    Enable_MSHE_Coupling = "Enable_MSHE_Coupling"
    Enable_DA = "Enable_DA"
    Enable_EPA_WQ = "Enable_EPA_WQ"
    Enable_EPA_FireFlow = "Enable_EPA_FireFlow"
    Enable_EPA_PipCri = "Enable_EPA_PipCri"
    Enable_EPA_CostAna = "Enable_EPA_CostAna"
    Enable_EPA_ShuPla = "Enable_EPA_ShuPla"
    Enable_EPA_FluAna = "Enable_EPA_FluAna"
    Enable_EPA_WH = "Enable_EPA_WH"
    Enable_1D_PESE = "Enable_1D_PESE"
    Enable_EPA_OnlAna = "Enable_EPA_OnlAna"
    EPAVersionNo = "EPAVersionNo"
    Enable_EPA_Optim = "Enable_EPA_Optim"
    Enable_EPA_MultSpecAna = "Enable_EPA_MultSpecAna"
    Enable_EPA_AutoCali = "Enable_EPA_AutoCali"
    HeadlossNo = "HeadlossNo"

class m_ModelSettingTable(BaseTable):
    """Table for m_ModelSetting (Model type)."""
    
    @property
    def columns(self) -> m_ModelSettingTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = m_ModelSettingTableColumns(self)
        return self._columns