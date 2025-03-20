from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .base_table import BaseTable


class BaseColumns:
    """
    Base class for column enumeration-like access.
    """

    def __init__(self, table: "BaseTable"):
        """
        Initialize with a reference to the parent table.

        Args:
            table: Reference to the parent BaseTable instance
        """
        self._table = table
        self._column_names: tuple[str] = tuple(
            c.Field for c in self._table._net_table.Columns
        )

    def __iter__(self):
        """Make the columns iterable."""
        return iter(self._column_names)

    def __contains__(self, item):
        """Check if a column exists."""
        return item in self._column_names
