"""The Connection Repair Tool from MIKE+."""

from DHI.Amelia.Tools.ConnectionRepairEngine import ConnectionRepairEngine


class ConnectionRepairTool:
    """The Connection Repair Tool from MIKE+.

    Rebuilds connection tables, such as station connections (`m_StationCon`) and
    load point connections (`msm_LoadPointConnection`).

    Examples
    --------
    >>> from mikeplus import Database
    >>> db = Database("path/to/model.sqlite")
    >>> conn_repair = ConnectionRepairTool(db)
    >>> conn_repair.run()
    >>> db.close()

    """

    def __init__(self, database):
        """Initialize the ConnectionRepairTool with the given Database.

        Parameters
        ----------
        database : Database
            A Database object for the MIKE+ model.

        """
        if not database.is_open:
            database.open()
        self._dataTables = database._data_table_container

    def run(self):
        """Run the connection repair tool."""
        tool = ConnectionRepairEngine(self._dataTables)
        tool.RuningProgress += self._on_tool_runing_progress
        tool.Run()

    def _on_tool_runing_progress(self, source, args):
        print(args.Msg)
