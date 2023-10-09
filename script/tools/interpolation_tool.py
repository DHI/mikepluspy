from DHI.Amelia.DomainServices.Interface.TransferEntity.InterpolationTool import InterpolationToolParameters
from DHI.Amelia.Tools.InterpolationEngine import InterpolationEngine


class InterpolationTool:
    def __init__(self,
                 dataTables):
        self._dataTables = dataTables

    """
    sourceLayerName can be database table name, or a shape file path
    """
    def interpolate_from_nearest_feature(self,
                                         target_Db_Name,
                                         target_attribute,
                                         source_layer_name,
                                         source_attribute,
                                         only_null_values=True,
                                         assign_val_as_missing=False,
                                         value_as_missing=None,
                                         search_radius=300):
        param = InterpolationToolParameters()
        param.assigmentMethod = 1
        param.TargetTable = target_Db_Name
        param.TargetAttribute = target_attribute
        param.SourceTable = source_layer_name
        param.sFeatureFile = source_layer_name
        param.SourceAttribute = source_attribute
        param.bOverallMissingValues = only_null_values
        param.bOverallAssignSelected = False
        param.bOverallAssignInside = False
        param.dSearhRadius = search_radius
        param.bOverallConsideredMissing = assign_val_as_missing
        param.sMissingVaue = value_as_missing
        tool = InterpolationEngine(self._dataTables)
        tool.RuningProgress += self._on_tool_runing_progress
        msgs = None
        tool.Run(param, False, msgs)

    def interpolate_from_DEM(self,
                             target_Db_Name,
                             target_attribute,
                             raster_file,
                             item_number,
                             only_null_values=True,
                             assign_val_as_missing=False,
                             value_as_missing=None):
        param = InterpolationToolParameters()
        param.assigmentMethod = 0
        param.TargetTable = target_Db_Name
        param.TargetAttribute = target_attribute
        param.sRasterFile = raster_file
        param.iItemnumber = item_number
        param.bOverallMissingValues = only_null_values
        param.bOverallAssignSelected = False
        param.bOverallAssignInside = False
        param.bOverallConsideredMissing = assign_val_as_missing
        param.sMissingVaue = value_as_missing
        tool = InterpolationEngine(self._dataTables)
        tool.RuningProgress += self._on_tool_runing_progress
        msgs = None
        tool.Run(param, False, msgs)

    def interpolation_IDW(self,
                          target_Db_name,
                          target_attribute,
                          source_layer_name,
                          source_attribute,
                          only_null_values=True,
                          assign_val_as_missing=False,
                          value_as_missing=None,
                          max_IDW_points=12,
                          search_radius=300):
        param = InterpolationToolParameters()
        param.assigmentMethod = 2
        param.TargetTable = target_Db_name
        param.TargetAttribute = target_attribute
        param.SourceTable = source_layer_name
        param.sFeatureFile = source_layer_name
        param.SourceAttribute = source_attribute
        param.bOverallMissingValues = only_null_values
        param.bOverallAssignSelected = False
        param.bOverallAssignInside = False
        param.iMaxFeatureSkip = max_IDW_points
        param.dSearhRadius = search_radius
        param.bOverallConsideredMissing = assign_val_as_missing
        param.sMissingVaue = value_as_missing
        tool = InterpolationEngine(self._dataTables)
        tool.RuningProgress += self._on_tool_runing_progress
        msgs = None
        tool.Run(param, False, msgs)

    def direct_assign_value(self,
                            target_Db_name,
                            target_attribute,
                            fixed_value,
                            only_null_values=True,
                            assign_val_as_missing=False,
                            value_as_missing=None):
        param = InterpolationToolParameters()
        param.assigmentMethod = 5
        param.TargetTable = target_Db_name
        param.TargetAttribute = target_attribute
        param.dFixedValue = fixed_value
        param.bOverallMissingValues = only_null_values
        param.bOverallAssignSelected = False
        param.bOverallAssignInside = False
        param.bOverallConsideredMissing = assign_val_as_missing
        param.sMissingVaue = value_as_missing
        tool = InterpolationEngine(self._dataTables)
        tool.RuningProgress += self._on_tool_runing_progress
        msgs = None
        tool.Run(param, False, msgs)

    '''
    AssignOption
    {
        ClosestNode=0,
        UpstreamElement=1,
        DownstreamElement=2,
        UpstreamMaxValue=3,
        UpstreamMinValue=4,
        DownlstreamMaxValue=5,
        DownstreamMinValue=6,
        MaxValueNeighbours=7,
        MinValueNeighbours=8
    }
    '''
    def interpolate_from_neighobour(self,
                                    target_Db_name,
                                    target_attribute,
                                    source_layer_name,
                                    source_attribute,
                                    only_null_values=True,
                                    assign_val_as_missing=False,
                                    value_as_missing=None,
                                    assign_option=0,
                                    alongPath=False,
                                    max_neighbours=3):
        param = InterpolationToolParameters()
        if self.alongPath is True:
            param.assigmentMethod = 4
        else:
            param.assigmentMethod = 3
        param.TargetTable = target_Db_name
        param.TargetAttribute = target_attribute
        param.SourceTable = source_layer_name
        param.SourceAttribute = source_attribute
        param.bOverallMissingValues = only_null_values
        param.bOverallAssignSelected = False
        param.bOverallAssignInside = False
        param.bOverallConsideredMissing = assign_val_as_missing
        param.sMissingVaue = value_as_missing
        param.assigmentOption = assign_option
        param.nNeighbours = max_neighbours
        tool = InterpolationEngine(self._dataTables)
        tool.RuningProgress += self._on_tool_runing_progress
        msgs = None
        tool.Run(param, False, msgs)

    def _on_tool_runing_progress(self, source, args):
        print(args.Msg)
