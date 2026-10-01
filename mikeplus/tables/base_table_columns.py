"""Base class for column enumeration-like access."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from System.Data import DbType

    from .base_table import BaseTable


class BaseColumns:
    """Base class for column enumeration-like access.

    Provides dictionary-like access to table columns.
    """

    def __init__(self, table: "BaseTable"):
        """Initialize with a reference to the parent table.

        Parameters
        ----------
        table : BaseTable
            Reference to the parent BaseTable instance

        """
        self._table = table
        self._column_names: tuple[str] = tuple(
            column.Field for column in self._table._net_table.Columns
        )
        self._columns_by_name = {name.casefold(): name for name in self._column_names}

    def __getitem__(self, column_name: str) -> str:
        """Resolve a column name to its canonical MIKE+ casing.

        Parameters
        ----------
        column_name : str
            Column name in any casing.

        Returns
        -------
        str
            The canonical MIKE+ column name.

        Raises
        ------
        KeyError
            If no column matches ``column_name``.

        """
        return self._columns_by_name[column_name.casefold()]

    def db_types(self) -> dict[str, "DbType"]:
        """Map casefolded column names to their database types.

        Read from the .NET table on each call, unlike the cached names, so
        user-defined columns added after construction are included.

        Returns
        -------
        dict[str, DbType]
            Casefolded column names mapped to their ``DbType``.

        """
        return {
            column.Field.casefold(): column.DbType
            for column in self._table._net_table.Columns
        }

    def __iter__(self):
        """Make the columns iterable.

        Returns
        -------
        iterator
            Iterator over column names

        """
        return iter(self._column_names)

    def __contains__(self, item):
        """Check for a column using case-insensitive matching.

        Parameters
        ----------
        item : str
            Column name in any casing.

        Returns
        -------
        bool
            Whether a matching column exists.

        """
        return isinstance(item, str) and item.casefold() in self._columns_by_name
