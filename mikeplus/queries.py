"""
Query implementation classes for database operations.
"""
from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .tables import BaseTable

class BaseQuery(ABC):
    """Base class for all query types."""
    
    def __init__(self, table: BaseTable):
        """Initialize a new query.
        
        Args:
            table: The table this query operates on
        """
        self._table = table
        self._conditions = []
        self._params = {}
        
    def where(self, condition: str, **params):
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
    
    @abstractmethod
    def execute(self):
        """Execute the query against the database.
        
        Returns:
            Query-type dependent result
        """
        pass


class SelectQuery(BaseQuery):
    """Query class for SELECT operations."""
    
    def __init__(self, table: BaseTable, columns: list[str] = []):
        """Initialize a new SELECT query.
        
        Args:
            table: The table to select from
            columns: The columns to select
        """
        super().__init__(table)
        self._columns = columns
        self._order_by = None
        self._limit = None
        self._offset = None
    
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
        
    def limit(self, limit: int, offset: int = 0):
        """Add a LIMIT clause to the query.
        
        Args:
            limit: Maximum number of rows to return
            offset: Number of rows to skip
            
        Returns:
            self for chaining
        """
        self._limit = limit
        self._offset = offset
        return self
        
    def execute(self):
        """Execute the SELECT query.
        
        Returns:
            List of dictionaries representing rows
        """
        pass
        
    def to_pandas(self):
        """Convert the query results to a pandas DataFrame.
        
        Returns:
            A pandas DataFrame containing the query results
        """
        pass


class InsertQuery(BaseQuery):
    """Query class for INSERT operations."""
    
    def __init__(self, table: BaseTable, *, values: dict[str, any] | None = None):
        """Initialize a new INSERT query.
        
        Args:
            table: The table to insert into
            values: Column-value pairs to insert
        """
        super().__init__(table)
        self._values = values 
        
    def execute(self):
        """Execute the INSERT query.
        
        Returns:
            The ID of the newly inserted row
        """
        pass


class UpdateQuery(BaseQuery):
    """Query class for UPDATE operations."""
    
    def __init__(self, table: BaseTable, values: dict[str, any] | None = None):
        """Initialize a new UPDATE query.
        
        Args:
            table: The table to update
            values: Column-value pairs to update
        """
        super().__init__(table)
        self._sets = values or {}
        
    def execute(self):
        """Execute the UPDATE query.
        
        Returns:
            Number of rows affected
        """
        pass


class DeleteQuery(BaseQuery):
    """Query class for DELETE operations."""
    
    def __init__(self, table: BaseTable):
        """Initialize a new DELETE query.
        
        Args:
            table: The table to delete from
        """
        super().__init__(table)
    
    def execute(self):
        """Execute the DELETE query.
        
        Returns:
            Number of rows affected
        """
        pass
