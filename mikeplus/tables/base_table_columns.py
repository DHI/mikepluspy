"""Base class for column enumeration-like access."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
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
            c.Field for c in self._table._net_table.Columns
        )

    def __iter__(self):
        """Make the columns iterable.
        
        Returns
        -------
        iterator
            Iterator over column names

        """
        return iter(self._column_names)

    def __contains__(self, item):
        """Check if a column exists.
        
        Parameters
        ----------
        item : str
            Column name to check
            
        Returns
        -------
        bool
            True if the column exists, False otherwise

        """
        return item in self._column_names
