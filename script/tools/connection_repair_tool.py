from DHI.Amelia.Tools.ConnectionRepairEngine import ConnectionRepairEngine

class ConnectionRepairTool:
	def __init__(self,
				 dataTables):
		self._dataTables = dataTables
	
	def run(self):
		tool = ConnectionRepairEngine(self._dataTables)
		tool.Run()
		tool.RuningProgress += self._on_tool_runing_progress
		
	def _on_tool_runing_progress(self, source, args):
		print(args.Msg)