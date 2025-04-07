from mikeplus.tables.base_table_collection import BaseTableCollection
from mikeplus.tables.base_table import BaseTable
from .m_Configuration import m_ConfigurationTable
from .m_Status import m_StatusTable
from .m_DefaultValue import m_DefaultValueTable
from .m_UserDefinedColumn import m_UserDefinedColumnTable
from .m_Media import m_MediaTable
from .m_StatusCode import m_StatusCodeTable
from .m_Selection import m_SelectionTable
from .m_Bookmark import m_BookmarkTable
from .m_Measurement import m_MeasurementTable
from .m_Station import m_StationTable
from .m_StationCon import m_StationConTable
from .m_ModelSetting import m_ModelSettingTable
from .m_GlobalParameter import m_GlobalParameterTable
from .m_CustomUnit import m_CustomUnitTable
from .m_CustomConfig import m_CustomConfigTable
from .m_ChartBookmark import m_ChartBookmarkTable
from .ms_Tab import ms_TabTable
from .ms_TabD import ms_TabDTable
from .ms_2DTab import ms_2DTabTable
from .ms_2DTabD_TVCtrlRule import ms_2DTabD_TVCtrlRuleTable
from .ms_2DTabD_GenericCtrlRule import ms_2DTabD_GenericCtrlRuleTable
from .ms_2DTabD_Bridge_USBPR_Eccentricity import ms_2DTabD_Bridge_USBPR_EccentricityTable
from .ms_2DTabD_Bridge_FHWA_WSPRO_spur_dykeIII import ms_2DTabD_Bridge_FHWA_WSPRO_spur_dykeIIITable
from .ms_2DTabD_Bridge_Hydraulic_Research_arch import ms_2DTabD_Bridge_Hydraulic_Research_archTable
from .ms_2DTabD_Bridge_Biery_and_Delleur_arch import ms_2DTabD_Bridge_Biery_and_Delleur_archTable
from .ms_2DTabD_Bridge_USBPR_velocity_distribution import ms_2DTabD_Bridge_USBPR_velocity_distributionTable
from .ms_2DTabD_Bridge_FHWA_WSPRO_coef_typeII import ms_2DTabD_Bridge_FHWA_WSPRO_coef_typeIITable
from .ms_2DTabD_Bridge_FHWA_WSPRO_coef_typeIII import ms_2DTabD_Bridge_FHWA_WSPRO_coef_typeIIITable
from .ms_2DTabD_Bridge_FHWA_WSPRO_coef_typeIV import ms_2DTabD_Bridge_FHWA_WSPRO_coef_typeIVTable
from .ms_2DTabD_Bridge_FHWA_WSPRO_depth import ms_2DTabD_Bridge_FHWA_WSPRO_depthTable
from .ms_2DTabD_Bridge_FHWA_WSPRO_abutment import ms_2DTabD_Bridge_FHWA_WSPRO_abutmentTable
from .ms_2DTabD_Bridge_FHWA_WSPRO_Piles import ms_2DTabD_Bridge_FHWA_WSPRO_PilesTable
from .ms_2DTabD_Tabulated_QH import ms_2DTabD_Tabulated_QHTable
from .ms_2DTabD_Tabulated_HQ_UP import ms_2DTabD_Tabulated_HQ_UPTable
from .ms_2DTabD_Tabulated_HQ_DOWN import ms_2DTabD_Tabulated_HQ_DOWNTable
from .ms_CRS import ms_CRSTable
from .ms_CRSD import ms_CRSDTable
from .ms_ProcessedCRSD import ms_ProcessedCRSDTable
from .ms_DPProfile import ms_DPProfileTable
from .ms_DPProfileD import ms_DPProfileDTable
from .ms_DPPattern import ms_DPPatternTable
from .ms_DPPatternD import ms_DPPatternDTable
from .ms_DPSpecDay import ms_DPSpecDayTable
from .ms_DPSchedule import ms_DPScheduleTable
from .ms_Material import ms_MaterialTable
from .ms_SimpSetting import ms_SimpSettingTable
from .ms_SimpMapping import ms_SimpMappingTable
from .msm_Node import msm_NodeTable
from .msm_Link import msm_LinkTable
from .mrm_Branch import mrm_BranchTable
from .mrm_UserDefinedChainage import mrm_UserDefinedChainageTable
from .mrm_RiverRoutingMethod import mrm_RiverRoutingMethodTable
from .mrm_BranchRoughnessLocal import mrm_BranchRoughnessLocalTable
from .mrm_ZoneSeparatorLocal import mrm_ZoneSeparatorLocalTable
from .mrm_RoughnessFactor import mrm_RoughnessFactorTable
from .mrm_BranchConn import mrm_BranchConnTable
from .msm_Catchment import msm_CatchmentTable
from .msm_CatchCon import msm_CatchConTable
from .msm_Weir import msm_WeirTable
from .msm_Valve import msm_ValveTable
from .msm_CurbInlet import msm_CurbInletTable
from .msm_Culvert import msm_CulvertTable
from .msm_CulvertGeom import msm_CulvertGeomTable
from .msm_CulvertHDParam import msm_CulvertHDParamTable
from .msm_CulvertQHFlow import msm_CulvertQHFlowTable
from .msm_CulvertOrificeFlowCoeff import msm_CulvertOrificeFlowCoeffTable
from .mrm_Weir import mrm_WeirTable
from .mrm_WeirGeom import mrm_WeirGeomTable
from .mrm_WeirQHRelation import mrm_WeirQHRelationTable
from .mrm_DirectDischarge import mrm_DirectDischargeTable
from .mrm_Gate import mrm_GateTable
from .mrm_Pump import mrm_PumpTable
from .mrm_Bridge import mrm_BridgeTable
from .mrm_BridgeOpening import mrm_BridgeOpeningTable
from .mrm_BridgeCrs import mrm_BridgeCrsTable
from .mrm_Dambreak import mrm_DambreakTable
from .mrm_EnergyLoss import mrm_EnergyLossTable
from .mrm_Tabulated import mrm_TabulatedTable
from .mrm_Storage import mrm_StorageTable
from .msm_Pump import msm_PumpTable
from .msm_Orifice import msm_OrificeTable
from .msm_BBoundary import msm_BBoundaryTable
from .msm_BndGridRainWeights import msm_BndGridRainWeightsTable
from .msm_WQBoundaryProperties import msm_WQBoundaryPropertiesTable
from .msm_LossPar import msm_LossParTable
from .msm_HParA import msm_HParATable
from .msm_HParB import msm_HParBTable
from .msm_HParC import msm_HParCTable
from .msm_HParRDII import msm_HParRDIITable
from .msm_HParAutoCaliRDII import msm_HParAutoCaliRDIITable
from .msm_HParRdiiElevZones import msm_HParRdiiElevZonesTable
from .msm_HParSeasonalVariation import msm_HParSeasonalVariationTable
from .msm_RTC import msm_RTCTable
from .msm_RTCSensor import msm_RTCSensorTable
from .msm_RTCRule import msm_RTCRuleTable
from .msm_RTCAction import msm_RTCActionTable
from .msm_RTCPID import msm_RTCPIDTable
from .msm_LoadPoint import msm_LoadPointTable
from .msm_LoadPointConnection import msm_LoadPointConnectionTable
from .msm_Project import msm_ProjectTable
from .msm_ProjectOutput import msm_ProjectOutputTable
from .msm_RS import msm_RSTable
from .msm_RSS import msm_RSSTable
from .msm_RSSItem import msm_RSSItemTable
from .msm_RSSGeom import msm_RSSGeomTable
from .msm_RSSFormatGeometry import msm_RSSFormatGeometryTable
from .msm_RSSDem import msm_RSSDemTable
from .msm_ADDispersionLocal import msm_ADDispersionLocalTable
from .msm_ADDispersion import msm_ADDispersionTable
from .msm_ADComponentIni import msm_ADComponentIniTable
from .msm_ADComponent import msm_ADComponentTable
from .msm_ADDecay import msm_ADDecayTable
from .msm_ADInitialCondition import msm_ADInitialConditionTable
from .msm_ADInitialConditionDefault import msm_ADInitialConditionDefaultTable
from .msm_ADInitialConditionLocal import msm_ADInitialConditionLocalTable
from .msm_ADInitialConditionLocalValue import msm_ADInitialConditionLocalValueTable
from .msm_ADInitialConditionHotstartFile import msm_ADInitialConditionHotstartFileTable
from .msm_LTSRunM import msm_LTSRunMTable
from .msm_LTSRunS import msm_LTSRunSTable
from .msm_LTSJobListCriteria import msm_LTSJobListCriteriaTable
from .msm_LTSDwfTs import msm_LTSDwfTsTable
from .msm_LTSInit import msm_LTSInitTable
from .msm_LTSInito import msm_LTSInitoTable
from .msm_LTSResult import msm_LTSResultTable
from .msm_LTSResultLocal import msm_LTSResultLocalTable
from .msm_LIDusage import msm_LIDusageTable
from .msm_LIDcontrol import msm_LIDcontrolTable
from .msm_LIDRemoval import msm_LIDRemovalTable
from .msm_ResultSelectionQuantity import msm_ResultSelectionQuantityTable
from .msm_ECOLABCoeff import msm_ECOLABCoeffTable
from .msm_ECOLABCoeffLocal import msm_ECOLABCoeffLocalTable
from .msm_ECOLABForcing import msm_ECOLABForcingTable
from .msm_ECOLABComponent import msm_ECOLABComponentTable
from .msm_ECOLABTemplate import msm_ECOLABTemplateTable
from .msm_ECOLABOutput import msm_ECOLABOutputTable
from .msm_SWQPollutant import msm_SWQPollutantTable
from .msm_SWQGlobalData import msm_SWQGlobalDataTable
from .msm_SWQAttachedPollutant import msm_SWQAttachedPollutantTable
from .msm_HtmlSummary import msm_HtmlSummaryTable
from .msm_OnGrade import msm_OnGradeTable
from .msm_OnGradeD import msm_OnGradeDTable
from .msm_ST import msm_STTable
from .msm_STFraction import msm_STFractionTable
from .mrm_STAdvFraction import mrm_STAdvFractionTable
from .mrm_STAdvFracGrainLocal import mrm_STAdvFracGrainLocalTable
from .mrm_STAdvFracSusLocal import mrm_STAdvFracSusLocalTable
from .msm_STInitDepthLocal import msm_STInitDepthLocalTable
from .msm_STInitDepthFractDefault import msm_STInitDepthFractDefaultTable
from .msm_STInitDepthFractLocal import msm_STInitDepthFractLocalTable
from .msm_STPipesRoughnessLocal import msm_STPipesRoughnessLocalTable
from .msm_STRemovalBasin import msm_STRemovalBasinTable
from .msm_STRemovalWeir import msm_STRemovalWeirTable
from .mrm_STLocalBedParThick import mrm_STLocalBedParThickTable
from .mrm_STLocalBedParMorph import mrm_STLocalBedParMorphTable
from .mrm_STInitConcentratDefault import mrm_STInitConcentratDefaultTable
from .mrm_STInitConcentratLocal import mrm_STInitConcentratLocalTable
from .msm_HDInitialCondition import msm_HDInitialConditionTable
from .msm_HDInitialConditionLocal import msm_HDInitialConditionLocalTable
from .msm_HDInitialConditionHotstartFile import msm_HDInitialConditionHotstartFileTable
from .msm_AlarmLevel import msm_AlarmLevelTable
from .msm_AlarmLevelD import msm_AlarmLevelDTable
from .msm_PumpESE import msm_PumpESETable
from .msm_PumpESED import msm_PumpESEDTable
from .mrm_DAGeneralPara import mrm_DAGeneralParaTable
from .mrm_DAUpdatePara import mrm_DAUpdateParaTable
from .mrm_DAStandardDeviation import mrm_DAStandardDeviationTable
from .mrm_DAErrorForecastEquations import mrm_DAErrorForecastEquationsTable
from .mrm_DAErrorForecastPara import mrm_DAErrorForecastParaTable
from .mrm_DAPerturbationsPara import mrm_DAPerturbationsParaTable
from .mrm_WindScaleFactorLocal import mrm_WindScaleFactorLocalTable
from .mrm_LeakageCoefficients import mrm_LeakageCoefficientsTable
from .msm_HDAddPercent import msm_HDAddPercentTable
from .msm_RRAddPercent import msm_RRAddPercentTable
from .mrm_SHECouplings import mrm_SHECouplingsTable
from .mrm_STNonScrLocalBedLevel import mrm_STNonScrLocalBedLevelTable
from .mrm_STPassiveLink import mrm_STPassiveLinkTable
from .msm_LandUse import msm_LandUseTable
from .msm_CatchLandUse import msm_CatchLandUseTable
from .mw_PPattern import mw_PPatternTable
from .mw_PPatternD import mw_PPatternDTable
from .mw_Curve import mw_CurveTable
from .mw_CurveD import mw_CurveDTable
from .mw_Junction import mw_JunctionTable
from .mw_Tank import mw_TankTable
from .mw_AirChamber import mw_AirChamberTable
from .mw_MDemand import mw_MDemandTable
from .mw_Pipe import mw_PipeTable
from .mw_Pump import mw_PumpTable
from .mw_Valve import mw_ValveTable
from .mw_Control import mw_ControlTable
from .mw_DemAlloc import mw_DemAllocTable
from .mw_DemAllocConn import mw_DemAllocConnTable
from .mw_PumpStation import mw_PumpStationTable
from .mw_PumpStationConn import mw_PumpStationConnTable
from .mw_SpecDay import mw_SpecDayTable
from .mw_ZoneDef import mw_ZoneDefTable
from .mw_ZoneWB import mw_ZoneWBTable
from .mw_DemStat import mw_DemStatTable
from .mw_DemStatConfig import mw_DemStatConfigTable
from .mw_Project import mw_ProjectTable
from .mw_Source import mw_SourceTable
from .mw_TraceNode import mw_TraceNodeTable
from .mw_Turbine import mw_TurbineTable
from .mw_Friction import mw_FrictionTable
from .mw_Loss import mw_LossTable
from .mw_RTC import mw_RTCTable
from .mw_Energy import mw_EnergyTable
from .mw_Rule import mw_RuleTable
from .mw_Reliability import mw_ReliabilityTable
from .mw_ReliabilityLocal import mw_ReliabilityLocalTable
from .mw_FireFlow import mw_FireFlowTable
from .mw_Flushing import mw_FlushingTable
from .mw_FlushingOutlet import mw_FlushingOutletTable
from .mw_ShutdownPlanning import mw_ShutdownPlanningTable
from .mw_ShutdownValve import mw_ShutdownValveTable
from .mw_PipeRel import mw_PipeRelTable
from .mw_WH_Boundary import mw_WH_BoundaryTable
from .mw_WDOSettings import mw_WDOSettingsTable
from .mw_WDOSensors import mw_WDOSensorsTable
from .mw_Optimization import mw_OptimizationTable
from .mw_OptimizationControl import mw_OptimizationControlTable
from .mw_OptimizationTarget import mw_OptimizationTargetTable
from .mw_OptimizationTargetWB import mw_OptimizationTargetWBTable
from .mw_WDOControls import mw_WDOControlsTable
from .mw_WDODemandZones import mw_WDODemandZonesTable
from .mw_WDODemandPredictions import mw_WDODemandPredictionsTable
from .mw_WDOComparisons import mw_WDOComparisonsTable
from .mw_EPAMSX import mw_EPAMSXTable
from .mw_Autocalibration import mw_AutocalibrationTable
from .mw_AutocaliPipesFrict import mw_AutocaliPipesFrictTable
from .mw_AutocaliNodeDemands import mw_AutocaliNodeDemandsTable
from .mw_AutocaliClosedLinks import mw_AutocaliClosedLinksTable
from .mw_AutocaliLeaks import mw_AutocaliLeaksTable
from .mw_AutocaliTargets import mw_AutocaliTargetsTable
from .mwRes_ValveCriticality import mwRes_ValveCriticalityTable
from .mwRes_Sustainability_Node import mwRes_Sustainability_NodeTable
from .mwRes_Sustainability_Link import mwRes_Sustainability_LinkTable
from .m21_pfsSection import m21_pfsSectionTable
from .m21_pfsKeyword import m21_pfsKeywordTable
from .m21_pfsParam import m21_pfsParamTable
from .m2d_GlobalSetting import m2d_GlobalSettingTable
from .m2d_SurfaceRoughnessArea import m2d_SurfaceRoughnessAreaTable
from .m2d_SurfaceRoughnessValue import m2d_SurfaceRoughnessValueTable
from .m2d_EddyViscosityArea import m2d_EddyViscosityAreaTable
from .m2d_Infiltration import m2d_InfiltrationTable
from .m2d_InfiltrationLandCover import m2d_InfiltrationLandCoverTable
from .m2d_InitialConditionArea import m2d_InitialConditionAreaTable
from .m2d_StructureDike import m2d_StructureDikeTable
from .m2d_StructureWeir import m2d_StructureWeirTable
from .m2d_StructureWeirD import m2d_StructureWeirDTable
from .m2d_StructureCulvert import m2d_StructureCulvertTable
from .m2d_StructureCulvertD import m2d_StructureCulvertDTable
from .m2d_Coupling import m2d_CouplingTable
from .m2d_CouplingConn import m2d_CouplingConnTable
from .m2d_CouplingEngineConn import m2d_CouplingEngineConnTable
from .m2d_CouplingEngineFace import m2d_CouplingEngineFaceTable
from .m2d_MeshArc import m2d_MeshArcTable
from .m2d_MeshLocalArea import m2d_MeshLocalAreaTable
from .m2d_GridDefinition import m2d_GridDefinitionTable
from .m2d_GridInactiveArea import m2d_GridInactiveAreaTable
from .m2d_Boundary import m2d_BoundaryTable
from .m2d_BndQHRelation import m2d_BndQHRelationTable
from .m2d_BndDistributedSource import m2d_BndDistributedSourceTable
from .m2d_ADInitalCondition import m2d_ADInitalConditionTable
from .m2d_ADInitalConditionArea import m2d_ADInitalConditionAreaTable
from .m2d_ADInitalConditionD import m2d_ADInitalConditionDTable
from .m2d_ADPrecipitation import m2d_ADPrecipitationTable
from .m2d_ADPrecipitationArea import m2d_ADPrecipitationAreaTable
from .m2d_ADPrecipitationD import m2d_ADPrecipitationDTable
from .m2d_ADDecay import m2d_ADDecayTable
from .m2d_ADInfiltration import m2d_ADInfiltrationTable
from .m2d_ADInfiltrationArea import m2d_ADInfiltrationAreaTable
from .m2d_ADInfiltrationD import m2d_ADInfiltrationDTable
from .m2d_ADEvaporation import m2d_ADEvaporationTable
from .m2d_ADEvaporationArea import m2d_ADEvaporationAreaTable
from .m2d_ADEvaporationD import m2d_ADEvaporationDTable
from .m2d_ADDispersion import m2d_ADDispersionTable
from .m2d_ADDispersionD import m2d_ADDispersionDTable
from .m2d_ADDispersionArea import m2d_ADDispersionAreaTable
from .m2d_WQBoundary import m2d_WQBoundaryTable
from .m2d_InfBuilding import m2d_InfBuildingTable
from .m2d_InfRoad import m2d_InfRoadTable
from .mss_Node import mss_NodeTable
from .mss_Link import mss_LinkTable
from .mss_CatchCon import mss_CatchConTable
from .mss_Orifice import mss_OrificeTable
from .mss_Pump import mss_PumpTable
from .mss_Outlet import mss_OutletTable
from .mss_Weir import mss_WeirTable
from .mss_Tab import mss_TabTable
from .mss_TabD import mss_TabDTable
from .mss_Project import mss_ProjectTable
from .mss_Timeseries import mss_TimeseriesTable
from .mss_TimeseriesD import mss_TimeseriesDTable
from .mss_Inflow import mss_InflowTable
from .mss_InflowD import mss_InflowDTable
from .mss_Pattern import mss_PatternTable
from .mss_Coverage import mss_CoverageTable
from .mss_Evaporation import mss_EvaporationTable
from .mss_Temperature import mss_TemperatureTable
from .mss_Adjustment import mss_AdjustmentTable
from .mss_Transect import mss_TransectTable
from .mss_TransectD import mss_TransectDTable
from .mss_TransectCoord import mss_TransectCoordTable
from .mss_Aquifer import mss_AquiferTable
from .mss_Hydrograph import mss_HydrographTable
from .mss_HydrographD import mss_HydrographDTable
from .mss_RDII import mss_RDIITable
from .mss_SnowPack import mss_SnowPackTable
from .mss_LIDControl import mss_LIDControlTable
from .mss_LIDControlD import mss_LIDControlDTable
from .mss_LIDusage import mss_LIDusageTable
from .mss_DWF import mss_DWFTable
from .mss_DWFD import mss_DWFDTable
from .mss_Raingauge import mss_RaingaugeTable
from .mss_Groundwater import mss_GroundwaterTable
from .mss_Rule import mss_RuleTable
from .mss_Pollutant import mss_PollutantTable
from .mss_Landuse import mss_LanduseTable
from .mss_Washoff import mss_WashoffTable
from .mss_Buildup import mss_BuildupTable
from .mss_Loading import mss_LoadingTable
from .mss_LocalTreatment import mss_LocalTreatmentTable

