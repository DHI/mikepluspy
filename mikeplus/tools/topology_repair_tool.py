"""The Topology Repair Tool from MIKE+."""

from DHI.Amelia.DomainServices.Interface.TransferEntity.TopologyRepairTool import (
    TopologyRepairParam,
)
from DHI.Amelia.GlobalUtility.DataType import MUModelOption
from DHI.Amelia.Tools.TopologyRepairTool import CSTopologyRepairTool
from DHI.Amelia.Tools.TopologyRepairTool import WDTopologyRepairTool
from ..database import Database
from System.Threading import CancellationTokenSource


class TopoRepairTool:
    """Topology repair tool for MIKE+.

    TopoRepairTool provides methods to repair the topology of a MIKE+ model.

    Examples
    --------
    Delete unlinked nodes and links, also delete overlapped nodes for the whole network.
    ```python
    >>> from mikeplus import Database
    >>> db = Database("path/to/model.sqlite")
    >>> repair_tool = TopoRepairTool(db)
    >>> repair_tool.run(True, True, False, False, False, False, False)
    >>> db.close()
    ```

    """

    def __init__(self, database):
        """Initialize the TopoRepairTool with the given Database.

        Parameters
        ----------
        database : Database or DataTables
            A Database object for the MIKE+ model, or for backward compatibility,
            a DataTables object from DataTableAccess.

        """
        self._dataTables = self._get_data_tables(database)

    def _get_data_tables(self, database):
        """Get proper DataTableContainer, working with deprecated DataTableAccess workflow."""
        if isinstance(database, Database):
            if not database.is_open:
                database.open()
            return database._data_table_container

        # if not Database object, assume user passed DataTableAccess.datatables per previous workflow
        return database

    def run(
        self,
        delete_unLink_node_Link=True,
        dissolve_overlap_node=True,
        correct_link_connection=True,
        search_junction_connection=True,
        create_junction_connection=True,
        split_link_on_tjunction=True,
        add_missing_zones=True,
        snap_distance=0.1,
    ):
        """Offers a way to detect and repair topology or network geometry issues in the model.

        Parameters
        ----------
        delete_unLink_node_Link : bool, optional
            If true, isolated nodes (other than tanks) and links / pipes, disconnected from the rest of the network, will be removed. By default True
        dissolve_overlap_node : bool, optional
            If true, extra nodes within the specified search radius will be removed. By default True
        correct_link_connection : bool, optional
            When a link's end is not con­nected to a node, if this operation is true, it will connect it either to the closest exist­ing node within the specified search radius, or to a new node. By default True
        search_junction_connection : bool, optional
            If true, it will connect to the closest exist­ing node within the specified search radius. By default True
        create_junction_connection : bool, optional
            If true, it will connect to a new node. By default True
        split_link_on_tjunction : bool, optional
            If true, when the end of a link overlaps a second link, this second link is split at the intersection and a node is inserted, and all the three resulting pipes are connected to this new node. By default True
        add_missing_zones : bool, optional
            If true, refresh the list of network zones. By default True
        snap_distance : float, optional
            The distance used in dissolve the overlapped nodes, in correct link connection, and in split link on T junction, by default 0.1.

        """
        cancel_source = CancellationTokenSource()
        topology_param = TopologyRepairParam()
        topology_param.DeleteUnLinkNodeAndLink = delete_unLink_node_Link
        topology_param.DissolveOverlapNode = dissolve_overlap_node
        topology_param.CorrectLinkConnection = correct_link_connection
        topology_param.SearchJunction4Connection = search_junction_connection
        topology_param.CreateJunction4Connection = create_junction_connection
        topology_param.SplitLinkOnTJunction = split_link_on_tjunction
        topology_param.AddMissingZones = add_missing_zones
        topology_param.OverlapNodeSearchRadius = snap_distance
        topology_param.JunctionSearchRadius4Connection = snap_distance
        topology_param.TJunctionSplitSearchRadius = snap_distance
        if self._dataTables.ActiveModel == MUModelOption.CS_MIKE1D:
            tool = CSTopologyRepairTool(self._dataTables)
            tool.RuningProgress += self._on_tool_runing_progress
            tool.Run(topology_param, cancel_source.Token, False)
        elif self._dataTables.ActiveModel == MUModelOption.WD_EPANET:
            tool = WDTopologyRepairTool(self._dataTables)
            tool.RuningProgress += self._on_tool_runing_progress
            tool.Run(topology_param, cancel_source.Token, False)

    def _on_tool_runing_progress(self, source, args):
        print(args.Msg)
