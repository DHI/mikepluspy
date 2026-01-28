from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class m_ModelSettingTableColumns(BaseColumns):
    """Column names for m_ModelSetting (Model type)."""
    MUID = "MUID"
    """ID"""
    ModelNo = "ModelNo"
    """Model no"""
    UBGNo = "UBGNo"
<<<<<<< HEAD
    """Ubg"""
=======
    Title = "Title"
    Description = "Description"
>>>>>>> bc29183 (Update auto generated tables for MIKE+ 2026)
    Enable_Catchment = "Enable_Catchment"
    """Catchments"""
    Enable_CS = "Enable_CS"
    """Collection system network"""
    Enable_River = "Enable_River"
    """River network"""
    Enable_2DOverland = "Enable_2DOverland"
    """2D Overland"""
    Enable_RR = "Enable_RR"
    """Rainfall-Runoff (RR)"""
    Enable_HD = "Enable_HD"
    """Hydrodynamic (HD)"""
    Enable_RTC = "Enable_RTC"
    """Control rules"""
    Enable_LTS = "Enable_LTS"
    """Long term statistics (LTS)"""
    Enable_AD = "Enable_AD"
    """Transport (AD, SWQ)"""
    Enable_ECOLAB = "Enable_ECOLAB"
    """Water quality (MIKE ECO Lab)"""
    Enable_ST = "Enable_ST"
    """Sediment transport (ST)"""
    Enable_MHRiver_Coupling = "Enable_MHRiver_Coupling"
    """Coupling to MIKE HYDRO River"""
    Enable_M21FM_Coupling = "Enable_M21FM_Coupling"
    """Coupling to MIKE 21 or MIKE 3 FM"""
    Enable_MSHE_Coupling = "Enable_MSHE_Coupling"
    """Coupling to MIKE SHE or FEFLOW"""
    Enable_DA = "Enable_DA"
    """Data assimilation (DA)"""
    Enable_EPA_WQ = "Enable_EPA_WQ"
    """EPAWQ"""
    Enable_EPA_FireFlow = "Enable_EPA_FireFlow"
    """EPA FireFlow"""
    Enable_EPA_PipCri = "Enable_EPA_PipCri"
    """EPA PipCri"""
    Enable_EPA_CostAna = "Enable_EPA_CostAna"
    """EPA CostAna"""
    Enable_EPA_ShuPla = "Enable_EPA_ShuPla"
    """EPA ShuPla"""
    Enable_EPA_FluAna = "Enable_EPA_FluAna"
    """EPA FluAna"""
    Enable_EPA_WH = "Enable_EPA_WH"
    """Water hammer analysis"""
    Enable_1D_PESE = "Enable_1D_PESE"
    """Pump emergency storage estimation"""
    Enable_EPA_OnlAna = "Enable_EPA_OnlAna"
<<<<<<< HEAD
    """Online analysis"""
    EPAVersionNo = "EPAVersionNo"
    """EPANET version"""
=======
>>>>>>> bc29183 (Update auto generated tables for MIKE+ 2026)
    Enable_EPA_Optim = "Enable_EPA_Optim"
    """Optimization"""
    Enable_EPA_MultSpecAna = "Enable_EPA_MultSpecAna"
    """Multi-species analysis"""
    Enable_EPA_AutoCali = "Enable_EPA_AutoCali"
    """Autocalibration"""
    HeadlossNo = "HeadlossNo"
<<<<<<< HEAD
    """Head loss No"""
=======
    WHEngineVersion = "WHEngineVersion"
>>>>>>> bc29183 (Update auto generated tables for MIKE+ 2026)

class m_ModelSettingTable(BaseTable):
    """Table for m_ModelSetting (Model type)."""
    
    @property
    def columns(self) -> m_ModelSettingTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = m_ModelSettingTableColumns(self)
        return self._columns