class TableCollection(BaseTableCollection):
    """Collection of auto-generated table classes for MIKE+ database tables."""
    
    def _init_tables(self) -> dict[str, BaseTable]:
        tables: dict[str, BaseTable] = {}
        tables['m_Configuration'] = m_ConfigurationTable(self._data_table_container.GetTable('m_Configuration'))
        tables['m_Status'] = m_StatusTable(self._data_table_container.GetTable('m_Status'))
        tables['m_DefaultValue'] = m_DefaultValueTable(self._data_table_container.GetTable('m_DefaultValue'))
        tables['m_UserDefinedColumn'] = m_UserDefinedColumnTable(self._data_table_container.GetTable('m_UserDefinedColumn'))
        tables['m_Media'] = m_MediaTable(self._data_table_container.GetTable('m_Media'))
        tables['m_StatusCode'] = m_StatusCodeTable(self._data_table_container.GetTable('m_StatusCode'))
        tables['m_Selection'] = m_SelectionTable(self._data_table_container.GetTable('m_Selection'))
        tables['m_Bookmark'] = m_BookmarkTable(self._data_table_container.GetTable('m_Bookmark'))
        tables['m_Measurement'] = m_MeasurementTable(self._data_table_container.GetTable('m_Measurement'))
        tables['m_Station'] = m_StationTable(self._data_table_container.GetTable('m_Station'))
        tables['m_StationCon'] = m_StationConTable(self._data_table_container.GetTable('m_StationCon'))
        tables['m_ModelSetting'] = m_ModelSettingTable(self._data_table_container.GetTable('m_ModelSetting'))
        tables['m_GlobalParameter'] = m_GlobalParameterTable(self._data_table_container.GetTable('m_GlobalParameter'))
        tables['m_CustomUnit'] = m_CustomUnitTable(self._data_table_container.GetTable('m_CustomUnit'))
        tables['m_CustomConfig'] = m_CustomConfigTable(self._data_table_container.GetTable('m_CustomConfig'))
        tables['m_ChartBookmark'] = m_ChartBookmarkTable(self._data_table_container.GetTable('m_ChartBookmark'))
        tables['ms_Tab'] = ms_TabTable(self._data_table_container.GetTable('ms_Tab'))
        tables['ms_TabD'] = ms_TabDTable(self._data_table_container.GetTable('ms_TabD'))
        tables['ms_2DTab'] = ms_2DTabTable(self._data_table_container.GetTable('ms_2DTab'))
        tables['ms_2DTabD_TVCtrlRule'] = ms_2DTabD_TVCtrlRuleTable(self._data_table_container.GetTable('ms_2DTabD_TVCtrlRule'))
        tables['ms_2DTabD_GenericCtrlRule'] = ms_2DTabD_GenericCtrlRuleTable(self._data_table_container.GetTable('ms_2DTabD_GenericCtrlRule'))
        tables['ms_2DTabD_Bridge_USBPR_Eccentricity'] = ms_2DTabD_Bridge_USBPR_EccentricityTable(self._data_table_container.GetTable('ms_2DTabD_Bridge_USBPR_Eccentricity'))
        tables['ms_2DTabD_Bridge_FHWA_WSPRO_spur_dykeIII'] = ms_2DTabD_Bridge_FHWA_WSPRO_spur_dykeIIITable(self._data_table_container.GetTable('ms_2DTabD_Bridge_FHWA_WSPRO_spur_dykeIII'))
        tables['ms_2DTabD_Bridge_Hydraulic_Research_arch'] = ms_2DTabD_Bridge_Hydraulic_Research_archTable(self._data_table_container.GetTable('ms_2DTabD_Bridge_Hydraulic_Research_arch'))
        tables['ms_2DTabD_Bridge_Biery_and_Delleur_arch'] = ms_2DTabD_Bridge_Biery_and_Delleur_archTable(self._data_table_container.GetTable('ms_2DTabD_Bridge_Biery_and_Delleur_arch'))
        tables['ms_2DTabD_Bridge_USBPR_velocity_distribution'] = ms_2DTabD_Bridge_USBPR_velocity_distributionTable(self._data_table_container.GetTable('ms_2DTabD_Bridge_USBPR_velocity_distribution'))
        tables['ms_2DTabD_Bridge_FHWA_WSPRO_coef_typeII'] = ms_2DTabD_Bridge_FHWA_WSPRO_coef_typeIITable(self._data_table_container.GetTable('ms_2DTabD_Bridge_FHWA_WSPRO_coef_typeII'))
        tables['ms_2DTabD_Bridge_FHWA_WSPRO_coef_typeIII'] = ms_2DTabD_Bridge_FHWA_WSPRO_coef_typeIIITable(self._data_table_container.GetTable('ms_2DTabD_Bridge_FHWA_WSPRO_coef_typeIII'))
        tables['ms_2DTabD_Bridge_FHWA_WSPRO_coef_typeIV'] = ms_2DTabD_Bridge_FHWA_WSPRO_coef_typeIVTable(self._data_table_container.GetTable('ms_2DTabD_Bridge_FHWA_WSPRO_coef_typeIV'))
        tables['ms_2DTabD_Bridge_FHWA_WSPRO_depth'] = ms_2DTabD_Bridge_FHWA_WSPRO_depthTable(self._data_table_container.GetTable('ms_2DTabD_Bridge_FHWA_WSPRO_depth'))
        tables['ms_2DTabD_Bridge_FHWA_WSPRO_abutment'] = ms_2DTabD_Bridge_FHWA_WSPRO_abutmentTable(self._data_table_container.GetTable('ms_2DTabD_Bridge_FHWA_WSPRO_abutment'))
        tables['ms_2DTabD_Bridge_FHWA_WSPRO_Piles'] = ms_2DTabD_Bridge_FHWA_WSPRO_PilesTable(self._data_table_container.GetTable('ms_2DTabD_Bridge_FHWA_WSPRO_Piles'))
        tables['ms_2DTabD_Tabulated_QH'] = ms_2DTabD_Tabulated_QHTable(self._data_table_container.GetTable('ms_2DTabD_Tabulated_QH'))
        tables['ms_2DTabD_Tabulated_HQ_UP'] = ms_2DTabD_Tabulated_HQ_UPTable(self._data_table_container.GetTable('ms_2DTabD_Tabulated_HQ_UP'))
        tables['ms_2DTabD_Tabulated_HQ_DOWN'] = ms_2DTabD_Tabulated_HQ_DOWNTable(self._data_table_container.GetTable('ms_2DTabD_Tabulated_HQ_DOWN'))
        tables['ms_CRS'] = ms_CRSTable(self._data_table_container.GetTable('ms_CRS'))
        tables['ms_CRSD'] = ms_CRSDTable(self._data_table_container.GetTable('ms_CRSD'))
        tables['ms_ProcessedCRSD'] = ms_ProcessedCRSDTable(self._data_table_container.GetTable('ms_ProcessedCRSD'))
        tables['ms_DPProfile'] = ms_DPProfileTable(self._data_table_container.GetTable('ms_DPProfile'))
        tables['ms_DPProfileD'] = ms_DPProfileDTable(self._data_table_container.GetTable('ms_DPProfileD'))
        tables['ms_DPPattern'] = ms_DPPatternTable(self._data_table_container.GetTable('ms_DPPattern'))
        tables['ms_DPPatternD'] = ms_DPPatternDTable(self._data_table_container.GetTable('ms_DPPatternD'))
        tables['ms_DPSpecDay'] = ms_DPSpecDayTable(self._data_table_container.GetTable('ms_DPSpecDay'))
        tables['ms_DPSchedule'] = ms_DPScheduleTable(self._data_table_container.GetTable('ms_DPSchedule'))
        tables['ms_Material'] = ms_MaterialTable(self._data_table_container.GetTable('ms_Material'))
        tables['ms_SimpSetting'] = ms_SimpSettingTable(self._data_table_container.GetTable('ms_SimpSetting'))
        tables['ms_SimpMapping'] = ms_SimpMappingTable(self._data_table_container.GetTable('ms_SimpMapping'))
        tables['msm_Node'] = msm_NodeTable(self._data_table_container.GetTable('msm_Node'))
        tables['msm_Link'] = msm_LinkTable(self._data_table_container.GetTable('msm_Link'))
        tables['mrm_Branch'] = mrm_BranchTable(self._data_table_container.GetTable('mrm_Branch'))
        tables['mrm_UserDefinedChainage'] = mrm_UserDefinedChainageTable(self._data_table_container.GetTable('mrm_UserDefinedChainage'))
        tables['mrm_RiverRoutingMethod'] = mrm_RiverRoutingMethodTable(self._data_table_container.GetTable('mrm_RiverRoutingMethod'))
        tables['mrm_BranchRoughnessLocal'] = mrm_BranchRoughnessLocalTable(self._data_table_container.GetTable('mrm_BranchRoughnessLocal'))
        tables['mrm_ZoneSeparatorLocal'] = mrm_ZoneSeparatorLocalTable(self._data_table_container.GetTable('mrm_ZoneSeparatorLocal'))
        tables['mrm_RoughnessFactor'] = mrm_RoughnessFactorTable(self._data_table_container.GetTable('mrm_RoughnessFactor'))
        tables['mrm_BranchConn'] = mrm_BranchConnTable(self._data_table_container.GetTable('mrm_BranchConn'))
        tables['msm_Catchment'] = msm_CatchmentTable(self._data_table_container.GetTable('msm_Catchment'))
        tables['msm_CatchCon'] = msm_CatchConTable(self._data_table_container.GetTable('msm_CatchCon'))
        tables['msm_Weir'] = msm_WeirTable(self._data_table_container.GetTable('msm_Weir'))
        tables['msm_Valve'] = msm_ValveTable(self._data_table_container.GetTable('msm_Valve'))
        tables['msm_CurbInlet'] = msm_CurbInletTable(self._data_table_container.GetTable('msm_CurbInlet'))
        tables['msm_Culvert'] = msm_CulvertTable(self._data_table_container.GetTable('msm_Culvert'))
        tables['msm_CulvertGeom'] = msm_CulvertGeomTable(self._data_table_container.GetTable('msm_CulvertGeom'))
        tables['msm_CulvertHDParam'] = msm_CulvertHDParamTable(self._data_table_container.GetTable('msm_CulvertHDParam'))
        tables['msm_CulvertQHFlow'] = msm_CulvertQHFlowTable(self._data_table_container.GetTable('msm_CulvertQHFlow'))
        tables['msm_CulvertOrificeFlowCoeff'] = msm_CulvertOrificeFlowCoeffTable(self._data_table_container.GetTable('msm_CulvertOrificeFlowCoeff'))
        tables['mrm_Weir'] = mrm_WeirTable(self._data_table_container.GetTable('mrm_Weir'))
        tables['mrm_WeirGeom'] = mrm_WeirGeomTable(self._data_table_container.GetTable('mrm_WeirGeom'))
        tables['mrm_WeirQHRelation'] = mrm_WeirQHRelationTable(self._data_table_container.GetTable('mrm_WeirQHRelation'))
        tables['mrm_DirectDischarge'] = mrm_DirectDischargeTable(self._data_table_container.GetTable('mrm_DirectDischarge'))
        tables['mrm_Gate'] = mrm_GateTable(self._data_table_container.GetTable('mrm_Gate'))
        tables['mrm_Pump'] = mrm_PumpTable(self._data_table_container.GetTable('mrm_Pump'))
        tables['mrm_Bridge'] = mrm_BridgeTable(self._data_table_container.GetTable('mrm_Bridge'))
        tables['mrm_BridgeOpening'] = mrm_BridgeOpeningTable(self._data_table_container.GetTable('mrm_BridgeOpening'))
        tables['mrm_BridgeCrs'] = mrm_BridgeCrsTable(self._data_table_container.GetTable('mrm_BridgeCrs'))
        tables['mrm_Dambreak'] = mrm_DambreakTable(self._data_table_container.GetTable('mrm_Dambreak'))
        tables['mrm_EnergyLoss'] = mrm_EnergyLossTable(self._data_table_container.GetTable('mrm_EnergyLoss'))
        tables['mrm_Tabulated'] = mrm_TabulatedTable(self._data_table_container.GetTable('mrm_Tabulated'))
        tables['mrm_Storage'] = mrm_StorageTable(self._data_table_container.GetTable('mrm_Storage'))
        tables['msm_Pump'] = msm_PumpTable(self._data_table_container.GetTable('msm_Pump'))
        tables['msm_Orifice'] = msm_OrificeTable(self._data_table_container.GetTable('msm_Orifice'))
        tables['msm_BBoundary'] = msm_BBoundaryTable(self._data_table_container.GetTable('msm_BBoundary'))
        tables['msm_BndGridRainWeights'] = msm_BndGridRainWeightsTable(self._data_table_container.GetTable('msm_BndGridRainWeights'))
        tables['msm_WQBoundaryProperties'] = msm_WQBoundaryPropertiesTable(self._data_table_container.GetTable('msm_WQBoundaryProperties'))
        tables['msm_LossPar'] = msm_LossParTable(self._data_table_container.GetTable('msm_LossPar'))
        tables['msm_HParA'] = msm_HParATable(self._data_table_container.GetTable('msm_HParA'))
        tables['msm_HParB'] = msm_HParBTable(self._data_table_container.GetTable('msm_HParB'))
        tables['msm_HParC'] = msm_HParCTable(self._data_table_container.GetTable('msm_HParC'))
        tables['msm_HParRDII'] = msm_HParRDIITable(self._data_table_container.GetTable('msm_HParRDII'))
        tables['msm_HParAutoCaliRDII'] = msm_HParAutoCaliRDIITable(self._data_table_container.GetTable('msm_HParAutoCaliRDII'))
        tables['msm_HParRdiiElevZones'] = msm_HParRdiiElevZonesTable(self._data_table_container.GetTable('msm_HParRdiiElevZones'))
        tables['msm_HParSeasonalVariation'] = msm_HParSeasonalVariationTable(self._data_table_container.GetTable('msm_HParSeasonalVariation'))
        tables['msm_RTC'] = msm_RTCTable(self._data_table_container.GetTable('msm_RTC'))
        tables['msm_RTCSensor'] = msm_RTCSensorTable(self._data_table_container.GetTable('msm_RTCSensor'))
        tables['msm_RTCRule'] = msm_RTCRuleTable(self._data_table_container.GetTable('msm_RTCRule'))
        tables['msm_RTCAction'] = msm_RTCActionTable(self._data_table_container.GetTable('msm_RTCAction'))
        tables['msm_RTCPID'] = msm_RTCPIDTable(self._data_table_container.GetTable('msm_RTCPID'))
        tables['msm_LoadPoint'] = msm_LoadPointTable(self._data_table_container.GetTable('msm_LoadPoint'))
        tables['msm_LoadPointConnection'] = msm_LoadPointConnectionTable(self._data_table_container.GetTable('msm_LoadPointConnection'))
        tables['msm_Project'] = msm_ProjectTable(self._data_table_container.GetTable('msm_Project'))
        tables['msm_ProjectOutput'] = msm_ProjectOutputTable(self._data_table_container.GetTable('msm_ProjectOutput'))
        tables['msm_RS'] = msm_RSTable(self._data_table_container.GetTable('msm_RS'))
        tables['msm_RSS'] = msm_RSSTable(self._data_table_container.GetTable('msm_RSS'))
        tables['msm_RSSItem'] = msm_RSSItemTable(self._data_table_container.GetTable('msm_RSSItem'))
        tables['msm_RSSGeom'] = msm_RSSGeomTable(self._data_table_container.GetTable('msm_RSSGeom'))
        tables['msm_RSSFormatGeometry'] = msm_RSSFormatGeometryTable(self._data_table_container.GetTable('msm_RSSFormatGeometry'))
        tables['msm_RSSDem'] = msm_RSSDemTable(self._data_table_container.GetTable('msm_RSSDem'))
        tables['msm_ADDispersionLocal'] = msm_ADDispersionLocalTable(self._data_table_container.GetTable('msm_ADDispersionLocal'))
        tables['msm_ADDispersion'] = msm_ADDispersionTable(self._data_table_container.GetTable('msm_ADDispersion'))
        tables['msm_ADComponentIni'] = msm_ADComponentIniTable(self._data_table_container.GetTable('msm_ADComponentIni'))
        tables['msm_ADComponent'] = msm_ADComponentTable(self._data_table_container.GetTable('msm_ADComponent'))
        tables['msm_ADDecay'] = msm_ADDecayTable(self._data_table_container.GetTable('msm_ADDecay'))
        tables['msm_ADInitialCondition'] = msm_ADInitialConditionTable(self._data_table_container.GetTable('msm_ADInitialCondition'))
        tables['msm_ADInitialConditionDefault'] = msm_ADInitialConditionDefaultTable(self._data_table_container.GetTable('msm_ADInitialConditionDefault'))
        tables['msm_ADInitialConditionLocal'] = msm_ADInitialConditionLocalTable(self._data_table_container.GetTable('msm_ADInitialConditionLocal'))
        tables['msm_ADInitialConditionLocalValue'] = msm_ADInitialConditionLocalValueTable(self._data_table_container.GetTable('msm_ADInitialConditionLocalValue'))
        tables['msm_ADInitialConditionHotstartFile'] = msm_ADInitialConditionHotstartFileTable(self._data_table_container.GetTable('msm_ADInitialConditionHotstartFile'))
        tables['msm_LTSRunM'] = msm_LTSRunMTable(self._data_table_container.GetTable('msm_LTSRunM'))
        tables['msm_LTSRunS'] = msm_LTSRunSTable(self._data_table_container.GetTable('msm_LTSRunS'))
        tables['msm_LTSJobListCriteria'] = msm_LTSJobListCriteriaTable(self._data_table_container.GetTable('msm_LTSJobListCriteria'))
        tables['msm_LTSDwfTs'] = msm_LTSDwfTsTable(self._data_table_container.GetTable('msm_LTSDwfTs'))
        tables['msm_LTSInit'] = msm_LTSInitTable(self._data_table_container.GetTable('msm_LTSInit'))
        tables['msm_LTSInito'] = msm_LTSInitoTable(self._data_table_container.GetTable('msm_LTSInito'))
        tables['msm_LTSResult'] = msm_LTSResultTable(self._data_table_container.GetTable('msm_LTSResult'))
        tables['msm_LTSResultLocal'] = msm_LTSResultLocalTable(self._data_table_container.GetTable('msm_LTSResultLocal'))
        tables['msm_LIDusage'] = msm_LIDusageTable(self._data_table_container.GetTable('msm_LIDusage'))
        tables['msm_LIDcontrol'] = msm_LIDcontrolTable(self._data_table_container.GetTable('msm_LIDcontrol'))
        tables['msm_LIDRemoval'] = msm_LIDRemovalTable(self._data_table_container.GetTable('msm_LIDRemoval'))
        tables['msm_ResultSelectionQuantity'] = msm_ResultSelectionQuantityTable(self._data_table_container.GetTable('msm_ResultSelectionQuantity'))
        tables['msm_ECOLABCoeff'] = msm_ECOLABCoeffTable(self._data_table_container.GetTable('msm_ECOLABCoeff'))
        tables['msm_ECOLABCoeffLocal'] = msm_ECOLABCoeffLocalTable(self._data_table_container.GetTable('msm_ECOLABCoeffLocal'))
        tables['msm_ECOLABForcing'] = msm_ECOLABForcingTable(self._data_table_container.GetTable('msm_ECOLABForcing'))
        tables['msm_ECOLABComponent'] = msm_ECOLABComponentTable(self._data_table_container.GetTable('msm_ECOLABComponent'))
        tables['msm_ECOLABTemplate'] = msm_ECOLABTemplateTable(self._data_table_container.GetTable('msm_ECOLABTemplate'))
        tables['msm_ECOLABOutput'] = msm_ECOLABOutputTable(self._data_table_container.GetTable('msm_ECOLABOutput'))
        tables['msm_SWQPollutant'] = msm_SWQPollutantTable(self._data_table_container.GetTable('msm_SWQPollutant'))
        tables['msm_SWQGlobalData'] = msm_SWQGlobalDataTable(self._data_table_container.GetTable('msm_SWQGlobalData'))
        tables['msm_SWQAttachedPollutant'] = msm_SWQAttachedPollutantTable(self._data_table_container.GetTable('msm_SWQAttachedPollutant'))
        tables['msm_HtmlSummary'] = msm_HtmlSummaryTable(self._data_table_container.GetTable('msm_HtmlSummary'))
        tables['msm_OnGrade'] = msm_OnGradeTable(self._data_table_container.GetTable('msm_OnGrade'))
        tables['msm_OnGradeD'] = msm_OnGradeDTable(self._data_table_container.GetTable('msm_OnGradeD'))
        tables['msm_ST'] = msm_STTable(self._data_table_container.GetTable('msm_ST'))
        tables['msm_STFraction'] = msm_STFractionTable(self._data_table_container.GetTable('msm_STFraction'))
        tables['mrm_STAdvFraction'] = mrm_STAdvFractionTable(self._data_table_container.GetTable('mrm_STAdvFraction'))
        tables['mrm_STAdvFracGrainLocal'] = mrm_STAdvFracGrainLocalTable(self._data_table_container.GetTable('mrm_STAdvFracGrainLocal'))
        tables['mrm_STAdvFracSusLocal'] = mrm_STAdvFracSusLocalTable(self._data_table_container.GetTable('mrm_STAdvFracSusLocal'))
        tables['msm_STInitDepthLocal'] = msm_STInitDepthLocalTable(self._data_table_container.GetTable('msm_STInitDepthLocal'))
        tables['msm_STInitDepthFractDefault'] = msm_STInitDepthFractDefaultTable(self._data_table_container.GetTable('msm_STInitDepthFractDefault'))
        tables['msm_STInitDepthFractLocal'] = msm_STInitDepthFractLocalTable(self._data_table_container.GetTable('msm_STInitDepthFractLocal'))
        tables['msm_STPipesRoughnessLocal'] = msm_STPipesRoughnessLocalTable(self._data_table_container.GetTable('msm_STPipesRoughnessLocal'))
        tables['msm_STRemovalBasin'] = msm_STRemovalBasinTable(self._data_table_container.GetTable('msm_STRemovalBasin'))
        tables['msm_STRemovalWeir'] = msm_STRemovalWeirTable(self._data_table_container.GetTable('msm_STRemovalWeir'))
        tables['mrm_STLocalBedParThick'] = mrm_STLocalBedParThickTable(self._data_table_container.GetTable('mrm_STLocalBedParThick'))
        tables['mrm_STLocalBedParMorph'] = mrm_STLocalBedParMorphTable(self._data_table_container.GetTable('mrm_STLocalBedParMorph'))
        tables['mrm_STInitConcentratDefault'] = mrm_STInitConcentratDefaultTable(self._data_table_container.GetTable('mrm_STInitConcentratDefault'))
        tables['mrm_STInitConcentratLocal'] = mrm_STInitConcentratLocalTable(self._data_table_container.GetTable('mrm_STInitConcentratLocal'))
        tables['msm_HDInitialCondition'] = msm_HDInitialConditionTable(self._data_table_container.GetTable('msm_HDInitialCondition'))
        tables['msm_HDInitialConditionLocal'] = msm_HDInitialConditionLocalTable(self._data_table_container.GetTable('msm_HDInitialConditionLocal'))
        tables['msm_HDInitialConditionHotstartFile'] = msm_HDInitialConditionHotstartFileTable(self._data_table_container.GetTable('msm_HDInitialConditionHotstartFile'))
        tables['msm_AlarmLevel'] = msm_AlarmLevelTable(self._data_table_container.GetTable('msm_AlarmLevel'))
        tables['msm_AlarmLevelD'] = msm_AlarmLevelDTable(self._data_table_container.GetTable('msm_AlarmLevelD'))
        tables['msm_PumpESE'] = msm_PumpESETable(self._data_table_container.GetTable('msm_PumpESE'))
        tables['msm_PumpESED'] = msm_PumpESEDTable(self._data_table_container.GetTable('msm_PumpESED'))
        tables['mrm_DAGeneralPara'] = mrm_DAGeneralParaTable(self._data_table_container.GetTable('mrm_DAGeneralPara'))
        tables['mrm_DAUpdatePara'] = mrm_DAUpdateParaTable(self._data_table_container.GetTable('mrm_DAUpdatePara'))
        tables['mrm_DAStandardDeviation'] = mrm_DAStandardDeviationTable(self._data_table_container.GetTable('mrm_DAStandardDeviation'))
        tables['mrm_DAErrorForecastEquations'] = mrm_DAErrorForecastEquationsTable(self._data_table_container.GetTable('mrm_DAErrorForecastEquations'))
        tables['mrm_DAErrorForecastPara'] = mrm_DAErrorForecastParaTable(self._data_table_container.GetTable('mrm_DAErrorForecastPara'))
        tables['mrm_DAPerturbationsPara'] = mrm_DAPerturbationsParaTable(self._data_table_container.GetTable('mrm_DAPerturbationsPara'))
        tables['mrm_WindScaleFactorLocal'] = mrm_WindScaleFactorLocalTable(self._data_table_container.GetTable('mrm_WindScaleFactorLocal'))
        tables['mrm_LeakageCoefficients'] = mrm_LeakageCoefficientsTable(self._data_table_container.GetTable('mrm_LeakageCoefficients'))
        tables['msm_HDAddPercent'] = msm_HDAddPercentTable(self._data_table_container.GetTable('msm_HDAddPercent'))
        tables['msm_RRAddPercent'] = msm_RRAddPercentTable(self._data_table_container.GetTable('msm_RRAddPercent'))
        tables['mrm_SHECouplings'] = mrm_SHECouplingsTable(self._data_table_container.GetTable('mrm_SHECouplings'))
        tables['mrm_STNonScrLocalBedLevel'] = mrm_STNonScrLocalBedLevelTable(self._data_table_container.GetTable('mrm_STNonScrLocalBedLevel'))
        tables['mrm_STPassiveLink'] = mrm_STPassiveLinkTable(self._data_table_container.GetTable('mrm_STPassiveLink'))
        tables['msm_LandUse'] = msm_LandUseTable(self._data_table_container.GetTable('msm_LandUse'))
        tables['msm_CatchLandUse'] = msm_CatchLandUseTable(self._data_table_container.GetTable('msm_CatchLandUse'))
        tables['mw_PPattern'] = mw_PPatternTable(self._data_table_container.GetTable('mw_PPattern'))
        tables['mw_PPatternD'] = mw_PPatternDTable(self._data_table_container.GetTable('mw_PPatternD'))
        tables['mw_Curve'] = mw_CurveTable(self._data_table_container.GetTable('mw_Curve'))
        tables['mw_CurveD'] = mw_CurveDTable(self._data_table_container.GetTable('mw_CurveD'))
        tables['mw_Junction'] = mw_JunctionTable(self._data_table_container.GetTable('mw_Junction'))
        tables['mw_Tank'] = mw_TankTable(self._data_table_container.GetTable('mw_Tank'))
        tables['mw_AirChamber'] = mw_AirChamberTable(self._data_table_container.GetTable('mw_AirChamber'))
        tables['mw_MDemand'] = mw_MDemandTable(self._data_table_container.GetTable('mw_MDemand'))
        tables['mw_Pipe'] = mw_PipeTable(self._data_table_container.GetTable('mw_Pipe'))
        tables['mw_Pump'] = mw_PumpTable(self._data_table_container.GetTable('mw_Pump'))
        tables['mw_Valve'] = mw_ValveTable(self._data_table_container.GetTable('mw_Valve'))
        tables['mw_Control'] = mw_ControlTable(self._data_table_container.GetTable('mw_Control'))
        tables['mw_DemAlloc'] = mw_DemAllocTable(self._data_table_container.GetTable('mw_DemAlloc'))
        tables['mw_DemAllocConn'] = mw_DemAllocConnTable(self._data_table_container.GetTable('mw_DemAllocConn'))
        tables['mw_PumpStation'] = mw_PumpStationTable(self._data_table_container.GetTable('mw_PumpStation'))
        tables['mw_PumpStationConn'] = mw_PumpStationConnTable(self._data_table_container.GetTable('mw_PumpStationConn'))
        tables['mw_SpecDay'] = mw_SpecDayTable(self._data_table_container.GetTable('mw_SpecDay'))
        tables['mw_ZoneDef'] = mw_ZoneDefTable(self._data_table_container.GetTable('mw_ZoneDef'))
        tables['mw_ZoneWB'] = mw_ZoneWBTable(self._data_table_container.GetTable('mw_ZoneWB'))
        tables['mw_DemStat'] = mw_DemStatTable(self._data_table_container.GetTable('mw_DemStat'))
        tables['mw_DemStatConfig'] = mw_DemStatConfigTable(self._data_table_container.GetTable('mw_DemStatConfig'))
        tables['mw_Project'] = mw_ProjectTable(self._data_table_container.GetTable('mw_Project'))
        tables['mw_Source'] = mw_SourceTable(self._data_table_container.GetTable('mw_Source'))
        tables['mw_TraceNode'] = mw_TraceNodeTable(self._data_table_container.GetTable('mw_TraceNode'))
        tables['mw_Turbine'] = mw_TurbineTable(self._data_table_container.GetTable('mw_Turbine'))
        tables['mw_Friction'] = mw_FrictionTable(self._data_table_container.GetTable('mw_Friction'))
        tables['mw_Loss'] = mw_LossTable(self._data_table_container.GetTable('mw_Loss'))
        tables['mw_RTC'] = mw_RTCTable(self._data_table_container.GetTable('mw_RTC'))
        tables['mw_Energy'] = mw_EnergyTable(self._data_table_container.GetTable('mw_Energy'))
        tables['mw_Rule'] = mw_RuleTable(self._data_table_container.GetTable('mw_Rule'))
        tables['mw_Reliability'] = mw_ReliabilityTable(self._data_table_container.GetTable('mw_Reliability'))
        tables['mw_ReliabilityLocal'] = mw_ReliabilityLocalTable(self._data_table_container.GetTable('mw_ReliabilityLocal'))
        tables['mw_FireFlow'] = mw_FireFlowTable(self._data_table_container.GetTable('mw_FireFlow'))
        tables['mw_Flushing'] = mw_FlushingTable(self._data_table_container.GetTable('mw_Flushing'))
        tables['mw_FlushingOutlet'] = mw_FlushingOutletTable(self._data_table_container.GetTable('mw_FlushingOutlet'))
        tables['mw_ShutdownPlanning'] = mw_ShutdownPlanningTable(self._data_table_container.GetTable('mw_ShutdownPlanning'))
        tables['mw_ShutdownValve'] = mw_ShutdownValveTable(self._data_table_container.GetTable('mw_ShutdownValve'))
        tables['mw_PipeRel'] = mw_PipeRelTable(self._data_table_container.GetTable('mw_PipeRel'))
        tables['mw_WH_Boundary'] = mw_WH_BoundaryTable(self._data_table_container.GetTable('mw_WH_Boundary'))
        tables['mw_WDOSettings'] = mw_WDOSettingsTable(self._data_table_container.GetTable('mw_WDOSettings'))
        tables['mw_WDOSensors'] = mw_WDOSensorsTable(self._data_table_container.GetTable('mw_WDOSensors'))
        tables['mw_Optimization'] = mw_OptimizationTable(self._data_table_container.GetTable('mw_Optimization'))
        tables['mw_OptimizationControl'] = mw_OptimizationControlTable(self._data_table_container.GetTable('mw_OptimizationControl'))
        tables['mw_OptimizationTarget'] = mw_OptimizationTargetTable(self._data_table_container.GetTable('mw_OptimizationTarget'))
        tables['mw_OptimizationTargetWB'] = mw_OptimizationTargetWBTable(self._data_table_container.GetTable('mw_OptimizationTargetWB'))
        tables['mw_WDOControls'] = mw_WDOControlsTable(self._data_table_container.GetTable('mw_WDOControls'))
        tables['mw_WDODemandZones'] = mw_WDODemandZonesTable(self._data_table_container.GetTable('mw_WDODemandZones'))
        tables['mw_WDODemandPredictions'] = mw_WDODemandPredictionsTable(self._data_table_container.GetTable('mw_WDODemandPredictions'))
        tables['mw_WDOComparisons'] = mw_WDOComparisonsTable(self._data_table_container.GetTable('mw_WDOComparisons'))
        tables['mw_EPAMSX'] = mw_EPAMSXTable(self._data_table_container.GetTable('mw_EPAMSX'))
        tables['mw_Autocalibration'] = mw_AutocalibrationTable(self._data_table_container.GetTable('mw_Autocalibration'))
        tables['mw_AutocaliPipesFrict'] = mw_AutocaliPipesFrictTable(self._data_table_container.GetTable('mw_AutocaliPipesFrict'))
        tables['mw_AutocaliNodeDemands'] = mw_AutocaliNodeDemandsTable(self._data_table_container.GetTable('mw_AutocaliNodeDemands'))
        tables['mw_AutocaliClosedLinks'] = mw_AutocaliClosedLinksTable(self._data_table_container.GetTable('mw_AutocaliClosedLinks'))
        tables['mw_AutocaliLeaks'] = mw_AutocaliLeaksTable(self._data_table_container.GetTable('mw_AutocaliLeaks'))
        tables['mw_AutocaliTargets'] = mw_AutocaliTargetsTable(self._data_table_container.GetTable('mw_AutocaliTargets'))
        tables['mwRes_ValveCriticality'] = mwRes_ValveCriticalityTable(self._data_table_container.GetTable('mwRes_ValveCriticality'))
        tables['mwRes_Sustainability_Node'] = mwRes_Sustainability_NodeTable(self._data_table_container.GetTable('mwRes_Sustainability_Node'))
        tables['mwRes_Sustainability_Link'] = mwRes_Sustainability_LinkTable(self._data_table_container.GetTable('mwRes_Sustainability_Link'))
        tables['m21_pfsSection'] = m21_pfsSectionTable(self._data_table_container.GetTable('m21_pfsSection'))
        tables['m21_pfsKeyword'] = m21_pfsKeywordTable(self._data_table_container.GetTable('m21_pfsKeyword'))
        tables['m21_pfsParam'] = m21_pfsParamTable(self._data_table_container.GetTable('m21_pfsParam'))
        tables['m2d_GlobalSetting'] = m2d_GlobalSettingTable(self._data_table_container.GetTable('m2d_GlobalSetting'))
        tables['m2d_SurfaceRoughnessArea'] = m2d_SurfaceRoughnessAreaTable(self._data_table_container.GetTable('m2d_SurfaceRoughnessArea'))
        tables['m2d_SurfaceRoughnessValue'] = m2d_SurfaceRoughnessValueTable(self._data_table_container.GetTable('m2d_SurfaceRoughnessValue'))
        tables['m2d_EddyViscosityArea'] = m2d_EddyViscosityAreaTable(self._data_table_container.GetTable('m2d_EddyViscosityArea'))
        tables['m2d_Infiltration'] = m2d_InfiltrationTable(self._data_table_container.GetTable('m2d_Infiltration'))
        tables['m2d_InfiltrationLandCover'] = m2d_InfiltrationLandCoverTable(self._data_table_container.GetTable('m2d_InfiltrationLandCover'))
        tables['m2d_InitialConditionArea'] = m2d_InitialConditionAreaTable(self._data_table_container.GetTable('m2d_InitialConditionArea'))
        tables['m2d_StructureDike'] = m2d_StructureDikeTable(self._data_table_container.GetTable('m2d_StructureDike'))
        tables['m2d_StructureWeir'] = m2d_StructureWeirTable(self._data_table_container.GetTable('m2d_StructureWeir'))
        tables['m2d_StructureWeirD'] = m2d_StructureWeirDTable(self._data_table_container.GetTable('m2d_StructureWeirD'))
        tables['m2d_StructureCulvert'] = m2d_StructureCulvertTable(self._data_table_container.GetTable('m2d_StructureCulvert'))
        tables['m2d_StructureCulvertD'] = m2d_StructureCulvertDTable(self._data_table_container.GetTable('m2d_StructureCulvertD'))
        tables['m2d_Coupling'] = m2d_CouplingTable(self._data_table_container.GetTable('m2d_Coupling'))
        tables['m2d_CouplingConn'] = m2d_CouplingConnTable(self._data_table_container.GetTable('m2d_CouplingConn'))
        tables['m2d_CouplingEngineConn'] = m2d_CouplingEngineConnTable(self._data_table_container.GetTable('m2d_CouplingEngineConn'))
        tables['m2d_CouplingEngineFace'] = m2d_CouplingEngineFaceTable(self._data_table_container.GetTable('m2d_CouplingEngineFace'))
        tables['m2d_MeshArc'] = m2d_MeshArcTable(self._data_table_container.GetTable('m2d_MeshArc'))
        tables['m2d_MeshLocalArea'] = m2d_MeshLocalAreaTable(self._data_table_container.GetTable('m2d_MeshLocalArea'))
        tables['m2d_GridDefinition'] = m2d_GridDefinitionTable(self._data_table_container.GetTable('m2d_GridDefinition'))
        tables['m2d_GridInactiveArea'] = m2d_GridInactiveAreaTable(self._data_table_container.GetTable('m2d_GridInactiveArea'))
        tables['m2d_Boundary'] = m2d_BoundaryTable(self._data_table_container.GetTable('m2d_Boundary'))
        tables['m2d_BndQHRelation'] = m2d_BndQHRelationTable(self._data_table_container.GetTable('m2d_BndQHRelation'))
        tables['m2d_BndDistributedSource'] = m2d_BndDistributedSourceTable(self._data_table_container.GetTable('m2d_BndDistributedSource'))
        tables['m2d_ADInitalCondition'] = m2d_ADInitalConditionTable(self._data_table_container.GetTable('m2d_ADInitalCondition'))
        tables['m2d_ADInitalConditionArea'] = m2d_ADInitalConditionAreaTable(self._data_table_container.GetTable('m2d_ADInitalConditionArea'))
        tables['m2d_ADInitalConditionD'] = m2d_ADInitalConditionDTable(self._data_table_container.GetTable('m2d_ADInitalConditionD'))
        tables['m2d_ADPrecipitation'] = m2d_ADPrecipitationTable(self._data_table_container.GetTable('m2d_ADPrecipitation'))
        tables['m2d_ADPrecipitationArea'] = m2d_ADPrecipitationAreaTable(self._data_table_container.GetTable('m2d_ADPrecipitationArea'))
        tables['m2d_ADPrecipitationD'] = m2d_ADPrecipitationDTable(self._data_table_container.GetTable('m2d_ADPrecipitationD'))
        tables['m2d_ADDecay'] = m2d_ADDecayTable(self._data_table_container.GetTable('m2d_ADDecay'))
        tables['m2d_ADInfiltration'] = m2d_ADInfiltrationTable(self._data_table_container.GetTable('m2d_ADInfiltration'))
        tables['m2d_ADInfiltrationArea'] = m2d_ADInfiltrationAreaTable(self._data_table_container.GetTable('m2d_ADInfiltrationArea'))
        tables['m2d_ADInfiltrationD'] = m2d_ADInfiltrationDTable(self._data_table_container.GetTable('m2d_ADInfiltrationD'))
        tables['m2d_ADEvaporation'] = m2d_ADEvaporationTable(self._data_table_container.GetTable('m2d_ADEvaporation'))
        tables['m2d_ADEvaporationArea'] = m2d_ADEvaporationAreaTable(self._data_table_container.GetTable('m2d_ADEvaporationArea'))
        tables['m2d_ADEvaporationD'] = m2d_ADEvaporationDTable(self._data_table_container.GetTable('m2d_ADEvaporationD'))
        tables['m2d_ADDispersion'] = m2d_ADDispersionTable(self._data_table_container.GetTable('m2d_ADDispersion'))
        tables['m2d_ADDispersionD'] = m2d_ADDispersionDTable(self._data_table_container.GetTable('m2d_ADDispersionD'))
        tables['m2d_ADDispersionArea'] = m2d_ADDispersionAreaTable(self._data_table_container.GetTable('m2d_ADDispersionArea'))
        tables['m2d_WQBoundary'] = m2d_WQBoundaryTable(self._data_table_container.GetTable('m2d_WQBoundary'))
        tables['m2d_InfBuilding'] = m2d_InfBuildingTable(self._data_table_container.GetTable('m2d_InfBuilding'))
        tables['m2d_InfRoad'] = m2d_InfRoadTable(self._data_table_container.GetTable('m2d_InfRoad'))
        tables['mss_Node'] = mss_NodeTable(self._data_table_container.GetTable('mss_Node'))
        tables['mss_Link'] = mss_LinkTable(self._data_table_container.GetTable('mss_Link'))
        tables['mss_CatchCon'] = mss_CatchConTable(self._data_table_container.GetTable('mss_CatchCon'))
        tables['mss_Orifice'] = mss_OrificeTable(self._data_table_container.GetTable('mss_Orifice'))
        tables['mss_Pump'] = mss_PumpTable(self._data_table_container.GetTable('mss_Pump'))
        tables['mss_Outlet'] = mss_OutletTable(self._data_table_container.GetTable('mss_Outlet'))
        tables['mss_Weir'] = mss_WeirTable(self._data_table_container.GetTable('mss_Weir'))
        tables['mss_Tab'] = mss_TabTable(self._data_table_container.GetTable('mss_Tab'))
        tables['mss_TabD'] = mss_TabDTable(self._data_table_container.GetTable('mss_TabD'))
        tables['mss_Project'] = mss_ProjectTable(self._data_table_container.GetTable('mss_Project'))
        tables['mss_Timeseries'] = mss_TimeseriesTable(self._data_table_container.GetTable('mss_Timeseries'))
        tables['mss_TimeseriesD'] = mss_TimeseriesDTable(self._data_table_container.GetTable('mss_TimeseriesD'))
        tables['mss_Inflow'] = mss_InflowTable(self._data_table_container.GetTable('mss_Inflow'))
        tables['mss_InflowD'] = mss_InflowDTable(self._data_table_container.GetTable('mss_InflowD'))
        tables['mss_Pattern'] = mss_PatternTable(self._data_table_container.GetTable('mss_Pattern'))
        tables['mss_Coverage'] = mss_CoverageTable(self._data_table_container.GetTable('mss_Coverage'))
        tables['mss_Evaporation'] = mss_EvaporationTable(self._data_table_container.GetTable('mss_Evaporation'))
        tables['mss_Temperature'] = mss_TemperatureTable(self._data_table_container.GetTable('mss_Temperature'))
        tables['mss_Adjustment'] = mss_AdjustmentTable(self._data_table_container.GetTable('mss_Adjustment'))
        tables['mss_Transect'] = mss_TransectTable(self._data_table_container.GetTable('mss_Transect'))
        tables['mss_TransectD'] = mss_TransectDTable(self._data_table_container.GetTable('mss_TransectD'))
        tables['mss_TransectCoord'] = mss_TransectCoordTable(self._data_table_container.GetTable('mss_TransectCoord'))
        tables['mss_Aquifer'] = mss_AquiferTable(self._data_table_container.GetTable('mss_Aquifer'))
        tables['mss_Hydrograph'] = mss_HydrographTable(self._data_table_container.GetTable('mss_Hydrograph'))
        tables['mss_HydrographD'] = mss_HydrographDTable(self._data_table_container.GetTable('mss_HydrographD'))
        tables['mss_RDII'] = mss_RDIITable(self._data_table_container.GetTable('mss_RDII'))
        tables['mss_SnowPack'] = mss_SnowPackTable(self._data_table_container.GetTable('mss_SnowPack'))
        tables['mss_LIDControl'] = mss_LIDControlTable(self._data_table_container.GetTable('mss_LIDControl'))
        tables['mss_LIDControlD'] = mss_LIDControlDTable(self._data_table_container.GetTable('mss_LIDControlD'))
        tables['mss_LIDusage'] = mss_LIDusageTable(self._data_table_container.GetTable('mss_LIDusage'))
        tables['mss_DWF'] = mss_DWFTable(self._data_table_container.GetTable('mss_DWF'))
        tables['mss_DWFD'] = mss_DWFDTable(self._data_table_container.GetTable('mss_DWFD'))
        tables['mss_Raingauge'] = mss_RaingaugeTable(self._data_table_container.GetTable('mss_Raingauge'))
        tables['mss_Groundwater'] = mss_GroundwaterTable(self._data_table_container.GetTable('mss_Groundwater'))
        tables['mss_Rule'] = mss_RuleTable(self._data_table_container.GetTable('mss_Rule'))
        tables['mss_Pollutant'] = mss_PollutantTable(self._data_table_container.GetTable('mss_Pollutant'))
        tables['mss_Landuse'] = mss_LanduseTable(self._data_table_container.GetTable('mss_Landuse'))
        tables['mss_Washoff'] = mss_WashoffTable(self._data_table_container.GetTable('mss_Washoff'))
        tables['mss_Buildup'] = mss_BuildupTable(self._data_table_container.GetTable('mss_Buildup'))
        tables['mss_Loading'] = mss_LoadingTable(self._data_table_container.GetTable('mss_Loading'))
        tables['mss_LocalTreatment'] = mss_LocalTreatmentTable(self._data_table_container.GetTable('mss_LocalTreatment'))
        return tables
    
    
    @property
    def m_Configuration(self) -> m_ConfigurationTable:
        """Table 'm_Configuration' (MIKE 1D engine configuration)"""
        return self._tables['m_Configuration']
    
    @property
    def m_Status(self) -> m_StatusTable:
        """Table 'm_Status' (m_Status)"""
        return self._tables['m_Status']
    
    @property
    def m_DefaultValue(self) -> m_DefaultValueTable:
        """Table 'm_DefaultValue' (m_DefaultValue)"""
        return self._tables['m_DefaultValue']
    
    @property
    def m_UserDefinedColumn(self) -> m_UserDefinedColumnTable:
        """Table 'm_UserDefinedColumn' (m_UserDefinedColumn)"""
        return self._tables['m_UserDefinedColumn']
    
    @property
    def m_Media(self) -> m_MediaTable:
        """Table 'm_Media' (m_Media)"""
        return self._tables['m_Media']
    
    @property
    def m_StatusCode(self) -> m_StatusCodeTable:
        """Table 'm_StatusCode' (Status code)"""
        return self._tables['m_StatusCode']
    
    @property
    def m_Selection(self) -> m_SelectionTable:
        """Table 'm_Selection' (m_Selection)"""
        return self._tables['m_Selection']
    
    @property
    def m_Bookmark(self) -> m_BookmarkTable:
        """Table 'm_Bookmark' (m_Bookmark)"""
        return self._tables['m_Bookmark']
    
    @property
    def m_Measurement(self) -> m_MeasurementTable:
        """Table 'm_Measurement' (Plots and statistics)"""
        return self._tables['m_Measurement']
    
    @property
    def m_Station(self) -> m_StationTable:
        """Table 'm_Station' (Measurement stations)"""
        return self._tables['m_Station']
    
    @property
    def m_StationCon(self) -> m_StationConTable:
        """Table 'm_StationCon' (Sensor connections)"""
        return self._tables['m_StationCon']
    
    @property
    def m_ModelSetting(self) -> m_ModelSettingTable:
        """Table 'm_ModelSetting' (Model type)"""
        return self._tables['m_ModelSetting']
    
    @property
    def m_GlobalParameter(self) -> m_GlobalParameterTable:
        """Table 'm_GlobalParameter' (m_GlobalParameter)"""
        return self._tables['m_GlobalParameter']
    
    @property
    def m_CustomUnit(self) -> m_CustomUnitTable:
        """Table 'm_CustomUnit' (m_CustomUnit)"""
        return self._tables['m_CustomUnit']
    
    @property
    def m_CustomConfig(self) -> m_CustomConfigTable:
        """Table 'm_CustomConfig' (Custom configuration)"""
        return self._tables['m_CustomConfig']
    
    @property
    def m_ChartBookmark(self) -> m_ChartBookmarkTable:
        """Table 'm_ChartBookmark' (m_ChartBookmark)"""
        return self._tables['m_ChartBookmark']
    
    @property
    def ms_Tab(self) -> ms_TabTable:
        """Table 'ms_Tab' (Curves and relations)"""
        return self._tables['ms_Tab']
    
    @property
    def ms_TabD(self) -> ms_TabDTable:
        """Table 'ms_TabD' (Curve values)"""
        return self._tables['ms_TabD']
    
    @property
    def ms_2DTab(self) -> ms_2DTabTable:
        """Table 'ms_2DTab' (Two-dimensional tables)"""
        return self._tables['ms_2DTab']
    
    @property
    def ms_2DTabD_TVCtrlRule(self) -> ms_2DTabD_TVCtrlRuleTable:
        """Table 'ms_2DTabD_TVCtrlRule' (Time varying control rule)"""
        return self._tables['ms_2DTabD_TVCtrlRule']
    
    @property
    def ms_2DTabD_GenericCtrlRule(self) -> ms_2DTabD_GenericCtrlRuleTable:
        """Table 'ms_2DTabD_GenericCtrlRule' ()"""
        return self._tables['ms_2DTabD_GenericCtrlRule']
    
    @property
    def ms_2DTabD_Bridge_USBPR_Eccentricity(self) -> ms_2DTabD_Bridge_USBPR_EccentricityTable:
        """Table 'ms_2DTabD_Bridge_USBPR_Eccentricity' ()"""
        return self._tables['ms_2DTabD_Bridge_USBPR_Eccentricity']
    
    @property
    def ms_2DTabD_Bridge_FHWA_WSPRO_spur_dykeIII(self) -> ms_2DTabD_Bridge_FHWA_WSPRO_spur_dykeIIITable:
        """Table 'ms_2DTabD_Bridge_FHWA_WSPRO_spur_dykeIII' ()"""
        return self._tables['ms_2DTabD_Bridge_FHWA_WSPRO_spur_dykeIII']
    
    @property
    def ms_2DTabD_Bridge_Hydraulic_Research_arch(self) -> ms_2DTabD_Bridge_Hydraulic_Research_archTable:
        """Table 'ms_2DTabD_Bridge_Hydraulic_Research_arch' ()"""
        return self._tables['ms_2DTabD_Bridge_Hydraulic_Research_arch']
    
    @property
    def ms_2DTabD_Bridge_Biery_and_Delleur_arch(self) -> ms_2DTabD_Bridge_Biery_and_Delleur_archTable:
        """Table 'ms_2DTabD_Bridge_Biery_and_Delleur_arch' ()"""
        return self._tables['ms_2DTabD_Bridge_Biery_and_Delleur_arch']
    
    @property
    def ms_2DTabD_Bridge_USBPR_velocity_distribution(self) -> ms_2DTabD_Bridge_USBPR_velocity_distributionTable:
        """Table 'ms_2DTabD_Bridge_USBPR_velocity_distribution' ()"""
        return self._tables['ms_2DTabD_Bridge_USBPR_velocity_distribution']
    
    @property
    def ms_2DTabD_Bridge_FHWA_WSPRO_coef_typeII(self) -> ms_2DTabD_Bridge_FHWA_WSPRO_coef_typeIITable:
        """Table 'ms_2DTabD_Bridge_FHWA_WSPRO_coef_typeII' ()"""
        return self._tables['ms_2DTabD_Bridge_FHWA_WSPRO_coef_typeII']
    
    @property
    def ms_2DTabD_Bridge_FHWA_WSPRO_coef_typeIII(self) -> ms_2DTabD_Bridge_FHWA_WSPRO_coef_typeIIITable:
        """Table 'ms_2DTabD_Bridge_FHWA_WSPRO_coef_typeIII' ()"""
        return self._tables['ms_2DTabD_Bridge_FHWA_WSPRO_coef_typeIII']
    
    @property
    def ms_2DTabD_Bridge_FHWA_WSPRO_coef_typeIV(self) -> ms_2DTabD_Bridge_FHWA_WSPRO_coef_typeIVTable:
        """Table 'ms_2DTabD_Bridge_FHWA_WSPRO_coef_typeIV' ()"""
        return self._tables['ms_2DTabD_Bridge_FHWA_WSPRO_coef_typeIV']
    
    @property
    def ms_2DTabD_Bridge_FHWA_WSPRO_depth(self) -> ms_2DTabD_Bridge_FHWA_WSPRO_depthTable:
        """Table 'ms_2DTabD_Bridge_FHWA_WSPRO_depth' ()"""
        return self._tables['ms_2DTabD_Bridge_FHWA_WSPRO_depth']
    
    @property
    def ms_2DTabD_Bridge_FHWA_WSPRO_abutment(self) -> ms_2DTabD_Bridge_FHWA_WSPRO_abutmentTable:
        """Table 'ms_2DTabD_Bridge_FHWA_WSPRO_abutment' ()"""
        return self._tables['ms_2DTabD_Bridge_FHWA_WSPRO_abutment']
    
    @property
    def ms_2DTabD_Bridge_FHWA_WSPRO_Piles(self) -> ms_2DTabD_Bridge_FHWA_WSPRO_PilesTable:
        """Table 'ms_2DTabD_Bridge_FHWA_WSPRO_Piles' ()"""
        return self._tables['ms_2DTabD_Bridge_FHWA_WSPRO_Piles']
    
    @property
    def ms_2DTabD_Tabulated_QH(self) -> ms_2DTabD_Tabulated_QHTable:
        """Table 'ms_2DTabD_Tabulated_QH' ()"""
        return self._tables['ms_2DTabD_Tabulated_QH']
    
    @property
    def ms_2DTabD_Tabulated_HQ_UP(self) -> ms_2DTabD_Tabulated_HQ_UPTable:
        """Table 'ms_2DTabD_Tabulated_HQ_UP' ()"""
        return self._tables['ms_2DTabD_Tabulated_HQ_UP']
    
    @property
    def ms_2DTabD_Tabulated_HQ_DOWN(self) -> ms_2DTabD_Tabulated_HQ_DOWNTable:
        """Table 'ms_2DTabD_Tabulated_HQ_DOWN' ()"""
        return self._tables['ms_2DTabD_Tabulated_HQ_DOWN']
    
    @property
    def ms_CRS(self) -> ms_CRSTable:
        """Table 'ms_CRS' (Generic shapes)"""
        return self._tables['ms_CRS']
    
    @property
    def ms_CRSD(self) -> ms_CRSDTable:
        """Table 'ms_CRSD' (Raw data)"""
        return self._tables['ms_CRSD']
    
    @property
    def ms_ProcessedCRSD(self) -> ms_ProcessedCRSDTable:
        """Table 'ms_ProcessedCRSD' (Processed data)"""
        return self._tables['ms_ProcessedCRSD']
    
    @property
    def ms_DPProfile(self) -> ms_DPProfileTable:
        """Table 'ms_DPProfile' (Cyclic profiles)"""
        return self._tables['ms_DPProfile']
    
    @property
    def ms_DPProfileD(self) -> ms_DPProfileDTable:
        """Table 'ms_DPProfileD' (profile data)"""
        return self._tables['ms_DPProfileD']
    
    @property
    def ms_DPPattern(self) -> ms_DPPatternTable:
        """Table 'ms_DPPattern' (Diurnal patterns)"""
        return self._tables['ms_DPPattern']
    
    @property
    def ms_DPPatternD(self) -> ms_DPPatternDTable:
        """Table 'ms_DPPatternD' (Pattern data)"""
        return self._tables['ms_DPPatternD']
    
    @property
    def ms_DPSpecDay(self) -> ms_DPSpecDayTable:
        """Table 'ms_DPSpecDay' (Special days)"""
        return self._tables['ms_DPSpecDay']
    
    @property
    def ms_DPSchedule(self) -> ms_DPScheduleTable:
        """Table 'ms_DPSchedule' (Profile calendars)"""
        return self._tables['ms_DPSchedule']
    
    @property
    def ms_Material(self) -> ms_MaterialTable:
        """Table 'ms_Material' (Materials)"""
        return self._tables['ms_Material']
    
    @property
    def ms_SimpSetting(self) -> ms_SimpSettingTable:
        """Table 'ms_SimpSetting' (ms_SimpSetting)"""
        return self._tables['ms_SimpSetting']
    
    @property
    def ms_SimpMapping(self) -> ms_SimpMappingTable:
        """Table 'ms_SimpMapping' (ms_SimpMapping)"""
        return self._tables['ms_SimpMapping']
    
    @property
    def msm_Node(self) -> msm_NodeTable:
        """Table 'msm_Node' (Nodes)"""
        return self._tables['msm_Node']
    
    @property
    def msm_Link(self) -> msm_LinkTable:
        """Table 'msm_Link' (Pipes and canals)"""
        return self._tables['msm_Link']
    
    @property
    def mrm_Branch(self) -> mrm_BranchTable:
        """Table 'mrm_Branch' (Rivers)"""
        return self._tables['mrm_Branch']
    
    @property
    def mrm_UserDefinedChainage(self) -> mrm_UserDefinedChainageTable:
        """Table 'mrm_UserDefinedChainage' (User defined chainage)"""
        return self._tables['mrm_UserDefinedChainage']
    
    @property
    def mrm_RiverRoutingMethod(self) -> mrm_RiverRoutingMethodTable:
        """Table 'mrm_RiverRoutingMethod' (Simple routing locations)"""
        return self._tables['mrm_RiverRoutingMethod']
    
    @property
    def mrm_BranchRoughnessLocal(self) -> mrm_BranchRoughnessLocalTable:
        """Table 'mrm_BranchRoughnessLocal' (Bed roughness)"""
        return self._tables['mrm_BranchRoughnessLocal']
    
    @property
    def mrm_ZoneSeparatorLocal(self) -> mrm_ZoneSeparatorLocalTable:
        """Table 'mrm_ZoneSeparatorLocal' (Zones separators)"""
        return self._tables['mrm_ZoneSeparatorLocal']
    
    @property
    def mrm_RoughnessFactor(self) -> mrm_RoughnessFactorTable:
        """Table 'mrm_RoughnessFactor' (Roughness factor)"""
        return self._tables['mrm_RoughnessFactor']
    
    @property
    def mrm_BranchConn(self) -> mrm_BranchConnTable:
        """Table 'mrm_BranchConn' (River connection)"""
        return self._tables['mrm_BranchConn']
    
    @property
    def msm_Catchment(self) -> msm_CatchmentTable:
        """Table 'msm_Catchment' (Catchments)"""
        return self._tables['msm_Catchment']
    
    @property
    def msm_CatchCon(self) -> msm_CatchConTable:
        """Table 'msm_CatchCon' (Catchment connections)"""
        return self._tables['msm_CatchCon']
    
    @property
    def msm_Weir(self) -> msm_WeirTable:
        """Table 'msm_Weir' (Weirs)"""
        return self._tables['msm_Weir']
    
    @property
    def msm_Valve(self) -> msm_ValveTable:
        """Table 'msm_Valve' (Valves)"""
        return self._tables['msm_Valve']
    
    @property
    def msm_CurbInlet(self) -> msm_CurbInletTable:
        """Table 'msm_CurbInlet' (Curb inlets)"""
        return self._tables['msm_CurbInlet']
    
    @property
    def msm_Culvert(self) -> msm_CulvertTable:
        """Table 'msm_Culvert' (Culverts)"""
        return self._tables['msm_Culvert']
    
    @property
    def msm_CulvertGeom(self) -> msm_CulvertGeomTable:
        """Table 'msm_CulvertGeom' (Culvert geometry)"""
        return self._tables['msm_CulvertGeom']
    
    @property
    def msm_CulvertHDParam(self) -> msm_CulvertHDParamTable:
        """Table 'msm_CulvertHDParam' (Hydraulic parameters)"""
        return self._tables['msm_CulvertHDParam']
    
    @property
    def msm_CulvertQHFlow(self) -> msm_CulvertQHFlowTable:
        """Table 'msm_CulvertQHFlow' (Q/h relations)"""
        return self._tables['msm_CulvertQHFlow']
    
    @property
    def msm_CulvertOrificeFlowCoeff(self) -> msm_CulvertOrificeFlowCoeffTable:
        """Table 'msm_CulvertOrificeFlowCoeff' (Orifice flow coefficients)"""
        return self._tables['msm_CulvertOrificeFlowCoeff']
    
    @property
    def mrm_Weir(self) -> mrm_WeirTable:
        """Table 'mrm_Weir' (Weirs)"""
        return self._tables['mrm_Weir']
    
    @property
    def mrm_WeirGeom(self) -> mrm_WeirGeomTable:
        """Table 'mrm_WeirGeom' (River weir geometry)"""
        return self._tables['mrm_WeirGeom']
    
    @property
    def mrm_WeirQHRelation(self) -> mrm_WeirQHRelationTable:
        """Table 'mrm_WeirQHRelation' (Weir Qh relations)"""
        return self._tables['mrm_WeirQHRelation']
    
    @property
    def mrm_DirectDischarge(self) -> mrm_DirectDischargeTable:
        """Table 'mrm_DirectDischarge' (Direct discharges)"""
        return self._tables['mrm_DirectDischarge']
    
    @property
    def mrm_Gate(self) -> mrm_GateTable:
        """Table 'mrm_Gate' (Gates)"""
        return self._tables['mrm_Gate']
    
    @property
    def mrm_Pump(self) -> mrm_PumpTable:
        """Table 'mrm_Pump' (Pumps)"""
        return self._tables['mrm_Pump']
    
    @property
    def mrm_Bridge(self) -> mrm_BridgeTable:
        """Table 'mrm_Bridge' (Bridges)"""
        return self._tables['mrm_Bridge']
    
    @property
    def mrm_BridgeOpening(self) -> mrm_BridgeOpeningTable:
        """Table 'mrm_BridgeOpening' (mrm_BridgeOpening)"""
        return self._tables['mrm_BridgeOpening']
    
    @property
    def mrm_BridgeCrs(self) -> mrm_BridgeCrsTable:
        """Table 'mrm_BridgeCrs' (mrm_BridgeCrs)"""
        return self._tables['mrm_BridgeCrs']
    
    @property
    def mrm_Dambreak(self) -> mrm_DambreakTable:
        """Table 'mrm_Dambreak' (Dambreak)"""
        return self._tables['mrm_Dambreak']
    
    @property
    def mrm_EnergyLoss(self) -> mrm_EnergyLossTable:
        """Table 'mrm_EnergyLoss' (Energy losses)"""
        return self._tables['mrm_EnergyLoss']
    
    @property
    def mrm_Tabulated(self) -> mrm_TabulatedTable:
        """Table 'mrm_Tabulated' (Tabulated)"""
        return self._tables['mrm_Tabulated']
    
    @property
    def mrm_Storage(self) -> mrm_StorageTable:
        """Table 'mrm_Storage' (Storages)"""
        return self._tables['mrm_Storage']
    
    @property
    def msm_Pump(self) -> msm_PumpTable:
        """Table 'msm_Pump' (Pumps)"""
        return self._tables['msm_Pump']
    
    @property
    def msm_Orifice(self) -> msm_OrificeTable:
        """Table 'msm_Orifice' (Orifices)"""
        return self._tables['msm_Orifice']
    
    @property
    def msm_BBoundary(self) -> msm_BBoundaryTable:
        """Table 'msm_BBoundary' (Boundary conditions)"""
        return self._tables['msm_BBoundary']
    
    @property
    def msm_BndGridRainWeights(self) -> msm_BndGridRainWeightsTable:
        """Table 'msm_BndGridRainWeights' (msm_BndGridRainWeights)"""
        return self._tables['msm_BndGridRainWeights']
    
    @property
    def msm_WQBoundaryProperties(self) -> msm_WQBoundaryPropertiesTable:
        """Table 'msm_WQBoundaryProperties' (WQ boundary properties)"""
        return self._tables['msm_WQBoundaryProperties']
    
    @property
    def msm_LossPar(self) -> msm_LossParTable:
        """Table 'msm_LossPar' (Outlet head loss)"""
        return self._tables['msm_LossPar']
    
    @property
    def msm_HParA(self) -> msm_HParATable:
        """Table 'msm_HParA' (Parameters time-area)"""
        return self._tables['msm_HParA']
    
    @property
    def msm_HParB(self) -> msm_HParBTable:
        """Table 'msm_HParB' (Parameters kinematic wave)"""
        return self._tables['msm_HParB']
    
    @property
    def msm_HParC(self) -> msm_HParCTable:
        """Table 'msm_HParC' (Parameters linear reservoir)"""
        return self._tables['msm_HParC']
    
    @property
    def msm_HParRDII(self) -> msm_HParRDIITable:
        """Table 'msm_HParRDII' (Parameters RDI)"""
        return self._tables['msm_HParRDII']
    
    @property
    def msm_HParAutoCaliRDII(self) -> msm_HParAutoCaliRDIITable:
        """Table 'msm_HParAutoCaliRDII' (RDI autocalibration)"""
        return self._tables['msm_HParAutoCaliRDII']
    
    @property
    def msm_HParRdiiElevZones(self) -> msm_HParRdiiElevZonesTable:
        """Table 'msm_HParRdiiElevZones' (Elevation zones)"""
        return self._tables['msm_HParRdiiElevZones']
    
    @property
    def msm_HParSeasonalVariation(self) -> msm_HParSeasonalVariationTable:
        """Table 'msm_HParSeasonalVariation' (Seasonal variation)"""
        return self._tables['msm_HParSeasonalVariation']
    
    @property
    def msm_RTC(self) -> msm_RTCTable:
        """Table 'msm_RTC' (Control rules)"""
        return self._tables['msm_RTC']
    
    @property
    def msm_RTCSensor(self) -> msm_RTCSensorTable:
        """Table 'msm_RTCSensor' (Sensors)"""
        return self._tables['msm_RTCSensor']
    
    @property
    def msm_RTCRule(self) -> msm_RTCRuleTable:
        """Table 'msm_RTCRule' (Control rules)"""
        return self._tables['msm_RTCRule']
    
    @property
    def msm_RTCAction(self) -> msm_RTCActionTable:
        """Table 'msm_RTCAction' (Actions)"""
        return self._tables['msm_RTCAction']
    
    @property
    def msm_RTCPID(self) -> msm_RTCPIDTable:
        """Table 'msm_RTCPID' (PID parameters)"""
        return self._tables['msm_RTCPID']
    
    @property
    def msm_LoadPoint(self) -> msm_LoadPointTable:
        """Table 'msm_LoadPoint' (Load points)"""
        return self._tables['msm_LoadPoint']
    
    @property
    def msm_LoadPointConnection(self) -> msm_LoadPointConnectionTable:
        """Table 'msm_LoadPointConnection' (Load point connections)"""
        return self._tables['msm_LoadPointConnection']
    
    @property
    def msm_Project(self) -> msm_ProjectTable:
        """Table 'msm_Project' (Simulation setup)"""
        return self._tables['msm_Project']
    
    @property
    def msm_ProjectOutput(self) -> msm_ProjectOutputTable:
        """Table 'msm_ProjectOutput' (Project outputs)"""
        return self._tables['msm_ProjectOutput']
    
    @property
    def msm_RS(self) -> msm_RSTable:
        """Table 'msm_RS' (Result files)"""
        return self._tables['msm_RS']
    
    @property
    def msm_RSS(self) -> msm_RSSTable:
        """Table 'msm_RSS' (Result selections)"""
        return self._tables['msm_RSS']
    
    @property
    def msm_RSSItem(self) -> msm_RSSItemTable:
        """Table 'msm_RSSItem' (RSSItem)"""
        return self._tables['msm_RSSItem']
    
    @property
    def msm_RSSGeom(self) -> msm_RSSGeomTable:
        """Table 'msm_RSSGeom' (Result selection geometry)"""
        return self._tables['msm_RSSGeom']
    
    @property
    def msm_RSSFormatGeometry(self) -> msm_RSSFormatGeometryTable:
        """Table 'msm_RSSFormatGeometry' (Result selection geometry)"""
        return self._tables['msm_RSSFormatGeometry']
    
    @property
    def msm_RSSDem(self) -> msm_RSSDemTable:
        """Table 'msm_RSSDem' (RSSDem)"""
        return self._tables['msm_RSSDem']
    
    @property
    def msm_ADDispersionLocal(self) -> msm_ADDispersionLocalTable:
        """Table 'msm_ADDispersionLocal' (AD Dispersion)"""
        return self._tables['msm_ADDispersionLocal']
    
    @property
    def msm_ADDispersion(self) -> msm_ADDispersionTable:
        """Table 'msm_ADDispersion' (msm_ADDispersion)"""
        return self._tables['msm_ADDispersion']
    
    @property
    def msm_ADComponentIni(self) -> msm_ADComponentIniTable:
        """Table 'msm_ADComponentIni' (msm_ADComponentIni)"""
        return self._tables['msm_ADComponentIni']
    
    @property
    def msm_ADComponent(self) -> msm_ADComponentTable:
        """Table 'msm_ADComponent' (WQ components)"""
        return self._tables['msm_ADComponent']
    
    @property
    def msm_ADDecay(self) -> msm_ADDecayTable:
        """Table 'msm_ADDecay' (Decay)"""
        return self._tables['msm_ADDecay']
    
    @property
    def msm_ADInitialCondition(self) -> msm_ADInitialConditionTable:
        """Table 'msm_ADInitialCondition' (AD initial conditions)"""
        return self._tables['msm_ADInitialCondition']
    
    @property
    def msm_ADInitialConditionDefault(self) -> msm_ADInitialConditionDefaultTable:
        """Table 'msm_ADInitialConditionDefault' (Default values)"""
        return self._tables['msm_ADInitialConditionDefault']
    
    @property
    def msm_ADInitialConditionLocal(self) -> msm_ADInitialConditionLocalTable:
        """Table 'msm_ADInitialConditionLocal' (Local values)"""
        return self._tables['msm_ADInitialConditionLocal']
    
    @property
    def msm_ADInitialConditionLocalValue(self) -> msm_ADInitialConditionLocalValueTable:
        """Table 'msm_ADInitialConditionLocalValue' (Local values)"""
        return self._tables['msm_ADInitialConditionLocalValue']
    
    @property
    def msm_ADInitialConditionHotstartFile(self) -> msm_ADInitialConditionHotstartFileTable:
        """Table 'msm_ADInitialConditionHotstartFile' (Hotstart files)"""
        return self._tables['msm_ADInitialConditionHotstartFile']
    
    @property
    def msm_LTSRunM(self) -> msm_LTSRunMTable:
        """Table 'msm_LTSRunM' (Run time stop criteria matrix)"""
        return self._tables['msm_LTSRunM']
    
    @property
    def msm_LTSRunS(self) -> msm_LTSRunSTable:
        """Table 'msm_LTSRunS' (Run time stop criteria)"""
        return self._tables['msm_LTSRunS']
    
    @property
    def msm_LTSJobListCriteria(self) -> msm_LTSJobListCriteriaTable:
        """Table 'msm_LTSJobListCriteria' (Job list criteria)"""
        return self._tables['msm_LTSJobListCriteria']
    
    @property
    def msm_LTSDwfTs(self) -> msm_LTSDwfTsTable:
        """Table 'msm_LTSDwfTs' (LTS Continuous TS output)"""
        return self._tables['msm_LTSDwfTs']
    
    @property
    def msm_LTSInit(self) -> msm_LTSInitTable:
        """Table 'msm_LTSInit' (LTS initial conditions)"""
        return self._tables['msm_LTSInit']
    
    @property
    def msm_LTSInito(self) -> msm_LTSInitoTable:
        """Table 'msm_LTSInito' (msm_LTSInito)"""
        return self._tables['msm_LTSInito']
    
    @property
    def msm_LTSResult(self) -> msm_LTSResultTable:
        """Table 'msm_LTSResult' (LTS Global parameters)"""
        return self._tables['msm_LTSResult']
    
    @property
    def msm_LTSResultLocal(self) -> msm_LTSResultLocalTable:
        """Table 'msm_LTSResultLocal' (Statistics specifications)"""
        return self._tables['msm_LTSResultLocal']
    
    @property
    def msm_LIDusage(self) -> msm_LIDusageTable:
        """Table 'msm_LIDusage' (LID deployment)"""
        return self._tables['msm_LIDusage']
    
    @property
    def msm_LIDcontrol(self) -> msm_LIDcontrolTable:
        """Table 'msm_LIDcontrol' (LID properties)"""
        return self._tables['msm_LIDcontrol']
    
    @property
    def msm_LIDRemoval(self) -> msm_LIDRemovalTable:
        """Table 'msm_LIDRemoval' (Pollutions removal in LIDS)"""
        return self._tables['msm_LIDRemoval']
    
    @property
    def msm_ResultSelectionQuantity(self) -> msm_ResultSelectionQuantityTable:
        """Table 'msm_ResultSelectionQuantity' (msm_ResultSelectionQuantity)"""
        return self._tables['msm_ResultSelectionQuantity']
    
    @property
    def msm_ECOLABCoeff(self) -> msm_ECOLABCoeffTable:
        """Table 'msm_ECOLABCoeff' (MIKE ECO Lab constants)"""
        return self._tables['msm_ECOLABCoeff']
    
    @property
    def msm_ECOLABCoeffLocal(self) -> msm_ECOLABCoeffLocalTable:
        """Table 'msm_ECOLABCoeffLocal' (MIKE ECO LAB constants local values)"""
        return self._tables['msm_ECOLABCoeffLocal']
    
    @property
    def msm_ECOLABForcing(self) -> msm_ECOLABForcingTable:
        """Table 'msm_ECOLABForcing' (MIKE ECO Lab forcings)"""
        return self._tables['msm_ECOLABForcing']
    
    @property
    def msm_ECOLABComponent(self) -> msm_ECOLABComponentTable:
        """Table 'msm_ECOLABComponent' (MIKE ECO Lab state variables)"""
        return self._tables['msm_ECOLABComponent']
    
    @property
    def msm_ECOLABTemplate(self) -> msm_ECOLABTemplateTable:
        """Table 'msm_ECOLABTemplate' (MIKE ECO Lab templates)"""
        return self._tables['msm_ECOLABTemplate']
    
    @property
    def msm_ECOLABOutput(self) -> msm_ECOLABOutputTable:
        """Table 'msm_ECOLABOutput' (ECOLAB Output)"""
        return self._tables['msm_ECOLABOutput']
    
    @property
    def msm_SWQPollutant(self) -> msm_SWQPollutantTable:
        """Table 'msm_SWQPollutant' (SWQ advanced methods)"""
        return self._tables['msm_SWQPollutant']
    
    @property
    def msm_SWQGlobalData(self) -> msm_SWQGlobalDataTable:
        """Table 'msm_SWQGlobalData' (SWQ global data)"""
        return self._tables['msm_SWQGlobalData']
    
    @property
    def msm_SWQAttachedPollutant(self) -> msm_SWQAttachedPollutantTable:
        """Table 'msm_SWQAttachedPollutant' (Attached pollutant)"""
        return self._tables['msm_SWQAttachedPollutant']
    
    @property
    def msm_HtmlSummary(self) -> msm_HtmlSummaryTable:
        """Table 'msm_HtmlSummary' (Network summary)"""
        return self._tables['msm_HtmlSummary']
    
    @property
    def msm_OnGrade(self) -> msm_OnGradeTable:
        """Table 'msm_OnGrade' (OnGrade captures)"""
        return self._tables['msm_OnGrade']
    
    @property
    def msm_OnGradeD(self) -> msm_OnGradeDTable:
        """Table 'msm_OnGradeD' (OnGrade capture data)"""
        return self._tables['msm_OnGradeD']
    
    @property
    def msm_ST(self) -> msm_STTable:
        """Table 'msm_ST' (General parameters)"""
        return self._tables['msm_ST']
    
    @property
    def msm_STFraction(self) -> msm_STFractionTable:
        """Table 'msm_STFraction' (Sediment fractions)"""
        return self._tables['msm_STFraction']
    
    @property
    def mrm_STAdvFraction(self) -> mrm_STAdvFractionTable:
        """Table 'mrm_STAdvFraction' (Sediment fractions)"""
        return self._tables['mrm_STAdvFraction']
    
    @property
    def mrm_STAdvFracGrainLocal(self) -> mrm_STAdvFracGrainLocalTable:
        """Table 'mrm_STAdvFracGrainLocal' (mrm_STAdvFracGrainLocal)"""
        return self._tables['mrm_STAdvFracGrainLocal']
    
    @property
    def mrm_STAdvFracSusLocal(self) -> mrm_STAdvFracSusLocalTable:
        """Table 'mrm_STAdvFracSusLocal' (mrm_STAdvFracSusLocal)"""
        return self._tables['mrm_STAdvFracSusLocal']
    
    @property
    def msm_STInitDepthLocal(self) -> msm_STInitDepthLocalTable:
        """Table 'msm_STInitDepthLocal' (ST initial depths)"""
        return self._tables['msm_STInitDepthLocal']
    
    @property
    def msm_STInitDepthFractDefault(self) -> msm_STInitDepthFractDefaultTable:
        """Table 'msm_STInitDepthFractDefault' (msm_STInitDepthFractDefault)"""
        return self._tables['msm_STInitDepthFractDefault']
    
    @property
    def msm_STInitDepthFractLocal(self) -> msm_STInitDepthFractLocalTable:
        """Table 'msm_STInitDepthFractLocal' (msm_STInitDepthFractLocal)"""
        return self._tables['msm_STInitDepthFractLocal']
    
    @property
    def msm_STPipesRoughnessLocal(self) -> msm_STPipesRoughnessLocalTable:
        """Table 'msm_STPipesRoughnessLocal' (Pipes roughness)"""
        return self._tables['msm_STPipesRoughnessLocal']
    
    @property
    def msm_STRemovalBasin(self) -> msm_STRemovalBasinTable:
        """Table 'msm_STRemovalBasin' (Sediment removal in basins)"""
        return self._tables['msm_STRemovalBasin']
    
    @property
    def msm_STRemovalWeir(self) -> msm_STRemovalWeirTable:
        """Table 'msm_STRemovalWeir' (Sediment removal in weirs)"""
        return self._tables['msm_STRemovalWeir']
    
    @property
    def mrm_STLocalBedParThick(self) -> mrm_STLocalBedParThickTable:
        """Table 'mrm_STLocalBedParThick' (Local target thickness)"""
        return self._tables['mrm_STLocalBedParThick']
    
    @property
    def mrm_STLocalBedParMorph(self) -> mrm_STLocalBedParMorphTable:
        """Table 'mrm_STLocalBedParMorph' (Local update method)"""
        return self._tables['mrm_STLocalBedParMorph']
    
    @property
    def mrm_STInitConcentratDefault(self) -> mrm_STInitConcentratDefaultTable:
        """Table 'mrm_STInitConcentratDefault' (ST initial concentrations)"""
        return self._tables['mrm_STInitConcentratDefault']
    
    @property
    def mrm_STInitConcentratLocal(self) -> mrm_STInitConcentratLocalTable:
        """Table 'mrm_STInitConcentratLocal' (ST initial concentrations)"""
        return self._tables['mrm_STInitConcentratLocal']
    
    @property
    def msm_HDInitialCondition(self) -> msm_HDInitialConditionTable:
        """Table 'msm_HDInitialCondition' (Initial conditions)"""
        return self._tables['msm_HDInitialCondition']
    
    @property
    def msm_HDInitialConditionLocal(self) -> msm_HDInitialConditionLocalTable:
        """Table 'msm_HDInitialConditionLocal' (Local values)"""
        return self._tables['msm_HDInitialConditionLocal']
    
    @property
    def msm_HDInitialConditionHotstartFile(self) -> msm_HDInitialConditionHotstartFileTable:
        """Table 'msm_HDInitialConditionHotstartFile' (Hotstart files)"""
        return self._tables['msm_HDInitialConditionHotstartFile']
    
    @property
    def msm_AlarmLevel(self) -> msm_AlarmLevelTable:
        """Table 'msm_AlarmLevel' (Alarm levels)"""
        return self._tables['msm_AlarmLevel']
    
    @property
    def msm_AlarmLevelD(self) -> msm_AlarmLevelDTable:
        """Table 'msm_AlarmLevelD' (Levels in alarm set)"""
        return self._tables['msm_AlarmLevelD']
    
    @property
    def msm_PumpESE(self) -> msm_PumpESETable:
        """Table 'msm_PumpESE' (Emergency storage estimation)"""
        return self._tables['msm_PumpESE']
    
    @property
    def msm_PumpESED(self) -> msm_PumpESEDTable:
        """Table 'msm_PumpESED' (ESE setupD)"""
        return self._tables['msm_PumpESED']
    
    @property
    def mrm_DAGeneralPara(self) -> mrm_DAGeneralParaTable:
        """Table 'mrm_DAGeneralPara' (General parameters)"""
        return self._tables['mrm_DAGeneralPara']
    
    @property
    def mrm_DAUpdatePara(self) -> mrm_DAUpdateParaTable:
        """Table 'mrm_DAUpdatePara' (Update parameters)"""
        return self._tables['mrm_DAUpdatePara']
    
    @property
    def mrm_DAStandardDeviation(self) -> mrm_DAStandardDeviationTable:
        """Table 'mrm_DAStandardDeviation' (Standard deviation)"""
        return self._tables['mrm_DAStandardDeviation']
    
    @property
    def mrm_DAErrorForecastEquations(self) -> mrm_DAErrorForecastEquationsTable:
        """Table 'mrm_DAErrorForecastEquations' (Error forecast equations)"""
        return self._tables['mrm_DAErrorForecastEquations']
    
    @property
    def mrm_DAErrorForecastPara(self) -> mrm_DAErrorForecastParaTable:
        """Table 'mrm_DAErrorForecastPara' (Error forecast equations parameter)"""
        return self._tables['mrm_DAErrorForecastPara']
    
    @property
    def mrm_DAPerturbationsPara(self) -> mrm_DAPerturbationsParaTable:
        """Table 'mrm_DAPerturbationsPara' (Perturbations parameters)"""
        return self._tables['mrm_DAPerturbationsPara']
    
    @property
    def mrm_WindScaleFactorLocal(self) -> mrm_WindScaleFactorLocalTable:
        """Table 'mrm_WindScaleFactorLocal' (Wind scaling factors)"""
        return self._tables['mrm_WindScaleFactorLocal']
    
    @property
    def mrm_LeakageCoefficients(self) -> mrm_LeakageCoefficientsTable:
        """Table 'mrm_LeakageCoefficients' (Leakage coefficients)"""
        return self._tables['mrm_LeakageCoefficients']
    
    @property
    def msm_HDAddPercent(self) -> msm_HDAddPercentTable:
        """Table 'msm_HDAddPercent' (Intervals)"""
        return self._tables['msm_HDAddPercent']
    
    @property
    def msm_RRAddPercent(self) -> msm_RRAddPercentTable:
        """Table 'msm_RRAddPercent' (Intervals)"""
        return self._tables['msm_RRAddPercent']
    
    @property
    def mrm_SHECouplings(self) -> mrm_SHECouplingsTable:
        """Table 'mrm_SHECouplings' (Groundwater couplings)"""
        return self._tables['mrm_SHECouplings']
    
    @property
    def mrm_STNonScrLocalBedLevel(self) -> mrm_STNonScrLocalBedLevelTable:
        """Table 'mrm_STNonScrLocalBedLevel' (Non-scouring bed level)"""
        return self._tables['mrm_STNonScrLocalBedLevel']
    
    @property
    def mrm_STPassiveLink(self) -> mrm_STPassiveLinkTable:
        """Table 'mrm_STPassiveLink' (Passive links)"""
        return self._tables['mrm_STPassiveLink']
    
    @property
    def msm_LandUse(self) -> msm_LandUseTable:
        """Table 'msm_LandUse' (Land uses)"""
        return self._tables['msm_LandUse']
    
    @property
    def msm_CatchLandUse(self) -> msm_CatchLandUseTable:
        """Table 'msm_CatchLandUse' (msm_CatchLandUse)"""
        return self._tables['msm_CatchLandUse']
    
    @property
    def mw_PPattern(self) -> mw_PPatternTable:
        """Table 'mw_PPattern' (Patterns)"""
        return self._tables['mw_PPattern']
    
    @property
    def mw_PPatternD(self) -> mw_PPatternDTable:
        """Table 'mw_PPatternD' (Pattern data)"""
        return self._tables['mw_PPatternD']
    
    @property
    def mw_Curve(self) -> mw_CurveTable:
        """Table 'mw_Curve' (Curves and relations)"""
        return self._tables['mw_Curve']
    
    @property
    def mw_CurveD(self) -> mw_CurveDTable:
        """Table 'mw_CurveD' (Curve values)"""
        return self._tables['mw_CurveD']
    
    @property
    def mw_Junction(self) -> mw_JunctionTable:
        """Table 'mw_Junction' (Junctions)"""
        return self._tables['mw_Junction']
    
    @property
    def mw_Tank(self) -> mw_TankTable:
        """Table 'mw_Tank' (Tanks)"""
        return self._tables['mw_Tank']
    
    @property
    def mw_AirChamber(self) -> mw_AirChamberTable:
        """Table 'mw_AirChamber' (Air-chambers)"""
        return self._tables['mw_AirChamber']
    
    @property
    def mw_MDemand(self) -> mw_MDemandTable:
        """Table 'mw_MDemand' (Multiple demands)"""
        return self._tables['mw_MDemand']
    
    @property
    def mw_Pipe(self) -> mw_PipeTable:
        """Table 'mw_Pipe' (Pipes)"""
        return self._tables['mw_Pipe']
    
    @property
    def mw_Pump(self) -> mw_PumpTable:
        """Table 'mw_Pump' (Pumps)"""
        return self._tables['mw_Pump']
    
    @property
    def mw_Valve(self) -> mw_ValveTable:
        """Table 'mw_Valve' (Valves)"""
        return self._tables['mw_Valve']
    
    @property
    def mw_Control(self) -> mw_ControlTable:
        """Table 'mw_Control' (Simple controls)"""
        return self._tables['mw_Control']
    
    @property
    def mw_DemAlloc(self) -> mw_DemAllocTable:
        """Table 'mw_DemAlloc' (Demand allocations)"""
        return self._tables['mw_DemAlloc']
    
    @property
    def mw_DemAllocConn(self) -> mw_DemAllocConnTable:
        """Table 'mw_DemAllocConn' (Demand allocation connection)"""
        return self._tables['mw_DemAllocConn']
    
    @property
    def mw_PumpStation(self) -> mw_PumpStationTable:
        """Table 'mw_PumpStation' (Pump stations)"""
        return self._tables['mw_PumpStation']
    
    @property
    def mw_PumpStationConn(self) -> mw_PumpStationConnTable:
        """Table 'mw_PumpStationConn' (Pump stations connection)"""
        return self._tables['mw_PumpStationConn']
    
    @property
    def mw_SpecDay(self) -> mw_SpecDayTable:
        """Table 'mw_SpecDay' (mw_SpecDay)"""
        return self._tables['mw_SpecDay']
    
    @property
    def mw_ZoneDef(self) -> mw_ZoneDefTable:
        """Table 'mw_ZoneDef' (Zones)"""
        return self._tables['mw_ZoneDef']
    
    @property
    def mw_ZoneWB(self) -> mw_ZoneWBTable:
        """Table 'mw_ZoneWB' (mw_ZoneWB)"""
        return self._tables['mw_ZoneWB']
    
    @property
    def mw_DemStat(self) -> mw_DemStatTable:
        """Table 'mw_DemStat' (Statistics and redistribution)"""
        return self._tables['mw_DemStat']
    
    @property
    def mw_DemStatConfig(self) -> mw_DemStatConfigTable:
        """Table 'mw_DemStatConfig' (Statistics and redistribution)"""
        return self._tables['mw_DemStatConfig']
    
    @property
    def mw_Project(self) -> mw_ProjectTable:
        """Table 'mw_Project' (Simulation setup)"""
        return self._tables['mw_Project']
    
    @property
    def mw_Source(self) -> mw_SourceTable:
        """Table 'mw_Source' (Point constituent source)"""
        return self._tables['mw_Source']
    
    @property
    def mw_TraceNode(self) -> mw_TraceNodeTable:
        """Table 'mw_TraceNode' (Trace nodes)"""
        return self._tables['mw_TraceNode']
    
    @property
    def mw_Turbine(self) -> mw_TurbineTable:
        """Table 'mw_Turbine' (Turbines)"""
        return self._tables['mw_Turbine']
    
    @property
    def mw_Friction(self) -> mw_FrictionTable:
        """Table 'mw_Friction' (Roughness)"""
        return self._tables['mw_Friction']
    
    @property
    def mw_Loss(self) -> mw_LossTable:
        """Table 'mw_Loss' (Loss coefficient)"""
        return self._tables['mw_Loss']
    
    @property
    def mw_RTC(self) -> mw_RTCTable:
        """Table 'mw_RTC' (Real time control)"""
        return self._tables['mw_RTC']
    
    @property
    def mw_Energy(self) -> mw_EnergyTable:
        """Table 'mw_Energy' (Cost analysis)"""
        return self._tables['mw_Energy']
    
    @property
    def mw_Rule(self) -> mw_RuleTable:
        """Table 'mw_Rule' (Extended rule-based controls)"""
        return self._tables['mw_Rule']
    
    @property
    def mw_Reliability(self) -> mw_ReliabilityTable:
        """Table 'mw_Reliability' (mw_Reliability)"""
        return self._tables['mw_Reliability']
    
    @property
    def mw_ReliabilityLocal(self) -> mw_ReliabilityLocalTable:
        """Table 'mw_ReliabilityLocal' (Pressure dependent demands)"""
        return self._tables['mw_ReliabilityLocal']
    
    @property
    def mw_FireFlow(self) -> mw_FireFlowTable:
        """Table 'mw_FireFlow' (Fire flow analysis)"""
        return self._tables['mw_FireFlow']
    
    @property
    def mw_Flushing(self) -> mw_FlushingTable:
        """Table 'mw_Flushing' (Flushing analysis)"""
        return self._tables['mw_Flushing']
    
    @property
    def mw_FlushingOutlet(self) -> mw_FlushingOutletTable:
        """Table 'mw_FlushingOutlet' (Flushing outlet table)"""
        return self._tables['mw_FlushingOutlet']
    
    @property
    def mw_ShutdownPlanning(self) -> mw_ShutdownPlanningTable:
        """Table 'mw_ShutdownPlanning' (Shutdown planning)"""
        return self._tables['mw_ShutdownPlanning']
    
    @property
    def mw_ShutdownValve(self) -> mw_ShutdownValveTable:
        """Table 'mw_ShutdownValve' (Shutdown valve)"""
        return self._tables['mw_ShutdownValve']
    
    @property
    def mw_PipeRel(self) -> mw_PipeRelTable:
        """Table 'mw_PipeRel' (Network vulnerability)"""
        return self._tables['mw_PipeRel']
    
    @property
    def mw_WH_Boundary(self) -> mw_WH_BoundaryTable:
        """Table 'mw_WH_Boundary' (Boundary conditions)"""
        return self._tables['mw_WH_Boundary']
    
    @property
    def mw_WDOSettings(self) -> mw_WDOSettingsTable:
        """Table 'mw_WDOSettings' (Settings)"""
        return self._tables['mw_WDOSettings']
    
    @property
    def mw_WDOSensors(self) -> mw_WDOSensorsTable:
        """Table 'mw_WDOSensors' (Sensors)"""
        return self._tables['mw_WDOSensors']
    
    @property
    def mw_Optimization(self) -> mw_OptimizationTable:
        """Table 'mw_Optimization' (Optimization)"""
        return self._tables['mw_Optimization']
    
    @property
    def mw_OptimizationControl(self) -> mw_OptimizationControlTable:
        """Table 'mw_OptimizationControl' (Controls)"""
        return self._tables['mw_OptimizationControl']
    
    @property
    def mw_OptimizationTarget(self) -> mw_OptimizationTargetTable:
        """Table 'mw_OptimizationTarget' (mw_OptimizationTarget)"""
        return self._tables['mw_OptimizationTarget']
    
    @property
    def mw_OptimizationTargetWB(self) -> mw_OptimizationTargetWBTable:
        """Table 'mw_OptimizationTargetWB' (mw_OptimizationTargetWB)"""
        return self._tables['mw_OptimizationTargetWB']
    
    @property
    def mw_WDOControls(self) -> mw_WDOControlsTable:
        """Table 'mw_WDOControls' (Controls)"""
        return self._tables['mw_WDOControls']
    
    @property
    def mw_WDODemandZones(self) -> mw_WDODemandZonesTable:
        """Table 'mw_WDODemandZones' (Demand zones)"""
        return self._tables['mw_WDODemandZones']
    
    @property
    def mw_WDODemandPredictions(self) -> mw_WDODemandPredictionsTable:
        """Table 'mw_WDODemandPredictions' (Demand predictions)"""
        return self._tables['mw_WDODemandPredictions']
    
    @property
    def mw_WDOComparisons(self) -> mw_WDOComparisonsTable:
        """Table 'mw_WDOComparisons' (Comparisons)"""
        return self._tables['mw_WDOComparisons']
    
    @property
    def mw_EPAMSX(self) -> mw_EPAMSXTable:
        """Table 'mw_EPAMSX' (Multi-species analysis)"""
        return self._tables['mw_EPAMSX']
    
    @property
    def mw_Autocalibration(self) -> mw_AutocalibrationTable:
        """Table 'mw_Autocalibration' (Autocalibration)"""
        return self._tables['mw_Autocalibration']
    
    @property
    def mw_AutocaliPipesFrict(self) -> mw_AutocaliPipesFrictTable:
        """Table 'mw_AutocaliPipesFrict' (mw_AutocaliPipesFrict)"""
        return self._tables['mw_AutocaliPipesFrict']
    
    @property
    def mw_AutocaliNodeDemands(self) -> mw_AutocaliNodeDemandsTable:
        """Table 'mw_AutocaliNodeDemands' (mw_AutocaliNodeDemands)"""
        return self._tables['mw_AutocaliNodeDemands']
    
    @property
    def mw_AutocaliClosedLinks(self) -> mw_AutocaliClosedLinksTable:
        """Table 'mw_AutocaliClosedLinks' (mw_AutocaliClosedLinks)"""
        return self._tables['mw_AutocaliClosedLinks']
    
    @property
    def mw_AutocaliLeaks(self) -> mw_AutocaliLeaksTable:
        """Table 'mw_AutocaliLeaks' (mw_AutocaliLeaks)"""
        return self._tables['mw_AutocaliLeaks']
    
    @property
    def mw_AutocaliTargets(self) -> mw_AutocaliTargetsTable:
        """Table 'mw_AutocaliTargets' (mw_AutocaliTargets)"""
        return self._tables['mw_AutocaliTargets']
    
    @property
    def mwRes_ValveCriticality(self) -> mwRes_ValveCriticalityTable:
        """Table 'mwRes_ValveCriticality' (Valve criticality)"""
        return self._tables['mwRes_ValveCriticality']
    
    @property
    def mwRes_Sustainability_Node(self) -> mwRes_Sustainability_NodeTable:
        """Table 'mwRes_Sustainability_Node' (mwRes_Sustainability_Node)"""
        return self._tables['mwRes_Sustainability_Node']
    
    @property
    def mwRes_Sustainability_Link(self) -> mwRes_Sustainability_LinkTable:
        """Table 'mwRes_Sustainability_Link' (mwRes_Sustainability_Link)"""
        return self._tables['mwRes_Sustainability_Link']
    
    @property
    def m21_pfsSection(self) -> m21_pfsSectionTable:
        """Table 'm21_pfsSection' (m21_pfsSection)"""
        return self._tables['m21_pfsSection']
    
    @property
    def m21_pfsKeyword(self) -> m21_pfsKeywordTable:
        """Table 'm21_pfsKeyword' (m21_pfsKeyword)"""
        return self._tables['m21_pfsKeyword']
    
    @property
    def m21_pfsParam(self) -> m21_pfsParamTable:
        """Table 'm21_pfsParam' (m21_pfsParam)"""
        return self._tables['m21_pfsParam']
    
    @property
    def m2d_GlobalSetting(self) -> m2d_GlobalSettingTable:
        """Table 'm2d_GlobalSetting' (m2d_GlobalSetting)"""
        return self._tables['m2d_GlobalSetting']
    
    @property
    def m2d_SurfaceRoughnessArea(self) -> m2d_SurfaceRoughnessAreaTable:
        """Table 'm2d_SurfaceRoughnessArea' (2D surface roughness)"""
        return self._tables['m2d_SurfaceRoughnessArea']
    
    @property
    def m2d_SurfaceRoughnessValue(self) -> m2d_SurfaceRoughnessValueTable:
        """Table 'm2d_SurfaceRoughnessValue' (2D surface roughness)"""
        return self._tables['m2d_SurfaceRoughnessValue']
    
    @property
    def m2d_EddyViscosityArea(self) -> m2d_EddyViscosityAreaTable:
        """Table 'm2d_EddyViscosityArea' (2D eddy viscosity)"""
        return self._tables['m2d_EddyViscosityArea']
    
    @property
    def m2d_Infiltration(self) -> m2d_InfiltrationTable:
        """Table 'm2d_Infiltration' (2D infiltration)"""
        return self._tables['m2d_Infiltration']
    
    @property
    def m2d_InfiltrationLandCover(self) -> m2d_InfiltrationLandCoverTable:
        """Table 'm2d_InfiltrationLandCover' (2D infiltration)"""
        return self._tables['m2d_InfiltrationLandCover']
    
    @property
    def m2d_InitialConditionArea(self) -> m2d_InitialConditionAreaTable:
        """Table 'm2d_InitialConditionArea' (2D initial conditions)"""
        return self._tables['m2d_InitialConditionArea']
    
    @property
    def m2d_StructureDike(self) -> m2d_StructureDikeTable:
        """Table 'm2d_StructureDike' (2D dikes)"""
        return self._tables['m2d_StructureDike']
    
    @property
    def m2d_StructureWeir(self) -> m2d_StructureWeirTable:
        """Table 'm2d_StructureWeir' (2D weirs)"""
        return self._tables['m2d_StructureWeir']
    
    @property
    def m2d_StructureWeirD(self) -> m2d_StructureWeirDTable:
        """Table 'm2d_StructureWeirD' (2D weir geometry)"""
        return self._tables['m2d_StructureWeirD']
    
    @property
    def m2d_StructureCulvert(self) -> m2d_StructureCulvertTable:
        """Table 'm2d_StructureCulvert' (2D culverts)"""
        return self._tables['m2d_StructureCulvert']
    
    @property
    def m2d_StructureCulvertD(self) -> m2d_StructureCulvertDTable:
        """Table 'm2d_StructureCulvertD' (2D culvert geometry)"""
        return self._tables['m2d_StructureCulvertD']
    
    @property
    def m2d_Coupling(self) -> m2d_CouplingTable:
        """Table 'm2d_Coupling' (1D-2D couplings)"""
        return self._tables['m2d_Coupling']
    
    @property
    def m2d_CouplingConn(self) -> m2d_CouplingConnTable:
        """Table 'm2d_CouplingConn' (Couple Connection)"""
        return self._tables['m2d_CouplingConn']
    
    @property
    def m2d_CouplingEngineConn(self) -> m2d_CouplingEngineConnTable:
        """Table 'm2d_CouplingEngineConn' (Coupling engine connections)"""
        return self._tables['m2d_CouplingEngineConn']
    
    @property
    def m2d_CouplingEngineFace(self) -> m2d_CouplingEngineFaceTable:
        """Table 'm2d_CouplingEngineFace' (Coupling engine faces)"""
        return self._tables['m2d_CouplingEngineFace']
    
    @property
    def m2d_MeshArc(self) -> m2d_MeshArcTable:
        """Table 'm2d_MeshArc' (Mesh arc)"""
        return self._tables['m2d_MeshArc']
    
    @property
    def m2d_MeshLocalArea(self) -> m2d_MeshLocalAreaTable:
        """Table 'm2d_MeshLocalArea' (Mesh polygon marker)"""
        return self._tables['m2d_MeshLocalArea']
    
    @property
    def m2d_GridDefinition(self) -> m2d_GridDefinitionTable:
        """Table 'm2d_GridDefinition' (Grid definition)"""
        return self._tables['m2d_GridDefinition']
    
    @property
    def m2d_GridInactiveArea(self) -> m2d_GridInactiveAreaTable:
        """Table 'm2d_GridInactiveArea' (Grid inactive area)"""
        return self._tables['m2d_GridInactiveArea']
    
    @property
    def m2d_Boundary(self) -> m2d_BoundaryTable:
        """Table 'm2d_Boundary' (2D boundary conditions)"""
        return self._tables['m2d_Boundary']
    
    @property
    def m2d_BndQHRelation(self) -> m2d_BndQHRelationTable:
        """Table 'm2d_BndQHRelation' (Q/h relation)"""
        return self._tables['m2d_BndQHRelation']
    
    @property
    def m2d_BndDistributedSource(self) -> m2d_BndDistributedSourceTable:
        """Table 'm2d_BndDistributedSource' (m2d_BndDistributedSource)"""
        return self._tables['m2d_BndDistributedSource']
    
    @property
    def m2d_ADInitalCondition(self) -> m2d_ADInitalConditionTable:
        """Table 'm2d_ADInitalCondition' (2D AD initial conditions)"""
        return self._tables['m2d_ADInitalCondition']
    
    @property
    def m2d_ADInitalConditionArea(self) -> m2d_ADInitalConditionAreaTable:
        """Table 'm2d_ADInitalConditionArea' (2D AD initial conditions)"""
        return self._tables['m2d_ADInitalConditionArea']
    
    @property
    def m2d_ADInitalConditionD(self) -> m2d_ADInitalConditionDTable:
        """Table 'm2d_ADInitalConditionD' (AD initial conditions area in 2D domain)"""
        return self._tables['m2d_ADInitalConditionD']
    
    @property
    def m2d_ADPrecipitation(self) -> m2d_ADPrecipitationTable:
        """Table 'm2d_ADPrecipitation' (2D WQ precipitation)"""
        return self._tables['m2d_ADPrecipitation']
    
    @property
    def m2d_ADPrecipitationArea(self) -> m2d_ADPrecipitationAreaTable:
        """Table 'm2d_ADPrecipitationArea' (2D AD precipitation)"""
        return self._tables['m2d_ADPrecipitationArea']
    
    @property
    def m2d_ADPrecipitationD(self) -> m2d_ADPrecipitationDTable:
        """Table 'm2d_ADPrecipitationD' (AD precipitation area in 2D domain)"""
        return self._tables['m2d_ADPrecipitationD']
    
    @property
    def m2d_ADDecay(self) -> m2d_ADDecayTable:
        """Table 'm2d_ADDecay' (2D decay)"""
        return self._tables['m2d_ADDecay']
    
    @property
    def m2d_ADInfiltration(self) -> m2d_ADInfiltrationTable:
        """Table 'm2d_ADInfiltration' (2D WQ infiltration)"""
        return self._tables['m2d_ADInfiltration']
    
    @property
    def m2d_ADInfiltrationArea(self) -> m2d_ADInfiltrationAreaTable:
        """Table 'm2d_ADInfiltrationArea' (2D AD infiltration)"""
        return self._tables['m2d_ADInfiltrationArea']
    
    @property
    def m2d_ADInfiltrationD(self) -> m2d_ADInfiltrationDTable:
        """Table 'm2d_ADInfiltrationD' (AD infiltration area in 2D domain)"""
        return self._tables['m2d_ADInfiltrationD']
    
    @property
    def m2d_ADEvaporation(self) -> m2d_ADEvaporationTable:
        """Table 'm2d_ADEvaporation' (2D WQ evaporation)"""
        return self._tables['m2d_ADEvaporation']
    
    @property
    def m2d_ADEvaporationArea(self) -> m2d_ADEvaporationAreaTable:
        """Table 'm2d_ADEvaporationArea' (2D AD evaporation)"""
        return self._tables['m2d_ADEvaporationArea']
    
    @property
    def m2d_ADEvaporationD(self) -> m2d_ADEvaporationDTable:
        """Table 'm2d_ADEvaporationD' (AD evaporations area in 2D domain)"""
        return self._tables['m2d_ADEvaporationD']
    
    @property
    def m2d_ADDispersion(self) -> m2d_ADDispersionTable:
        """Table 'm2d_ADDispersion' (2D AD dispersion)"""
        return self._tables['m2d_ADDispersion']
    
    @property
    def m2d_ADDispersionD(self) -> m2d_ADDispersionDTable:
        """Table 'm2d_ADDispersionD' (Dispersion area, 2D)"""
        return self._tables['m2d_ADDispersionD']
    
    @property
    def m2d_ADDispersionArea(self) -> m2d_ADDispersionAreaTable:
        """Table 'm2d_ADDispersionArea' (2D AD dispersion)"""
        return self._tables['m2d_ADDispersionArea']
    
    @property
    def m2d_WQBoundary(self) -> m2d_WQBoundaryTable:
        """Table 'm2d_WQBoundary' (2D WQ boundaries)"""
        return self._tables['m2d_WQBoundary']
    
    @property
    def m2d_InfBuilding(self) -> m2d_InfBuildingTable:
        """Table 'm2d_InfBuilding' (Building)"""
        return self._tables['m2d_InfBuilding']
    
    @property
    def m2d_InfRoad(self) -> m2d_InfRoadTable:
        """Table 'm2d_InfRoad' (Road)"""
        return self._tables['m2d_InfRoad']
    
    @property
    def mss_Node(self) -> mss_NodeTable:
        """Table 'mss_Node' (Nodes)"""
        return self._tables['mss_Node']
    
    @property
    def mss_Link(self) -> mss_LinkTable:
        """Table 'mss_Link' (Conduits)"""
        return self._tables['mss_Link']
    
    @property
    def mss_CatchCon(self) -> mss_CatchConTable:
        """Table 'mss_CatchCon' (SWMM catchment connections)"""
        return self._tables['mss_CatchCon']
    
    @property
    def mss_Orifice(self) -> mss_OrificeTable:
        """Table 'mss_Orifice' (Orifices)"""
        return self._tables['mss_Orifice']
    
    @property
    def mss_Pump(self) -> mss_PumpTable:
        """Table 'mss_Pump' (Pumps)"""
        return self._tables['mss_Pump']
    
    @property
    def mss_Outlet(self) -> mss_OutletTable:
        """Table 'mss_Outlet' (Outlets)"""
        return self._tables['mss_Outlet']
    
    @property
    def mss_Weir(self) -> mss_WeirTable:
        """Table 'mss_Weir' (Weirs)"""
        return self._tables['mss_Weir']
    
    @property
    def mss_Tab(self) -> mss_TabTable:
        """Table 'mss_Tab' (Curves and relations)"""
        return self._tables['mss_Tab']
    
    @property
    def mss_TabD(self) -> mss_TabDTable:
        """Table 'mss_TabD' (Curve values)"""
        return self._tables['mss_TabD']
    
    @property
    def mss_Project(self) -> mss_ProjectTable:
        """Table 'mss_Project' (Simulation setup)"""
        return self._tables['mss_Project']
    
    @property
    def mss_Timeseries(self) -> mss_TimeseriesTable:
        """Table 'mss_Timeseries' (Time series)"""
        return self._tables['mss_Timeseries']
    
    @property
    def mss_TimeseriesD(self) -> mss_TimeseriesDTable:
        """Table 'mss_TimeseriesD' (Time Series data values)"""
        return self._tables['mss_TimeseriesD']
    
    @property
    def mss_Inflow(self) -> mss_InflowTable:
        """Table 'mss_Inflow' (Inflows)"""
        return self._tables['mss_Inflow']
    
    @property
    def mss_InflowD(self) -> mss_InflowDTable:
        """Table 'mss_InflowD' (Pollutants inflows)"""
        return self._tables['mss_InflowD']
    
    @property
    def mss_Pattern(self) -> mss_PatternTable:
        """Table 'mss_Pattern' (Time patterns)"""
        return self._tables['mss_Pattern']
    
    @property
    def mss_Coverage(self) -> mss_CoverageTable:
        """Table 'mss_Coverage' (Coverage)"""
        return self._tables['mss_Coverage']
    
    @property
    def mss_Evaporation(self) -> mss_EvaporationTable:
        """Table 'mss_Evaporation' (Evaporation)"""
        return self._tables['mss_Evaporation']
    
    @property
    def mss_Temperature(self) -> mss_TemperatureTable:
        """Table 'mss_Temperature' (Climatology)"""
        return self._tables['mss_Temperature']
    
    @property
    def mss_Adjustment(self) -> mss_AdjustmentTable:
        """Table 'mss_Adjustment' (Climatology adjustments)"""
        return self._tables['mss_Adjustment']
    
    @property
    def mss_Transect(self) -> mss_TransectTable:
        """Table 'mss_Transect' (Transects)"""
        return self._tables['mss_Transect']
    
    @property
    def mss_TransectD(self) -> mss_TransectDTable:
        """Table 'mss_TransectD' (Transects data)"""
        return self._tables['mss_TransectD']
    
    @property
    def mss_TransectCoord(self) -> mss_TransectCoordTable:
        """Table 'mss_TransectCoord' (Transects data)"""
        return self._tables['mss_TransectCoord']
    
    @property
    def mss_Aquifer(self) -> mss_AquiferTable:
        """Table 'mss_Aquifer' (Aquifers)"""
        return self._tables['mss_Aquifer']
    
    @property
    def mss_Hydrograph(self) -> mss_HydrographTable:
        """Table 'mss_Hydrograph' (RDII hydrographs)"""
        return self._tables['mss_Hydrograph']
    
    @property
    def mss_HydrographD(self) -> mss_HydrographDTable:
        """Table 'mss_HydrographD' (MssHydrographDTable)"""
        return self._tables['mss_HydrographD']
    
    @property
    def mss_RDII(self) -> mss_RDIITable:
        """Table 'mss_RDII' (RDII)"""
        return self._tables['mss_RDII']
    
    @property
    def mss_SnowPack(self) -> mss_SnowPackTable:
        """Table 'mss_SnowPack' (Snowpacks)"""
        return self._tables['mss_SnowPack']
    
    @property
    def mss_LIDControl(self) -> mss_LIDControlTable:
        """Table 'mss_LIDControl' (LID properties)"""
        return self._tables['mss_LIDControl']
    
    @property
    def mss_LIDControlD(self) -> mss_LIDControlDTable:
        """Table 'mss_LIDControlD' (LIDControlD)"""
        return self._tables['mss_LIDControlD']
    
    @property
    def mss_LIDusage(self) -> mss_LIDusageTable:
        """Table 'mss_LIDusage' (LID deployment)"""
        return self._tables['mss_LIDusage']
    
    @property
    def mss_DWF(self) -> mss_DWFTable:
        """Table 'mss_DWF' (Dry weather flow)"""
        return self._tables['mss_DWF']
    
    @property
    def mss_DWFD(self) -> mss_DWFDTable:
        """Table 'mss_DWFD' (Pollutant data)"""
        return self._tables['mss_DWFD']
    
    @property
    def mss_Raingauge(self) -> mss_RaingaugeTable:
        """Table 'mss_Raingauge' (Raingauge)"""
        return self._tables['mss_Raingauge']
    
    @property
    def mss_Groundwater(self) -> mss_GroundwaterTable:
        """Table 'mss_Groundwater' (Ground water)"""
        return self._tables['mss_Groundwater']
    
    @property
    def mss_Rule(self) -> mss_RuleTable:
        """Table 'mss_Rule' (Controls)"""
        return self._tables['mss_Rule']
    
    @property
    def mss_Pollutant(self) -> mss_PollutantTable:
        """Table 'mss_Pollutant' (Pollutants)"""
        return self._tables['mss_Pollutant']
    
    @property
    def mss_Landuse(self) -> mss_LanduseTable:
        """Table 'mss_Landuse' (Land uses)"""
        return self._tables['mss_Landuse']
    
    @property
    def mss_Washoff(self) -> mss_WashoffTable:
        """Table 'mss_Washoff' (Washoff)"""
        return self._tables['mss_Washoff']
    
    @property
    def mss_Buildup(self) -> mss_BuildupTable:
        """Table 'mss_Buildup' (Buildup)"""
        return self._tables['mss_Buildup']
    
    @property
    def mss_Loading(self) -> mss_LoadingTable:
        """Table 'mss_Loading' (Initial loading)"""
        return self._tables['mss_Loading']
    
    @property
    def mss_LocalTreatment(self) -> mss_LocalTreatmentTable:
        """Table 'mss_LocalTreatment' (Local treatment)"""
        return self._tables['mss_LocalTreatment']
    