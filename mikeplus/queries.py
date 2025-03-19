"""
Query implementation classes for database operations.
"""
from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .tables import BaseTable

from datetime import datetime

from .dotnet import as_dotnet_list
from .dotnet import from_dotnet_dict
from .dotnet import from_dotnet_datetime
from .dotnet import to_dotnet_datetime

from System import String
from System import Nullable
from System import Object
from System.Collections.Generic import Dictionary

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

        self._validate_columns()

    def _validate_columns(self):
        """Validate the columns specified in the query."""
        self._columns = list(self._columns)
        if not self._columns:
            self._columns = list(self._table.columns)
        else:
            invalid_columns = [col for col in self._columns if col not in self._table.columns]
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
        
    def execute(self) -> dict[str, dict[str, any]]:
        """Execute the SELECT query.
        
        Returns:
            Dictionary of dictionaries representing rows
        """
        net_table = self._table._net_table
        
        result = net_table.GetMuidAndFieldsWhereOrder(
            as_dotnet_list(self._columns),
        )
        result = from_dotnet_dict(result)
        
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


class InsertQuery(BaseQuery):
    """Query class for INSERT operations."""
    
    def __init__(self, table: BaseTable, values: dict[str, any] = {}):
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
        net_table = self._table._net_table
        
        values = self._values.copy()
        muid = values.pop("MUID", net_table.CreateUniqueMuid())
        
        if net_table.IsMuidExistInActive(muid, None):
            raise ValueError(f"MUID {muid} already exists in {self._table.name} for active scenario.")

        geometry = values.pop("geometry", None)

        if geometry:
            if isinstance(geometry, str):
                geometry = GeoAPIHelper.GetIGeometryFromWKT(geometry)
            else:
                shapely = self._get_shapely()
                geometry = GeoAPIHelper.GetIGeometryFromWKT(shapely.to_wkt(geometry))

        net_values = Dictionary[String, Object]() if values else None

        for column, value in values.items():
            net_value = None
            if isinstance(value, int):
                net_value = Nullable[int](value)
            elif isinstance(value, datetime):
                net_value = to_dotnet_datetime(value)
            else:
                net_value = value
            net_values[column] = net_value

        _, inserted_muid = net_table.InsertByCommand(
            muid, 
            geometry,
            net_values,
        )

        return inserted_muid


class UpdateQuery(BaseQuery):
    """Query class for UPDATE operations."""
    
    def __init__(self, table: BaseTable, values: dict[str, any]):
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
        
    def execute(self):
        """Execute the UPDATE query.
        
        Returns:
            List of MUIDs updated
            
        Raises:
            ValueError: If no WHERE conditions specified and all() not called
        """
        # Safety check: if no conditions and all() not called, prevent accidental updates
        if not self._conditions and not self._all_rows:
            raise ValueError("Attempted to update all rows without explicit all() call. "
                           "Use where() to specify conditions or all() to update all rows.")
        
        net_table = self._table._net_table
        
        values = self._values.copy()
        
        net_values = Dictionary[String, Object]() if values else None

        for column, value in values.items():
            net_value = None
            if isinstance(value, int):
                net_value = Nullable[int](value)
            elif isinstance(value, datetime):
                net_value = to_dotnet_datetime(value)
            else:
                net_value = value
            net_values[column] = net_value

        muids = self._table.get_muids()
        updated_muids = []
        for muid in muids:
            net_table.SetValuesByCommand(muid,net_values)
            updated_muids.append(muid)

        return updated_muids

class DeleteQuery(BaseQuery):
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
    
    def execute(self):
        """Execute the DELETE query.
        
        Returns:
            List of MUIDs deleted
            
        Raises:
            ValueError: If no WHERE conditions specified and all() not called
        """
        # Safety check: if no conditions and all() not called, prevent accidental deletes
        if not self._conditions and not self._all_rows:
            raise ValueError("Attempted to delete all rows without explicit all() call. "
                           "Use where() to specify conditions or all() to delete all rows.")
            
        net_table = self._table._net_table
        muids = self._table.get_muids()
        muids_net = as_dotnet_list(muids)
        net_table.MultiDeleteByCommand(muids_net)
        return muids
