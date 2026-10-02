"""Base table collection for MIKE+ database tables."""

from collections.abc import ItemsView, KeysView, ValuesView

from DHI.Amelia.DataModule.Services.DataTables import DataTableContainer

from mikeplus.tables.base_table import BaseTable


class BaseTableCollection:
    """A dict-like collection of tables in a model database.

    This class provides a base implementation for table collections in a model database.
    """

    def __init__(
        self, data_table_container: DataTableContainer
    ):  # api: allow-leaked-type
        """Initialize a new BaseTableCollection.

        Parameters
        ----------
        data_table_container : DataTableContainer
            The underlying data table container

        """
        self._data_table_container = data_table_container
        self._tables = self._init_tables()
        self._table_names = {name.casefold(): name for name in self._tables}

    def __repr__(self) -> str:
        """Get string representation.

        Returns
        -------
        str
            The class name and number of tables.

        """
        return f"{self.__class__.__name__}<{len(self._tables)} tables>"

    def _init_tables(self) -> dict[str, BaseTable]:
        """Initialize the tables dictionary.

        Returns
        -------
        dict[str, BaseTable]
            Tables keyed by name. Empty in the base class.

        """
        return {}

    def keys(self) -> KeysView[str]:
        """Get all table names.

        Returns
        -------
        KeysView[str]
            View of the table names

        """
        return self._tables.keys()

    def values(self) -> ValuesView[BaseTable]:
        """Get all table objects.

        Returns
        -------
        ValuesView[BaseTable]
            View of the table objects

        """
        return self._tables.values()

    def items(self) -> ItemsView[str, BaseTable]:
        """Get all (name, table) pairs.

        Returns
        -------
        ItemsView[str, BaseTable]
            View of (name, table) pairs

        """
        return self._tables.items()

    def __getitem__(self, table_name: str) -> BaseTable:
        """Get a table by name using case-insensitive matching.

        Parameters
        ----------
        table_name : str
            Table name in any casing.

        Returns
        -------
        BaseTable
            The requested table.

        Raises
        ------
        KeyError
            If no table matches ``table_name``.

        Notes
        -----
        Collection keys retain their canonical MIKE+ casing.

        """
        canonical_name = self._table_names.get(
            table_name.casefold(),
            table_name,
        )
        return self._tables[canonical_name]

    def __contains__(self, table_name: str) -> bool:
        """Check for a table using case-insensitive matching.

        Parameters
        ----------
        table_name : str
            Table name in any casing.

        Returns
        -------
        bool
            Whether a matching table exists.

        """
        return (
            isinstance(table_name, str) and table_name.casefold() in self._table_names
        )

    def __iter__(self):
        """Get an iterator over table names.

        Returns
        -------
            Iterator over table names

        """
        return iter(self._tables)
