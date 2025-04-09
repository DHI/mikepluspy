"""Base table class for MIKE+ database tables."""
from __future__ import annotations

from typing import Any

from mikeplus.queries import SelectQuery
from mikeplus.queries import UpdateQuery
from mikeplus.queries import DeleteQuery
from mikeplus.queries import InsertQuery

from .base_table_columns import BaseColumns


class BaseTable:
    """Base class representing a database table."""

    def __init__(self, net_table):
        """Initialize a new table wrapper.

        Parameters
        ----------
        net_table
            The underlying .NET IMuTable object

        """
        self._net_table = net_table
        self._columns = None

    def __repr__(self) -> str:
        """Get string representation."""
        return f"{self.__class__.__name__}<{self.display_name}>"
    
    @property
    def columns(self) -> BaseColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = BaseColumns(self)
        return self._columns

    @property
    def name(self) -> str:
        """Get the table name."""
        return self._net_table.TableName

    @property
    def display_name(self) -> str:
        """Get the display name for the table."""
        return self._net_table.TableDisplayName

    @property
    def description(self) -> str:
        """Get the table description."""
        return self._net_table.Description

    def get_muids(self, order_by: str | None = None, descending: bool = False) -> list[str]:
        """Get a list of MUIDs for the table.

        Parameters
        ----------
        order_by : str or None, optional
            Column to order the MUIDs by
        descending : bool, optional
            Whether to order in descending order

        Returns
        -------
        list of str
            A list of MUIDs

        """
        return list(self._net_table.GetMuids(order_by, descending))

    def select(self, columns: list[str] = []):
        """Create a SELECT query for this table.

        Parameters
        ----------
        columns : list of str, optional
            The columns to select

        Returns
        -------
        SelectQuery
            A new SelectQuery object

        """
        return SelectQuery(self, columns)

    def insert(self, values: dict[str, Any], execute=True):
        """Insert a row with the given values.

        Parameters
        ----------
        values : dict of str to Any
            Column-value pairs to insert
        execute : bool, optional
            Whether to execute the query immediately (default: True)

        Returns
        -------
        str or InsertQuery
            If execute is True, returns the ID of the newly inserted row (MUID)
            If execute is False, returns an InsertQuery instance

        """
        query = InsertQuery(self, values=values)
        if execute:
            return query.execute()
        return query

    def update(self, values: dict[str, Any]):
        """Create an UPDATE query for this table.

        Parameters
        ----------
        values : dict of str to Any
            Column-value pairs to set in the UPDATE

        Returns
        -------
        UpdateQuery
            A new UpdateQuery object

        """
        query = UpdateQuery(self, values)
        return query

    def delete(self):
        """Create a DELETE query for this table.

        Returns
        -------
        DeleteQuery
            A new DeleteQuery object

        """
        return DeleteQuery(self)
