"""Auto-generated table classes for MIKE+ database.

DO NOT MANUALLY MODIFY THIS PACKAGE! Use AutoTableClassGenerator to regenerate.
"""
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

from .table_collection import TableCollection

__all__ = [
    "TableCollection",
    "m_ConfigurationTable",
    "m_StatusTable",
    "m_DefaultValueTable",
    "m_UserDefinedColumnTable",
    "m_MediaTable",
    "m_StatusCodeTable",
    "m_SelectionTable",
    "m_BookmarkTable",
    "m_MeasurementTable",
    "m_StationTable",
    "m_StationConTable",
    "m_ModelSettingTable",
    "m_GlobalParameterTable",
    "m_CustomUnitTable",
    "m_CustomConfigTable",
    "m_ChartBookmarkTable",
    "ms_TabTable",
    "ms_TabDTable",
    "ms_2DTabTable",
    "ms_2DTabD_TVCtrlRuleTable",
    "ms_2DTabD_GenericCtrlRuleTable",
    "ms_2DTabD_Bridge_USBPR_EccentricityTable",
    "ms_2DTabD_Bridge_FHWA_WSPRO_spur_dykeIIITable",
    "ms_2DTabD_Bridge_Hydraulic_Research_archTable",
    "ms_2DTabD_Bridge_Biery_and_Delleur_archTable",
    "ms_2DTabD_Bridge_USBPR_velocity_distributionTable",
    "ms_2DTabD_Bridge_FHWA_WSPRO_coef_typeIITable",
    "ms_2DTabD_Bridge_FHWA_WSPRO_coef_typeIIITable",
    "ms_2DTabD_Bridge_FHWA_WSPRO_coef_typeIVTable",
    "ms_2DTabD_Bridge_FHWA_WSPRO_depthTable",
    "ms_2DTabD_Bridge_FHWA_WSPRO_abutmentTable",
    "ms_2DTabD_Bridge_FHWA_WSPRO_PilesTable",
    "ms_2DTabD_Tabulated_QHTable",
    "ms_2DTabD_Tabulated_HQ_UPTable",
    "ms_2DTabD_Tabulated_HQ_DOWNTable",
    "ms_CRSTable",
    "ms_CRSDTable",
    "ms_ProcessedCRSDTable",
    "ms_DPProfileTable",
    "ms_DPProfileDTable",
    "ms_DPPatternTable",
    "ms_DPPatternDTable",
    "ms_DPSpecDayTable",
    "ms_DPScheduleTable",
    "ms_MaterialTable",
    "ms_SimpSettingTable",
    "ms_SimpMappingTable",
    "msm_NodeTable",
    "msm_LinkTable",
    "mrm_BranchTable",
    "mrm_UserDefinedChainageTable",
    "mrm_RiverRoutingMethodTable",
    "mrm_BranchRoughnessLocalTable",
    "mrm_ZoneSeparatorLocalTable",
    "mrm_RoughnessFactorTable",
    "mrm_BranchConnTable",
    "msm_CatchmentTable",
    "msm_CatchConTable",
    "msm_WeirTable",
    "msm_ValveTable",
    "msm_CurbInletTable",
    "msm_CulvertTable",
    "msm_CulvertGeomTable",
    "msm_CulvertHDParamTable",
    "msm_CulvertQHFlowTable",
    "msm_CulvertOrificeFlowCoeffTable",
    "mrm_WeirTable",
    "mrm_WeirGeomTable",
    "mrm_WeirQHRelationTable",
    "mrm_DirectDischargeTable",
    "mrm_GateTable",
    "mrm_PumpTable",
    "mrm_BridgeTable",
    "mrm_BridgeOpeningTable",
    "mrm_BridgeCrsTable",
    "mrm_DambreakTable",
    "mrm_EnergyLossTable",
    "mrm_TabulatedTable",
    "mrm_StorageTable",
    "msm_PumpTable",
    "msm_OrificeTable",
    "msm_BBoundaryTable",
    "msm_BndGridRainWeightsTable",
    "msm_WQBoundaryPropertiesTable",
    "msm_LossParTable",
    "msm_HParATable",
    "msm_HParBTable",
    "msm_HParCTable",
    "msm_HParRDIITable",
    "msm_HParAutoCaliRDIITable",
    "msm_HParRdiiElevZonesTable",
    "msm_HParSeasonalVariationTable",
    "msm_RTCTable",
    "msm_RTCSensorTable",
    "msm_RTCRuleTable",
    "msm_RTCActionTable",
    "msm_RTCPIDTable",
    "msm_LoadPointTable",
    "msm_LoadPointConnectionTable",
    "msm_ProjectTable",
    "msm_ProjectOutputTable",
    "msm_RSTable",
    "msm_RSSTable",
    "msm_RSSItemTable",
    "msm_RSSGeomTable",
    "msm_RSSFormatGeometryTable",
    "msm_RSSDemTable",
    "msm_ADDispersionLocalTable",
    "msm_ADDispersionTable",
    "msm_ADComponentIniTable",
    "msm_ADComponentTable",
    "msm_ADDecayTable",
    "msm_ADInitialConditionTable",
    "msm_ADInitialConditionDefaultTable",
    "msm_ADInitialConditionLocalTable",
    "msm_ADInitialConditionLocalValueTable",
    "msm_ADInitialConditionHotstartFileTable",
    "msm_LTSRunMTable",
    "msm_LTSRunSTable",
    "msm_LTSJobListCriteriaTable",
    "msm_LTSDwfTsTable",
    "msm_LTSInitTable",
    "msm_LTSInitoTable",
    "msm_LTSResultTable",
    "msm_LTSResultLocalTable",
    "msm_LIDusageTable",
    "msm_LIDcontrolTable",
    "msm_LIDRemovalTable",
    "msm_ResultSelectionQuantityTable",
    "msm_ECOLABCoeffTable",
    "msm_ECOLABCoeffLocalTable",
    "msm_ECOLABForcingTable",
    "msm_ECOLABComponentTable",
    "msm_ECOLABTemplateTable",
    "msm_ECOLABOutputTable",
    "msm_SWQPollutantTable",
    "msm_SWQGlobalDataTable",
    "msm_SWQAttachedPollutantTable",
    "msm_HtmlSummaryTable",
    "msm_OnGradeTable",
    "msm_OnGradeDTable",
    "msm_STTable",
    "msm_STFractionTable",
    "mrm_STAdvFractionTable",
    "mrm_STAdvFracGrainLocalTable",
    "mrm_STAdvFracSusLocalTable",
    "msm_STInitDepthLocalTable",
    "msm_STInitDepthFractDefaultTable",
    "msm_STInitDepthFractLocalTable",
    "msm_STPipesRoughnessLocalTable",
    "msm_STRemovalBasinTable",
    "msm_STRemovalWeirTable",
    "mrm_STLocalBedParThickTable",
    "mrm_STLocalBedParMorphTable",
    "mrm_STInitConcentratDefaultTable",
    "mrm_STInitConcentratLocalTable",
    "msm_HDInitialConditionTable",
    "msm_HDInitialConditionLocalTable",
    "msm_HDInitialConditionHotstartFileTable",
    "msm_AlarmLevelTable",
    "msm_AlarmLevelDTable",
    "msm_PumpESETable",
    "msm_PumpESEDTable",
    "mrm_DAGeneralParaTable",
    "mrm_DAUpdateParaTable",
    "mrm_DAStandardDeviationTable",
    "mrm_DAErrorForecastEquationsTable",
    "mrm_DAErrorForecastParaTable",
    "mrm_DAPerturbationsParaTable",
    "mrm_WindScaleFactorLocalTable",
    "mrm_LeakageCoefficientsTable",
    "msm_HDAddPercentTable",
    "msm_RRAddPercentTable",
    "mrm_SHECouplingsTable",
    "mrm_STNonScrLocalBedLevelTable",
    "mrm_STPassiveLinkTable",
    "msm_LandUseTable",
    "msm_CatchLandUseTable",
    "mw_PPatternTable",
    "mw_PPatternDTable",
    "mw_CurveTable",
    "mw_CurveDTable",
    "mw_JunctionTable",
    "mw_TankTable",
    "mw_AirChamberTable",
    "mw_MDemandTable",
    "mw_PipeTable",
    "mw_PumpTable",
    "mw_ValveTable",
    "mw_ControlTable",
    "mw_DemAllocTable",
    "mw_DemAllocConnTable",
    "mw_PumpStationTable",
    "mw_PumpStationConnTable",
    "mw_SpecDayTable",
    "mw_ZoneDefTable",
    "mw_ZoneWBTable",
    "mw_DemStatTable",
    "mw_DemStatConfigTable",
    "mw_ProjectTable",
    "mw_SourceTable",
    "mw_TraceNodeTable",
    "mw_TurbineTable",
    "mw_FrictionTable",
    "mw_LossTable",
    "mw_RTCTable",
    "mw_EnergyTable",
    "mw_RuleTable",
    "mw_ReliabilityTable",
    "mw_ReliabilityLocalTable",
    "mw_FireFlowTable",
    "mw_FlushingTable",
    "mw_FlushingOutletTable",
    "mw_ShutdownPlanningTable",
    "mw_ShutdownValveTable",
    "mw_PipeRelTable",
    "mw_WH_BoundaryTable",
    "mw_WDOSettingsTable",
    "mw_WDOSensorsTable",
    "mw_OptimizationTable",
    "mw_OptimizationControlTable",
    "mw_OptimizationTargetTable",
    "mw_OptimizationTargetWBTable",
    "mw_WDOControlsTable",
    "mw_WDODemandZonesTable",
    "mw_WDODemandPredictionsTable",
    "mw_WDOComparisonsTable",
    "mw_EPAMSXTable",
    "mw_AutocalibrationTable",
    "mw_AutocaliPipesFrictTable",
    "mw_AutocaliNodeDemandsTable",
    "mw_AutocaliClosedLinksTable",
    "mw_AutocaliLeaksTable",
    "mw_AutocaliTargetsTable",
    "mwRes_ValveCriticalityTable",
    "mwRes_Sustainability_NodeTable",
    "mwRes_Sustainability_LinkTable",
    "m21_pfsSectionTable",
    "m21_pfsKeywordTable",
    "m21_pfsParamTable",
    "m2d_GlobalSettingTable",
    "m2d_SurfaceRoughnessAreaTable",
    "m2d_SurfaceRoughnessValueTable",
    "m2d_EddyViscosityAreaTable",
    "m2d_InfiltrationTable",
    "m2d_InfiltrationLandCoverTable",
    "m2d_InitialConditionAreaTable",
    "m2d_StructureDikeTable",
    "m2d_StructureWeirTable",
    "m2d_StructureWeirDTable",
    "m2d_StructureCulvertTable",
    "m2d_StructureCulvertDTable",
    "m2d_CouplingTable",
    "m2d_CouplingConnTable",
    "m2d_CouplingEngineConnTable",
    "m2d_CouplingEngineFaceTable",
    "m2d_MeshArcTable",
    "m2d_MeshLocalAreaTable",
    "m2d_GridDefinitionTable",
    "m2d_GridInactiveAreaTable",
    "m2d_BoundaryTable",
    "m2d_BndQHRelationTable",
    "m2d_BndDistributedSourceTable",
    "m2d_ADInitalConditionTable",
    "m2d_ADInitalConditionAreaTable",
    "m2d_ADInitalConditionDTable",
    "m2d_ADPrecipitationTable",
    "m2d_ADPrecipitationAreaTable",
    "m2d_ADPrecipitationDTable",
    "m2d_ADDecayTable",
    "m2d_ADInfiltrationTable",
    "m2d_ADInfiltrationAreaTable",
    "m2d_ADInfiltrationDTable",
    "m2d_ADEvaporationTable",
    "m2d_ADEvaporationAreaTable",
    "m2d_ADEvaporationDTable",
    "m2d_ADDispersionTable",
    "m2d_ADDispersionDTable",
    "m2d_ADDispersionAreaTable",
    "m2d_WQBoundaryTable",
    "m2d_InfBuildingTable",
    "m2d_InfRoadTable",
    "mss_NodeTable",
    "mss_LinkTable",
    "mss_CatchConTable",
    "mss_OrificeTable",
    "mss_PumpTable",
    "mss_OutletTable",
    "mss_WeirTable",
    "mss_TabTable",
    "mss_TabDTable",
    "mss_ProjectTable",
    "mss_TimeseriesTable",
    "mss_TimeseriesDTable",
    "mss_InflowTable",
    "mss_InflowDTable",
    "mss_PatternTable",
    "mss_CoverageTable",
    "mss_EvaporationTable",
    "mss_TemperatureTable",
    "mss_AdjustmentTable",
    "mss_TransectTable",
    "mss_TransectDTable",
    "mss_TransectCoordTable",
    "mss_AquiferTable",
    "mss_HydrographTable",
    "mss_HydrographDTable",
    "mss_RDIITable",
    "mss_SnowPackTable",
    "mss_LIDControlTable",
    "mss_LIDControlDTable",
    "mss_LIDusageTable",
    "mss_DWFTable",
    "mss_DWFDTable",
    "mss_RaingaugeTable",
    "mss_GroundwaterTable",
    "mss_RuleTable",
    "mss_PollutantTable",
    "mss_LanduseTable",
    "mss_WashoffTable",
    "mss_BuildupTable",
    "mss_LoadingTable",
    "mss_LocalTreatmentTable",
]