"""The Connection Repair Tool from MIKE+."""

from DHI.Amelia.Tools.ConnectionRepairEngine import ConnectionRepairEngine
from ..database import Database


class ConnectionRepairTool:
    """The Connection Repair Tool from MIKE+.

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
        database : Database or DataTables
            A Database object for the MIKE+ model.

        """
        if not database.is_open:
            database.open()
        self._dataTables = database._data_table_container

    def run(self):
        """Run the connection repair tool."""
        tool = ConnectionRepairEngine(self._dataTables)
        tool.Run()
        tool.RuningProgress += self._on_tool_runing_progress

    def _on_tool_runing_progress(self, source, args):
        print(args.Msg)
