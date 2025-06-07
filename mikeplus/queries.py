"""Query implementation classes for database operations.

This module provides a set of query classes for working with MIKE+ database tables.
It implements a fluent interface for common database operations (SELECT, INSERT,
UPDATE, DELETE) with chainable methods and consistent error handling.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, TypeVar, Generic, Any, Union

if TYPE_CHECKING:
    from .tables import BaseTable


# Replace imports from converters with imports from dotnet
from .dotnet import DotNetConverter


# Define a TypeVar for the return type of execute
QueryResultT = TypeVar("QueryResultT")


class BaseQuery(Generic[QueryResultT], ABC):
    """Base class for all query types."""

    def __init__(self, table: BaseTable):
        """Initialize a new query.

        Parameters
        ----------
        table : BaseTable
            The table this query operates on

        """
        self._table = table
        self._conditions: list[str] = []
        self._params: dict[str, str] = {}
        self._executed = False

    def __repr__(self) -> str:
        """Get nice string representation."""
        return (
            f"{self.__class__.__name__}<{self._table.name}, executed={self._executed}>"
        )

    def where(self, condition: str, params: dict[str, str] = {}):
        """Add a WHERE condition to the query.

        Parameters
        ----------
        condition : str
            SQL-like condition string
        params : dict of str to str, optional
            Named parameters for the condition

        Returns
        -------
        self
            For method chaining

        """
        self._conditions.append(condition)
        self._params.update(params)
        return self

    def by_muid(self, muid_or_muids: str | list[str] | tuple[str]):
        """Filter the query by one or more MUIDs.

        Parameters
        ----------
        muid_or_muids : str or list/tuple of str
            A single MUID string, or a list/tuple of MUID strings.

        Returns
        -------
        self
            The query instance for method chaining.

        Raises
        ------
        ValueError
            If `muid_or_muids` is not a string, or a list/tuple of strings,
            or if items in list/tuple are not strings.
        ValueError
            If `muid_or_muids` is an empty list/tuple.
        """
        if isinstance(muid_or_muids, str):
            self.where(f"MUID = '{muid_or_muids}'")
        elif isinstance(muid_or_muids, (list, tuple)):
            if not muid_or_muids:
                raise ValueError(
                    f"The muid_or_muids list/tuple cannot be empty. You provided: {muid_or_muids}."
                )
            if not all(isinstance(muid, str) for muid in muid_or_muids):
                types = [type(muid) for muid in muid_or_muids]
                raise ValueError(
                    f"All items in muid_or_muids list/tuple must be strings. You provided: {types}."
                )

            condition = f"MUID IN ({', '.join(f"'{muid}'" for muid in muid_or_muids)})"
            self.where(condition)
        else:
            raise ValueError(
                "by_muid() accepts a single MUID string or a list/tuple of MUID strings."
            )
        return self

    def _build_where_clause(self):
        """Build the WHERE clause from conditions.

        Returns
        -------
        str or None
            String of the WHERE clause or None if no conditions

        """
        if not self._conditions:
            return None

        wrapped_conditions = [f"({condition})" for condition in self._conditions]
        where_clause = " AND ".join(wrapped_conditions)

        for key, value in self._params.items():
            if isinstance(value, (int, float)):
                where_clause = where_clause.replace(f":{key}", str(value))
            else:
                where_clause = where_clause.replace(f":{key}", f"'{str(value)}'")

        return where_clause

    def reset(self):
        """Reset the query execution status to allow re-execution.

        Returns
        -------
        self
            For method chaining

        """
        self._executed = False
        return self

    def execute(self) -> QueryResultT:
        """Execute the query against the database.

        Template method that handles execution tracking and delegates to
        _execute_impl for the actual query execution.

        Returns
        -------
        QueryResultT
            Query-type dependent result

        Raises
        ------
        RuntimeError
            If the query has already been executed

        """
        if self._executed:
            raise RuntimeError(
                "Query has already been executed. Use reset() to execute again."
            )

        self._executed = True
        return self._execute_impl()

    @abstractmethod
    def _execute_impl(self) -> QueryResultT:
        """Implement the actual query execution.

        This abstract method must be implemented by subclasses to perform
        the actual database operation.

        Returns
        -------
        QueryResultT
            Query-type dependent result

        Notes
        -----
        This is an internal implementation method called by execute().

        """
        pass


class SelectQuery(BaseQuery[Union[dict[str, dict[str, Any]], None]]):
    """Query class for SELECT operations."""

    def __init__(self, table: BaseTable, columns: list[str] = []):
        """Initialize a new SELECT query.

        Parameters
        ----------
        table : BaseTable
            The table to select from
        columns : list of str, optional
            The columns to select

        """
        super().__init__(table)
        self._columns = columns
        self._order_by: tuple[str, bool] | None = None

        self._validate_columns()

    def _validate_columns(self):
        """Validate the columns specified in the query."""
        self._columns = list(self._columns)
        if not self._columns:
            self._columns = list(self._table.columns)
        else:
            invalid_columns = [
                col for col in self._columns if col not in self._table.columns
            ]
            if invalid_columns:
                raise ValueError(f"Invalid columns: {invalid_columns}")

    def order_by(self, column: str, descending: bool = False):
        """Add an ORDER BY clause to the query.

        Parameters
        ----------
        column : str
            Column name to order by
        descending : bool, optional
            Whether to sort in descending order

        Returns
        -------
        self
            For method chaining

        """
        self._order_by = (column, descending)
        return self

    def _execute_impl(self) -> dict[str, dict[str, Any]] | None:
        """Implement the SELECT query execution.

        Returns
        -------
        dict or None
            Dictionary of dictionaries representing rows

        """
        net_table = self._table._net_table

        # Build where clause
        where_clause = self._build_where_clause()
        order_column = self._order_by[0] if self._order_by else None
        ascending = (
            not self._order_by[1] if self._order_by else True
        )  # order_by uses descending, but GetMuidAndFieldsWhereOrder uses ascending

        result = net_table.GetMuidAndFieldsWhereOrder(
            DotNetConverter.as_dotnet_list(self._columns),
            where_clause,
            order_column,
            ascending,
        )

        result = DotNetConverter.from_dotnet_dictionary(result)

        return result

    def to_pandas(self):
        """Convert the query results to a pandas DataFrame.

        Returns
        -------
        pandas.DataFrame
            A pandas DataFrame containing the query results

        """
        import pandas as pd

        result = self.execute()

        if not result:
            return pd.DataFrame(index=pd.Index([], name="MUID"), columns=self._columns)

        df_result = pd.DataFrame(result).T
        df_result.columns = self._columns
        return df_result

    def to_dataframe(self):
        """Convert the query results to a pandas DataFrame.

        Returns
        -------
        pandas.DataFrame
            A pandas DataFrame containing the query results

        """
        return self.to_pandas()


class InsertQuery(BaseQuery[str]):
    """Query class for INSERT operations."""

    def __init__(self, table: BaseTable, values: dict[str, Any] = {}):
        """Initialize a new INSERT query.

        Parameters
        ----------
        table : BaseTable
            The table to insert into
        values : dict of str to Any, optional
            Column-value pairs to insert

        """
        super().__init__(table)
        self._values = values

    def _execute_impl(self) -> str:
        """Implement the INSERT query execution.

        Returns
        -------
        str
            The MUID of the newly inserted row

        """
        net_table = self._table._net_table

        values = self._values.copy()
        muid = values.pop("MUID", net_table.CreateUniqueMuid())

        if net_table.IsMuidExistInActive(muid, None):
            raise ValueError(
                f"MUID {muid} already exists in {self._table.name} for active scenario."
            )

        geometry = values.pop("geometry", None)

        if geometry:
            geometry = DotNetConverter.to_dotnet_geometry(geometry)

        net_values = DotNetConverter.to_dotnet_dictionary(values) if values else None

        _, inserted_muid = net_table.InsertByCommand(
            muid,
            geometry,
            net_values,
        )

        return inserted_muid


class UpdateQuery(BaseQuery[list[str]]):
    """Query class for UPDATE operations."""

    def __init__(self, table: BaseTable, values: dict[str, Any]):
        """Initialize a new UPDATE query.

        Parameters
        ----------
        table : BaseTable
            The table to update
        values : dict of str to Any
            Column-value pairs to update

        """
        super().__init__(table)
        self._values = values
        self._all_rows = False

    def all(self):
        """Explicitly indicate that this query should affect all rows.

        Returns
        -------
        self
            For method chaining

        """
        self._all_rows = True
        return self

    def _execute_impl(self) -> list[str]:
        """Implement the UPDATE query execution.

        Returns
        -------
        list of str
            List of MUIDs updated

        """
        # Safety check: if no conditions and all() not called, prevent accidental updates
        if not self._conditions and not self._all_rows:
            raise ValueError(
                "Attempted to update all rows without explicit all() call. "
                "Use where() to specify conditions or all() to update all rows."
            )
        net_table = self._table._net_table

        values = self._values.copy()

        net_values = DotNetConverter.to_dotnet_dictionary(values) if values else None

        where_clause = self._build_where_clause()

        muids = self._table.get_muids()

        if where_clause:
            filtered_result = net_table.GetMuidsWhere(where_clause)
            muids = list(filtered_result)

        updated_muids = []
        for muid in muids:
            net_table.SetValuesByCommand(muid, net_values)
            updated_muids.append(muid)

        return updated_muids


class DeleteQuery(BaseQuery[list[str]]):
    """Query class for DELETE operations."""

    def __init__(self, table: BaseTable):
        """Initialize a new DELETE query.

        Parameters
        ----------
        table : BaseTable
            The table to delete from

        """
        super().__init__(table)
        self._all_rows = False

    def all(self):
        """Explicitly indicate that this query should affect all rows.

        Returns
        -------
        self
            For method chaining

        """
        self._all_rows = True
        return self

    def _execute_impl(self) -> list[str]:
        """Implement the DELETE query execution.

        Returns
        -------
        list of str
            List of MUIDs deleted

        Raises
        ------
        ValueError
            If no WHERE conditions specified and all() not called

        """
        # Safety check: if no conditions and all() not called, prevent accidental deletes
        if not self._conditions and not self._all_rows:
            raise ValueError(
                "Attempted to delete all rows without explicit all() call. "
                "Use where() to specify conditions or all() to delete all rows."
            )

        net_table = self._table._net_table

        where_clause = self._build_where_clause()

        muids = self._table.get_muids()

        if where_clause:
            filtered_result = net_table.GetMuidsWhere(where_clause)
            muids = list(filtered_result)

        muids_net = DotNetConverter.as_dotnet_list(muids)
        net_table.MultiDeleteByCommand(muids_net)
        return muids
