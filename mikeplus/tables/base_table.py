"""
Base table class for MIKE+ database tables.
"""
from typing import List


class BaseTable:
    """Base class representing a database table."""
    
    def __init__(self, net_table):
        """Initialize a new table wrapper.
        
        Args:
            net_table: The underlying .NET IMuTable object
        """
        self._net_table = net_table
        
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

    def get_muids(self, order_by: str = None, descending: bool = False) -> list[str]:
        """Get a list of MUIDs for the table.
        
        Args:
            order_by: Column to order the MUIDs by
            descending: Whether to order in descending order
            
        Returns:
            A list of MUIDs
        """
        return list(self._net_table.GetMuids(order_by, descending))
        
    def select(self, *columns):
        """Create a SELECT query for this table.
        
        Args:
            columns: The columns to select
            
        Returns:
            A new SelectQuery object
        """
        pass
        
    def insert(self, **values):
        """Insert a row with the given values.
        
        Args:
            values: Column-value pairs to insert
            
        Returns:
            The ID of the newly inserted row (MUID)
        """
        pass
        
    def update(self):
        """Create an UPDATE query for this table.
        
        Returns:
            A new UpdateQuery object
        """
        pass
        
    def delete(self):
        """Create a DELETE query for this table.
        
        Returns:
            A new DeleteQuery object
        """
        pass
