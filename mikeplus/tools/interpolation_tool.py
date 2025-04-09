from DHI.Amelia.DomainServices.Interface.TransferEntity.InterpolationTool import (
    InterpolationToolParameters,
)
from DHI.Amelia.Tools.InterpolationEngine import InterpolationEngine


class InterpolationTool:
    """The Interpolation and Assignment tool helps assign values to any field in the MIKE+ database either by taking the attribute value directly from
    another fea­ture/attribute or by interpolating between any number of other features.

    Examples
    --------
    Interplate node diameter from connected links for the nodes which have NULL diameter.
    ```python
    >>> data_access = DataTableAccess(muppOrSqlite)
    >>> data_access.open_database()
    >>> tool = InterpolationTool(data_access.datatables)
    >>> tool.interpolate_from_nearest_feature("msm_Node", "Diameter", "msm_Link", "Diameter", Ture, False, None)
    >>> data_access.close_database()
    ```

    """

    def __init__(self, dataTables):
        self._dataTables = dataTables

    def interpolate_from_nearest_feature(
        self,
        target_Db_Name,
        target_attribute,
        source_layer_name,
        source_attribute,
        only_null_values=True,
        assign_val_as_missing=False,
        value_as_missing=None,
        search_radius=300.0,
    ):
        """Interpolate target attribute from nearest source in search radius.

        Parameters
        ----------
        target_Db_Name : string
            target table name, the table you want to interpolate
        target_attribute : string
            target attribute name, the field in the table, which you want to interpolate
        source_layer_name : string
            source_layer_name can be database table name, or a shape file path, the source is used to interpolate the target
        source_attribute : string
            source attribute name, field name of source layer
        only_null_values : bool, optional
            If true, only interpolate null value or defined as missing value in target attribute in target table. Otherwise, interpolate all. By default True
        assign_val_as_missing : bool, optional
            If true, assgined value as missing value. By default False
        value_as_missing : float, optional
            Specify the value as the missing value, by default None
        search_radius : float, optional
            the search radius to find the source, by default 300

        """
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

    def interpolate_from_DEM(
        self,
        target_Db_Name,
        target_attribute,
        raster_file,
        item_number,
        only_null_values=True,
        assign_val_as_missing=False,
        value_as_missing=None,
    ):
        """Interpolate target attribute from specified item number in raster layer.

        Parameters
        ----------
        target_Db_Name : string
            target table name, the table you want to interpolate
        target_attribute : string
            target attribute name, the field in the table, which you want to interpolate
        raster_file : string
            raster file path
        item_number : int
            the item number in raster file used to interpolate
        only_null_values : bool, optional
            If true, only interpolate null value or defined as missing value in target attribute in target table. Otherwise, interpolate all. By default True
        assign_val_as_missing : bool, optional
            If true, assgined value as missing value. By default False
        value_as_missing : float, optional
            Specify the value as the missing value, by default None

        """
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

    def interpolation_IDW(
        self,
        target_Db_name,
        target_attribute,
        source_layer_name,
        source_attribute,
        only_null_values=True,
        assign_val_as_missing=False,
        value_as_missing=None,
        max_IDW_points=12,
        search_radius=300.0,
    ):
        """Interpolate target attribute from the specified max number of sources in search radius.

        Parameters
        ----------
        target_Db_name : string
            target table name, the table you want to interpolate
        target_attribute : string
            target attribute name, the field in the table, which you want to interpolate
        source_layer_name : string
            source_layer_name can be database table name, or a shape file path, the source is used to interpolate the target
        source_attribute : string
            source attribute name, field name of source layer
        only_null_values : bool, optional
            If true, only interpolate null value or defined as missing value in target attribute in target table. Otherwise, interpolate all. By default True
        assign_val_as_missing : bool, optional
            If true, assgined value as missing value. By default False
        value_as_missing : float, optional
            Specify the value as the missing value, by default None
        max_IDW_points : int, optional
            the max source number used to interpolate, by default 12
        search_radius : float, optional
            the search radius to find the source, by default 300.0

        """
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

    def direct_assign_value(
        self,
        target_Db_name,
        target_attribute,
        fixed_value,
        only_null_values=True,
        assign_val_as_missing=False,
        value_as_missing=None,
    ):
        """Set the target attribute as the fixed value.

        Parameters
        ----------
        target_Db_name : string
            target table name, the table you want to interpolate
        target_attribute : string
            target attribute name, the field in the table, which you want to interpolate
        fixed_value : float
            The fixed value is used to set the missing value.
        only_null_values : bool, optional
            If true, only interpolate null value or defined as missing value in target attribute in target table. Otherwise, interpolate all. By default True
        assign_val_as_missing : bool, optional
            If true, assgined value as missing value. By default False
        value_as_missing : float, optional
            Specify the value as the missing value, by default None

        """
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

    """
    
    """

    def interpolate_from_neighobour(
        self,
        target_Db_name,
        target_attribute,
        source_layer_name,
        source_attribute,
        only_null_values=True,
        assign_val_as_missing=False,
        value_as_missing=None,
        assign_option=0,
        alongPath=False,
        max_neighbours=3,
    ):
        """Interpolate target attribute from the source attribute along the network.

        Parameters
        ----------
        target_Db_name : string
            target table name, the table you want to interpolate
        target_attribute : string
            target attribute name, the field in the table, which you want to interpolate
        source_layer_name : string
            source table name, the table used to interpolate
        source_attribute : string
            source attribute name, the field in source table used to interpolate
        only_null_values : bool, optional
            If true, only interpolate null value or defined as missing value in target attribute in target table. Otherwise, interpolate all. By default True
        assign_val_as_missing : bool, optional
            If true, assgined value as missing value. By default False
        value_as_missing : float, optional
            Specify the value as the missing value, by default None
        assign_option : int, optional
            assign option, by default 0
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
        alongPath : bool, optional
            If true, interpolate from neighbour. Otherwise, interpolate from network. By default False
        max_neighbours : int, optional
            the max neighbours with missing value along the network, by default 3

        """
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
