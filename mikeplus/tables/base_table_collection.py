"""
Base table collection for MIKE+ database tables.
"""

from mikeplus.tables.base_table import BaseTable


class BaseTableCollection:
    """A dict-like collection of tables in a model database.

    This class provides a base implementation for table collections in a model database.
    """

    def __init__(self, data_table_container):
        """Initialize a new BaseTableCollection.

        Args:
            data_table_container: The underlying data table container
        """
        self._data_table_container = data_table_container
        self._tables = self._init_tables()

    def _init_tables(self) -> dict[str, BaseTable]:
        """Initialize the tables dictionary."""
        return {}

    def keys(self):
        """Get a list of all table names.

        Returns:
            List of table names
        """
        return self._tables.keys()

    def values(self):
        """Get a list of all table objects.

        Returns:
            List of table objects
        """
        return self._tables.values()

    def items(self):
        """Get a list of (name, table) pairs.

        Returns:
            List of (name, table) tuples
        """
        return self._tables.items()

    def __getitem__(self, table_name: str) -> BaseTable:
        """Get a table by name.

        Args:
            table_name: Name of the table to get

        Returns:
            The requested table
        """
        return self._tables[table_name]

    def __contains__(self, table_name: str) -> bool:
        """Check if a table exists.

        Args:
            table_name: Name of the table to check

        Returns:
            True if the table exists, False otherwise
        """
        return table_name in self._tables

    def __iter__(self):
        """Get an iterator over table names.

        Returns:
            Iterator over table names
        """
        return iter(self._tables)
