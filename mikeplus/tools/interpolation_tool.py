"""The Interpolation and Assignment tool from MIKE+."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from DHI.Amelia.DomainServices.Interface.TransferEntity.InterpolationTool import (
    InterpolationToolParameters,
)
from DHI.Amelia.Tools.InterpolationEngine import InterpolationEngine
from System import Convert

if TYPE_CHECKING:
    from ..database import Database


def _missing_value_text(value: float | None) -> str | None:
    # MIKE+ takes the missing value as text. Convert formats it in the current culture.
    return None if value is None else Convert.ToString(float(value))


class InterpolationTool:
    """The Interpolation and Assignment tool from MIKE+.

    Examples
    --------
    Interpolate node diameter from connected links for the nodes which have NULL diameter.

    ```python
    >>> from mikeplus import Database
    >>> db = Database("path/to/model.sqlite")
    >>> tool = InterpolationTool(db)
    >>> tool.interpolate_from_nearest_feature("msm_Node", "Diameter", "msm_Link", "Diameter", True, False, None)
    >>> db.close()
    ```

    """

    def __init__(self, database: Database) -> None:
        """Initialize the InterpolationTool with the given Database.

        Parameters
        ----------
        database : Database or DataTables
            A Database object for the MIKE+ model.

        """
        if not database.is_open:
            database.open()
        self._dataTables = database._data_table_container

    def interpolate_from_nearest_feature(
        self,
        target_Db_Name: str,
        target_attribute: str,
        source_layer_name: str,
        source_attribute: str,
        only_null_values: bool = True,
        assign_val_as_missing: bool = False,
        value_as_missing: float | None = None,
        search_radius: float = 300.0,
    ) -> None:
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
            If true, treat `value_as_missing` as a missing value. By default False
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
        param.sMissingVaue = _missing_value_text(value_as_missing)
        tool = InterpolationEngine(self._dataTables)
        tool.RuningProgress += self._on_tool_runing_progress
        msgs = None
        tool.Run(param, False, msgs)

    def interpolate_from_DEM(
        self,
        target_Db_Name: str,
        target_attribute: str,
        raster_file: str,
        item_number: int,
        only_null_values: bool = True,
        assign_val_as_missing: bool = False,
        value_as_missing: float | None = None,
    ) -> None:
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
            If true, treat `value_as_missing` as a missing value. By default False
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
        param.sMissingVaue = _missing_value_text(value_as_missing)
        tool = InterpolationEngine(self._dataTables)
        tool.RuningProgress += self._on_tool_runing_progress
        msgs = None
        tool.Run(param, False, msgs)

    def interpolation_IDW(
        self,
        target_Db_name: str,
        target_attribute: str,
        source_layer_name: str,
        source_attribute: str,
        only_null_values: bool = True,
        assign_val_as_missing: bool = False,
        value_as_missing: float | None = None,
        max_IDW_points: int = 12,
        search_radius: float = 300.0,
    ) -> None:
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
            If true, treat `value_as_missing` as a missing value. By default False
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
        param.sMissingVaue = _missing_value_text(value_as_missing)
        tool = InterpolationEngine(self._dataTables)
        tool.RuningProgress += self._on_tool_runing_progress
        msgs = None
        tool.Run(param, False, msgs)

    def direct_assign_value(
        self,
        target_Db_name: str,
        target_attribute: str,
        fixed_value: float,
        only_null_values: bool = True,
        assign_val_as_missing: bool = False,
        value_as_missing: float | None = None,
    ) -> None:
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
            If true, treat `value_as_missing` as a missing value. By default False
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
        param.sMissingVaue = _missing_value_text(value_as_missing)
        tool = InterpolationEngine(self._dataTables)
        tool.RuningProgress += self._on_tool_runing_progress
        msgs = None
        tool.Run(param, False, msgs)

    """
    
    """

    def interpolate_from_neighobour(
        self,
        target_Db_name: str,
        target_attribute: str,
        source_layer_name: str,
        source_attribute: str,
        only_null_values: bool = True,
        assign_val_as_missing: bool = False,
        value_as_missing: float | None = None,
        assign_option: int = 0,
        alongPath: bool = False,
        max_neighbours: int = 3,
    ) -> None:
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
            If true, treat `value_as_missing` as a missing value. By default False
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
        if alongPath:
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
        param.sMissingVaue = _missing_value_text(value_as_missing)
        param.assigmentOption = assign_option
        param.nNeighbours = max_neighbours
        tool = InterpolationEngine(self._dataTables)
        tool.RuningProgress += self._on_tool_runing_progress
        msgs = None
        tool.Run(param, False, msgs)

    def _on_tool_runing_progress(self, source: Any, args: Any) -> None:
        print(args.Msg)
