"""The Connection Repair Tool from MIKE+."""
from DHI.Amelia.Tools.ConnectionRepairEngine import ConnectionRepairEngine


class ConnectionRepairTool:
    """The Connection Repair Tool from MIKE+.

    Examples
    --------
    >>> data_access = DataTableAccess(muppOrSqlite)
    >>> data_access.open_database()
    >>> conn_repair = ConnectionRepairTool(data_access.datatables)
    >>> conn_repair.run()
    >>> data_access.close_database()

    """

    def __init__(self, dataTables):
        """Initialize the ConnectionRepairTool with the given DataTables.
        
        Parameters
        ----------
        dataTables : DataTableContainer
            The DataTables to be used by the ConnectionRepairTool.

        """
        self._dataTables = dataTables

    def run(self):
        """Run the connection repair tool."""
        tool = ConnectionRepairEngine(self._dataTables)
        tool.Run()
        tool.RuningProgress += self._on_tool_runing_progress

    def _on_tool_runing_progress(self, source, args):
        print(args.Msg)
