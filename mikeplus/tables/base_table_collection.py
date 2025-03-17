"""
Base table collection for MIKE+ database tables.
"""
from typing import List, Any, Tuple


class BaseTableCollection:
    """A dict-like collection of tables in a model database.
    
    This class provides a base implementation for table collections in a model database. 
    """
    
    def __init__(self, data_table_container):
        """Initialize a new BaseTableCollection.
        
        Args:
            data_table_container: The underlying data table container
        """
        self._data_table_container = data_table_container
        self._tables = {}
    
    def keys(self) -> List[str]:
        """Get a list of all table names.
        
        Returns:
            List of table names
        """
        pass
    
    def values(self) -> List[Any]:
        """Get a list of all table objects.
        
        Returns:
            List of table objects
        """
        pass
    
    def items(self) -> List[Tuple[str, Any]]:
        """Get a list of (name, table) pairs.
        
        Returns:
            List of (name, table) tuples
        """
        pass
    
    def __getitem__(self, table_name: str):
        """Get a table by name.
        
        Args:
            table_name: Name of the table to get
            
        Returns:
            The requested table
            
        Raises:
            KeyError: If the table does not exist
        """
        pass
    
    def __contains__(self, table_name: str) -> bool:
        """Check if a table exists.
        
        Args:
            table_name: Name of the table to check
            
        Returns:
            True if the table exists, False otherwise
        """
        pass
    
    def __iter__(self):
        """Get an iterator over table names.
        
        Returns:
            Iterator over table names
        """
        pass
