from DHI.Amelia.Tools.ConnectionRepairEngine import ConnectionRepairEngine


class ConnectionRepairTool:
    """
    For collection module, this class is to repair station connections, catchment connections and load point connections.
    For water distribute module, this class is to repair station connections and demand allocation connections.
    For SWMM, this class is to repair station connections and catchment connections.
    """
    def __init__(self,
                 dataTables):
        self._dataTables = dataTables

    def run(self):
        tool = ConnectionRepairEngine(self._dataTables)
        tool.Run()
        tool.RuningProgress += self._on_tool_runing_progress

    def _on_tool_runing_progress(self, source, args):
        print(args.Msg)
