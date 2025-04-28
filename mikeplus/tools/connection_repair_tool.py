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

    def run(self):
        """Run the connection repair tool."""
        tool = ConnectionRepairEngine(self._dataTables)
        tool.Run()
        tool.RuningProgress += self._on_tool_runing_progress

    def _on_tool_runing_progress(self, source, args):
        print(args.Msg)
