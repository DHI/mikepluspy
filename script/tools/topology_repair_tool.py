import os.path
from DHI.Amelia.DomainServices.Interface.TransferEntity.TopologyRepairTool import TopologyRepairParam
from DHI.Amelia.GlobalUtility.DataType import MUModelOption
from DHI.Amelia.Tools.TopologyRepairTool import CSTopologyRepairTool
from DHI.Amelia.Tools.TopologyRepairTool import WDTopologyRepairTool
from System.Threading import CancellationTokenSource

class TopoRepairTool:
	def __init__(self,
				 dataTables):
		self._dataTables = dataTables
	
	def run(self,
			 delete_unLink_node_Link=True,
			 dissolve_overlap_node=True,
			 correct_link_connection=True,
			 search_junction_connection=True,
			 create_junction_connection=True,
			 split_link_on_tjunction=True,
			 add_missing_zones=True,
			 snap_distance=0.1):
		cancel_source = CancellationTokenSource();
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