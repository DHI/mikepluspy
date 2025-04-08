"""
Query implementation classes for database operations.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, TypeVar, Generic, Any

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

        Args:
            table: The table this query operates on
        """
        self._table = table
        self._conditions: list[str] = []
        self._params: dict[str, str] = {}
        self._executed = False

    def where(self, condition: str, params: dict[str, str] = {}):
        """Add a WHERE condition to the query.

        Args:
            condition: SQL-like condition string
            params: Named parameters for the condition

        Returns:
            self for chaining
        """
        self._conditions.append(condition)
        self._params.update(params)
        return self

    def _build_where_clause(self):
        """Build the WHERE clause from conditions.

        Returns:
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

        Returns:
            self for chaining
        """
        self._executed = False
        return self

    def execute(self) -> QueryResultT:
        """Execute the query against the database.

        Template method that handles execution tracking and delegates to
        _execute_impl for the actual query execution.

        Returns:
            Query-type dependent result

        Raises:
            RuntimeError: If the query has already been executed
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

        Returns:
            Query-type dependent result
        """
        pass


class SelectQuery(BaseQuery[dict[str, dict[str, Any]] | None]):
    """Query class for SELECT operations."""

    def __init__(self, table: BaseTable, columns: list[str] = []):
        """Initialize a new SELECT query.

        Args:
            table: The table to select from
            columns: The columns to select
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

        Args:
            column: Column name to order by
            descending: Whether to sort in descending order

        Returns:
            self for chaining
        """
        self._order_by = (column, descending)
        return self

    def _execute_impl(self) -> dict[str, dict[str, Any]] | None:
        """Implement the SELECT query execution.

        Returns:
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

        Returns:
            A pandas DataFrame containing the query results
        """
        import pandas as pd

        result = self.execute()
        df = pd.DataFrame(result).T
        df.columns = self._columns
        return df


class InsertQuery(BaseQuery[str]):
    """Query class for INSERT operations."""

    def __init__(self, table: BaseTable, values: dict[str, Any] = {}):
        """Initialize a new INSERT query.

        Args:
            table: The table to insert into
            values: Column-value pairs to insert
        """
        super().__init__(table)
        self._values = values

    def _execute_impl(self) -> str:
        """Implement the INSERT query execution.

        Returns:
            The ID of the newly inserted row
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

        Args:
            table: The table to update
            values: Column-value pairs to update
        """
        super().__init__(table)
        self._values = values
        self._all_rows = False

    def all(self):
        """Explicitly indicate that this query should affect all rows.

        Returns:
            self for chaining
        """
        self._all_rows = True
        return self

    def _execute_impl(self) -> list[str]:
        """Implement the UPDATE query execution.

        Returns:
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

        Args:
            table: The table to delete from
        """
        super().__init__(table)
        self._all_rows = False

    def all(self):
        """Explicitly indicate that this query should affect all rows.

        Returns:
            self for chaining
        """
        self._all_rows = True
        return self

    def _execute_impl(self) -> list[str]:
        """Implement the DELETE query execution.

        Returns:
            List of MUIDs deleted

        Raises:
            ValueError: If no WHERE conditions specified and all() not called
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
